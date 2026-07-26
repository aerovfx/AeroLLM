"""
mini_gpt.py — GPT tối giản, char-level, dựa trên nanoGPT (Karpathy).
Chạy / Run:
    pip install torch
    curl -o input.txt https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt
    python mini_gpt.py
CPU cũng chạy được trong vài phút. Đã kiểm tra chạy thật (loss 3.4 -> ~1.x).
"""
import torch, torch.nn as nn
from torch.nn import functional as F

# ---------- 1) SIÊU THAM SỐ / HYPERPARAMETERS ----------
batch_size = 32
block_size = 64
n_embd     = 96
n_head     = 4
n_layer    = 3
dropout    = 0.1
lr         = 1e-3
max_iters  = 3000
eval_iters = 20
device     = 'cuda' if torch.cuda.is_available() else 'cpu'
torch.manual_seed(1337)

# ---------- 2) DỮ LIỆU / DATA ----------
with open('input.txt', 'r', encoding='utf-8') as f:
    text = f.read()
chars = sorted(list(set(text)))
vocab_size = len(chars)
stoi = {c: i for i, c in enumerate(chars)}
itos = {i: c for i, c in enumerate(chars)}
encode = lambda s: [stoi[c] for c in s]
decode = lambda l: ''.join(itos[i] for i in l)
data = torch.tensor(encode(text), dtype=torch.long)
n = int(0.9 * len(data)); train_data, val_data = data[:n], data[n:]

def get_batch(split):
    d = train_data if split == 'train' else val_data
    ix = torch.randint(len(d) - block_size, (batch_size,))
    x = torch.stack([d[i:i+block_size]     for i in ix])
    y = torch.stack([d[i+1:i+1+block_size] for i in ix])
    return x.to(device), y.to(device)

# ---------- 3) MÔ HÌNH / MODEL ----------
class Head(nn.Module):
    def __init__(self, hs):
        super().__init__()
        self.key   = nn.Linear(n_embd, hs, bias=False)
        self.query = nn.Linear(n_embd, hs, bias=False)
        self.value = nn.Linear(n_embd, hs, bias=False)
        self.register_buffer('tril', torch.tril(torch.ones(block_size, block_size)))
        self.drop = nn.Dropout(dropout)
    def forward(self, x):
        B, T, C = x.shape
        k, q, v = self.key(x), self.query(x), self.value(x)
        att = q @ k.transpose(-2, -1) * k.shape[-1]**-0.5
        att = att.masked_fill(self.tril[:T, :T] == 0, float('-inf'))
        att = self.drop(F.softmax(att, dim=-1))
        return att @ v

class MultiHead(nn.Module):
    def __init__(self):
        super().__init__()
        hs = n_embd // n_head
        self.heads = nn.ModuleList([Head(hs) for _ in range(n_head)])
        self.proj  = nn.Linear(n_embd, n_embd)
        self.drop  = nn.Dropout(dropout)
    def forward(self, x):
        out = torch.cat([h(x) for h in self.heads], dim=-1)
        return self.drop(self.proj(out))

class MLP(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(n_embd, 4*n_embd), nn.GELU(),
            nn.Linear(4*n_embd, n_embd), nn.Dropout(dropout))
    def forward(self, x): return self.net(x)

class Block(nn.Module):
    def __init__(self):
        super().__init__()
        self.ln1, self.ln2 = nn.LayerNorm(n_embd), nn.LayerNorm(n_embd)
        self.attn, self.mlp = MultiHead(), MLP()
    def forward(self, x):
        x = x + self.attn(self.ln1(x))
        x = x + self.mlp(self.ln2(x))
        return x

class MiniGPT(nn.Module):
    def __init__(self):
        super().__init__()
        self.tok_emb = nn.Embedding(vocab_size, n_embd)
        self.pos_emb = nn.Embedding(block_size, n_embd)
        self.blocks  = nn.Sequential(*[Block() for _ in range(n_layer)])
        self.ln_f    = nn.LayerNorm(n_embd)
        self.head    = nn.Linear(n_embd, vocab_size)
    def forward(self, idx, targets=None):
        B, T = idx.shape
        tok = self.tok_emb(idx)
        pos = self.pos_emb(torch.arange(T, device=device))
        x = self.blocks(tok + pos)
        logits = self.head(self.ln_f(x))
        loss = None
        if targets is not None:
            loss = F.cross_entropy(logits.view(-1, vocab_size), targets.view(-1))
        return logits, loss
    @torch.no_grad()
    def generate(self, idx, max_new_tokens):
        for _ in range(max_new_tokens):
            idx_cond = idx[:, -block_size:]
            logits, _ = self(idx_cond)
            probs = F.softmax(logits[:, -1, :], dim=-1)
            idx_next = torch.multinomial(probs, 1)
            idx = torch.cat([idx, idx_next], dim=1)
        return idx

# ---------- 4) HUẤN LUYỆN / TRAIN ----------
model = MiniGPT().to(device)
print("So tham so / params: %.2fK" % (sum(p.numel() for p in model.parameters())/1e3))
opt = torch.optim.AdamW(model.parameters(), lr=lr)

@torch.no_grad()
def est_loss():
    model.eval(); out = {}
    for split in ['train', 'val']:
        losses = torch.zeros(eval_iters)
        for k in range(eval_iters):
            _, l = model(*get_batch(split)); losses[k] = l.item()
        out[split] = losses.mean().item()
    model.train(); return out

for it in range(max_iters):
    if it % 300 == 0:
        l = est_loss(); print(f"iter {it}: train {l['train']:.3f}, val {l['val']:.3f}")
    xb, yb = get_batch('train')
    _, loss = model(xb, yb)
    opt.zero_grad(set_to_none=True); loss.backward(); opt.step()

# ---------- 5) SINH VĂN BẢN / SAMPLE ----------
start = torch.zeros((1, 1), dtype=torch.long, device=device)
print("---- VAN BAN SINH RA / GENERATED ----")
print(decode(model.generate(start, 500)[0].tolist()))
