---
layout: course
title: "Week07"
permalink: /2_LLM_Core/llm-from-scratch-10weeks/lessons/week07.html
---

# Tuần 07 — Lắp ráp GPT hoàn chỉnh / Assemble a complete GPT

[← Tuần 6](week06.md) · [Mục lục khoá](../INDEX.md) · [40 tuần](../../../courses/WEEK_INDEX.md) · [Lịch 20 buổi](../schedule.md) · [Tuần 8 →](week08.md)

## Mục tiêu học tập / Learning objectives

- Kết nối tokenizer, embedding, positional signal, block và LM head / connect tokenizer, embeddings, position signal, blocks, and LM head.
- Hiểu weight tying, khởi tạo và ngân sách tham số / understand weight tying, initialization, and parameter budgets.
- Kiểm thử causal leakage và tính đúng của loss dịch một token / test causal leakage and next-token loss.
- Sinh văn bản từ mô hình chưa huấn luyện như một smoke test / generate from an untrained model as a smoke test.

## Lý thuyết sâu / Deep theory

Token IDs $t_{1:T}$ thành $X_0=E[t]+P[0:T]$. Sau $L$ blocks: $H=N(X_L)$, logits $Z=HW_U$. Phân phối kế tiếp là $p(t_{i+1}|t_{\le i})=\operatorname{softmax}(Z_i)$. Cross-entropy:

$$\mathcal{L}=-\frac1{BT}\sum_{b,i}\log p_\theta(t^{(b)}_{i+1}\mid t^{(b)}_{\le i}).$$

Weight tying đặt $W_U=E^\top$, giảm $Vd$ tham số và ép không gian đọc/ghi token dùng chung. Khởi tạo Gaussian scale khoảng $0.02$ là điểm bắt đầu; residual projection đôi khi scale thêm $1/\sqrt{2L}$ để phương sai không tăng theo độ sâu.

## Buổi 1 — Kiến trúc và cấu hình / Session 1 — Architecture and configuration

```python
from dataclasses import dataclass  # Tạo object cấu hình có type annotation/default rõ ràng.
import torch  # Tensor, arange và loss operations.
import torch.nn as nn  # Embedding, Linear, LayerNorm và ModuleList.

@dataclass
class GPTConfig:
    vocab_size: int  # Số token khác nhau; bắt buộc vì phụ thuộc tokenizer.
    block_size: int = 256  # Context length tối đa.
    n_layer: int = 6  # Số Transformer blocks xếp chồng.
    n_head: int = 6  # Số attention heads trong mỗi block.
    n_embd: int = 384  # Residual/model width; phải chia hết cho n_head.
    dropout: float = 0.0  # Tỷ lệ dropout dùng trong training.
    bias: bool = False  # Có dùng bias trong Linear/Norm hay không.

class GPT(nn.Module):
    def __init__(self, cfg, Block):
        super().__init__()  # Khởi tạo Module trước khi gán submodule.
        self.cfg = cfg  # Giữ cấu hình để forward kiểm tra block_size.
        # Token table và learned positional table đều trả vector n_embd.
        self.tok = nn.Embedding(cfg.vocab_size, cfg.n_embd)
        self.pos = nn.Embedding(cfg.block_size, cfg.n_embd)
        # Tạo n_layer block độc lập; không chia sẻ trọng số giữa các layer.
        self.blocks = nn.ModuleList([Block(cfg) for _ in range(cfg.n_layer)])
        self.norm = nn.LayerNorm(cfg.n_embd)  # Final normalization trước logits.
        self.head = nn.Linear(cfg.n_embd, cfg.vocab_size, bias=False)  # Hidden → vocab logits.
        self.head.weight = self.tok.weight  # Weight tying giảm tham số và thường cải thiện học.

    def forward(self, ids, targets=None):
        B, T = ids.shape  # ids có shape (batch, sequence).
        if T > self.cfg.block_size:
            raise ValueError("sequence too long")  # Không có position embedding ngoài bảng.
        # arange nằm cùng device để tránh lỗi CPU/GPU; position vectors broadcast qua batch.
        x = self.tok(ids) + self.pos(torch.arange(T, device=ids.device))
        for block in self.blocks:
            x = block(x)  # Giữ shape (B,T,n_embd) qua mọi block.
        logits = self.head(self.norm(x))  # Kết quả shape (B,T,vocab_size).
        # Khi inference không có targets nên không tốn phép tính cross-entropy.
        loss = None if targets is None else nn.functional.cross_entropy(
            logits.reshape(-1, logits.size(-1)), targets.reshape(-1))
        return logits, loss  # Trả cả logits để sample/evaluate và loss để train.
```

### Thực hành / Hands-on

1. Tính tay tham số của embeddings, attention và MLP; đối chiếu `sum(p.numel())`.
2. Xác nhận `head.weight.data_ptr() == tok.weight.data_ptr()`.
3. Kiểm tra logits có shape `(B,T,V)` và loss scalar.
4. Thay token ở tương lai, xác minh logits quá khứ không đổi trong `eval()`.

## Buổi 2 — Khởi tạo, loss và smoke training / Session 2 — Initialization, loss, and smoke training

Áp dụng initialization có chủ đích, rồi overfit một batch. Một mô hình đúng phải giảm loss mạnh trên một batch nhỏ; nếu không, kiểm tra shift target, mask, dropout, learning rate và gradient.

```python
def init_weights(m):
    # apply(init_weights) sẽ gọi hàm này cho từng submodule trong model.
    if isinstance(m, nn.Linear):
        # GPT-style Gaussian initialization cho ma trận Linear.
        nn.init.normal_(m.weight, 0.0, 0.02)
        if m.bias is not None:
            nn.init.zeros_(m.bias)  # Bias bắt đầu ở 0.
    elif isinstance(m, nn.Embedding):
        # Khởi tạo embedding cùng độ lệch chuẩn với Linear weights.
        nn.init.normal_(m.weight, 0.0, 0.02)

def shifted_batch(tokens, block_size):
    # Cần thêm một token để tạo cả input và next-token target dài block_size.
    start = torch.randint(0, len(tokens)-block_size-1, (1,)).item()
    # Lấy đoạn liên tục để không phá quan hệ thứ tự trong language modeling.
    chunk = tokens[start:start+block_size+1]
    # Thêm chiều batch; target chính là cùng đoạn dịch trái một token.
    return chunk[:-1][None, :], chunk[1:][None, :]
```

### Lab tích hợp / Integration lab

- Dùng tokenizer/corpus của các tuần trước, train 200–500 steps trên một batch cố định.
- Ghi initial loss và so với $\log V$; sai lệch lớn bất thường báo hiệu initialization/logit scale.
- Chạy `torch.autograd.gradcheck` cho thành phần nhỏ ở double precision nếu khả thi.
- Lưu config cùng checkpoint để kiến trúc có thể tái tạo.

## Chính xác 5 câu hỏi thảo luận / Exactly 5 discussion questions

1. Weight tying tạo inductive bias nào? / What inductive bias does weight tying introduce?
2. Vì sao loss ban đầu thường gần $\log V$? / Why is initial loss often near $\log V$?
3. Causal leakage test nên thay token nào và quan sát logits nào? / How should a causal leakage test be constructed?
4. Learned positions giới hạn context extension ra sao? / How do learned positions constrain context extension?
5. Overfit-one-batch phân biệt bug mô hình với bug dữ liệu thế nào? / How does one-batch overfitting isolate model versus data bugs?

## Bài tập về nhà / Homework

Hoàn thiện GPT tối thiểu 4 layers từ các module tự viết. Nộp source, config JSON, parameter-budget worksheet, 8 unit tests, checkpoint overfit-one-batch và đoạn sample 200 token. Giải thích mọi khác biệt so với dự báo $\log V$ và chứng minh không causal leakage.

## Rubric đánh giá / Assessment rubric

| Tiêu chí / Criterion | Điểm / Points |
|---|---:|
| Kiến trúc GPT đúng / Correct architecture | 30 |
| Loss, shift, mask và weight tying / Loss, shifting, mask, tying | 25 |
| Bộ test có sức phát hiện lỗi / Effective tests | 20 |
| Budget và initialization / Budget and initialization | 15 |
| Báo cáo tái lập / Reproducible report | 10 |

## ⚠️ Hiểu lầm thường gặp / Common misconceptions

- Targets phải lệch một token, không trùng input / Targets are shifted by one token.
- Weight tying phải dùng cùng `Parameter`, không chỉ copy giá trị / Tying is parameter sharing, not copying.
- Output ngẫu nhiên trước training không chứng minh sampling hỏng / Random pretraining output is expected.
- `eval()` cần thiết khi test causality có dropout / Use evaluation mode for causality tests.
