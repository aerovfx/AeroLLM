"""Mini GPT lab chạy nhanh trên CPU; dùng cho tuần 1–9."""

from __future__ import annotations

import math
import random
from dataclasses import dataclass

import torch
import torch.nn as nn
import torch.nn.functional as F

SEED = 3407
random.seed(SEED)
torch.manual_seed(SEED)


class CharTokenizer:
    """Tokenizer ký tự nhỏ, đủ để quan sát encode/decode."""

    def __init__(self, text: str):
        chars = sorted(set(text))
        self.stoi = {char: index for index, char in enumerate(chars)}
        self.itos = {index: char for char, index in self.stoi.items()}

    def encode(self, text: str) -> list[int]:
        return [self.stoi[char] for char in text]

    def decode(self, token_ids: list[int]) -> str:
        return "".join(self.itos[token_id] for token_id in token_ids)

    @property
    def vocab_size(self) -> int:
        return len(self.stoi)


@dataclass
class Config:
    vocab_size: int
    block_size: int = 16
    n_embd: int = 32
    n_head: int = 4
    n_layer: int = 2


class CausalAttention(nn.Module):
    def __init__(self, config: Config):
        super().__init__()
        assert config.n_embd % config.n_head == 0
        self.n_head = config.n_head
        self.head_dim = config.n_embd // config.n_head
        self.qkv = nn.Linear(config.n_embd, 3 * config.n_embd)
        self.output = nn.Linear(config.n_embd, config.n_embd)

    def forward(self, hidden: torch.Tensor) -> torch.Tensor:
        batch, time, width = hidden.shape
        qkv = self.qkv(hidden).reshape(batch, time, 3, self.n_head, self.head_dim)
        query, key, value = qkv.permute(2, 0, 3, 1, 4)
        attended = F.scaled_dot_product_attention(query, key, value, is_causal=True)
        merged = attended.transpose(1, 2).reshape(batch, time, width)
        return self.output(merged)


class Block(nn.Module):
    def __init__(self, config: Config):
        super().__init__()
        self.norm1 = nn.LayerNorm(config.n_embd)
        self.attention = CausalAttention(config)
        self.norm2 = nn.LayerNorm(config.n_embd)
        self.mlp = nn.Sequential(
            nn.Linear(config.n_embd, 4 * config.n_embd),
            nn.GELU(),
            nn.Linear(4 * config.n_embd, config.n_embd),
        )

    def forward(self, hidden: torch.Tensor) -> torch.Tensor:
        hidden = hidden + self.attention(self.norm1(hidden))
        return hidden + self.mlp(self.norm2(hidden))


class MiniGPT(nn.Module):
    def __init__(self, config: Config):
        super().__init__()
        self.config = config
        self.token_embedding = nn.Embedding(config.vocab_size, config.n_embd)
        self.position_embedding = nn.Embedding(config.block_size, config.n_embd)
        self.blocks = nn.ModuleList([Block(config) for _ in range(config.n_layer)])
        self.norm = nn.LayerNorm(config.n_embd)
        self.head = nn.Linear(config.n_embd, config.vocab_size)

    def forward(self, token_ids: torch.Tensor, targets: torch.Tensor | None = None):
        _, time = token_ids.shape
        positions = torch.arange(time, device=token_ids.device)
        hidden = self.token_embedding(token_ids) + self.position_embedding(positions)
        for block in self.blocks:
            hidden = block(hidden)
        logits = self.head(self.norm(hidden))
        loss = None
        if targets is not None:
            loss = F.cross_entropy(logits.flatten(0, 1), targets.flatten())
        return logits, loss


def get_batch(data: torch.Tensor, batch_size: int, block_size: int):
    starts = torch.randint(len(data) - block_size, (batch_size,))
    inputs = torch.stack([data[start : start + block_size] for start in starts])
    targets = torch.stack([data[start + 1 : start + block_size + 1] for start in starts])
    return inputs, targets


@torch.no_grad()
def generate(model: MiniGPT, prompt: torch.Tensor, new_tokens: int = 40) -> torch.Tensor:
    model.eval()
    for _ in range(new_tokens):
        context = prompt[:, -model.config.block_size :]
        logits, _ = model(context)
        probabilities = torch.softmax(logits[:, -1] / 0.8, dim=-1)
        prompt = torch.cat([prompt, torch.multinomial(probabilities, 1)], dim=1)
    return prompt


def main() -> None:
    corpus = ("học máy là học từ dữ liệu. " * 30).strip()
    tokenizer = CharTokenizer(corpus)
    assert tokenizer.decode(tokenizer.encode(corpus[:20])) == corpus[:20]
    data = torch.tensor(tokenizer.encode(corpus), dtype=torch.long)
    config = Config(vocab_size=tokenizer.vocab_size)
    model = MiniGPT(config)
    optimizer = torch.optim.AdamW(model.parameters(), lr=3e-3)
    initial_loss = None
    for step in range(30):
        inputs, targets = get_batch(data, batch_size=8, block_size=config.block_size)
        _, loss = model(inputs, targets)
        initial_loss = loss.item() if initial_loss is None else initial_loss
        optimizer.zero_grad(set_to_none=True)
        loss.backward()
        nn.utils.clip_grad_norm_(model.parameters(), 1.0)
        optimizer.step()
    prompt_text = "học "
    prompt = torch.tensor([tokenizer.encode(prompt_text)], dtype=torch.long)
    output = generate(model, prompt)
    print({"parameters": sum(p.numel() for p in model.parameters()),
           "initial_loss": round(initial_loss, 4), "final_loss": round(loss.item(), 4),
           "perplexity": round(math.exp(min(loss.item(), 20)), 2)})
    print(tokenizer.decode(output[0].tolist()))
    assert torch.isfinite(loss)


if __name__ == "__main__":
    main()
