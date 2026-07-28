# Tuần 4 — Causal self-attention / Week 4 — Causal self-attention

## Mục tiêu học tập / Learning objectives

- Tính scaled dot-product attention và giải thích scale $1/\sqrt{d_k}$. / Compute scaled dot-product attention and explain scaling.
- Xây causal mask không nhìn tương lai. / Build a causal mask that prevents future access.
- Theo dõi shapes và kiểm thử leakage bằng perturbation. / Trace shapes and test leakage by perturbation.
- Phân tích chi phí $O(T^2d)$. / Analyze quadratic cost.

## Lý thuyết sâu / Deep theory

Từ $X\in\mathbb R^{B\times T\times d}$: $Q=XW_Q$, $K=XW_K$, $V=XW_V$. Attention là

$$A=\operatorname{softmax}\left(\frac{QK^\top}{\sqrt{d_k}}+M\right),\qquad Y=AV,$$

với $M_{ij}=0$ nếu $j\le i$, ngược lại $-\infty$. Softmax chạy trên chiều key cuối; mỗi hàng $A_{i,:}$ tổng bằng 1. Scale giữ variance logits ổn định khi $d_k$ tăng, tránh softmax bão hoà. / Scaling prevents dot products from growing with key dimension and saturating softmax.

Causality là invariant: output tại vị trí $t$ không được đổi nếu chỉ sửa token sau $t$. Padding mask và causal mask giải quyết hai vấn đề khác nhau. Numerical stability đòi masked fill trước softmax và dtype-aware negative values. / Causal and padding masks are distinct constraints.

## Buổi 1 — Tính attention bằng tay / Session 1 — Attention by hand

1. Dùng $T=3,d_k=2$, tính $QK^T$, scale, mask, softmax và weighted sum. / Calculate every matrix by hand.
2. Kiểm tra row sums, upper-triangle zeros và output shape. / Check invariants.
3. Giải thích attention weights không mặc nhiên là causal explanation. / Explain why weights are not automatically explanations.

```python
import math  # Căn bậc hai dùng để scale attention scores.
import torch  # Matrix multiplication, mask và softmax.

def causal_attention(q, k, v):
    # q/k/v thường có shape (..., T, d_head); -2 chính là chiều thời gian T.
    T = q.size(-2)
    # Tính QK^T và chia sqrt(d_head) để logits không quá lớn khi d_head tăng.
    scores = q @ k.transpose(-2,-1) / math.sqrt(q.size(-1))
    # triu(..., 1) đánh dấu vùng phía trên đường chéo: các token ở tương lai.
    scores = scores.masked_fill(torch.triu(torch.ones(T,T,dtype=torch.bool),1), float("-inf"))
    # Softmax theo key positions; vị trí -inf nhận trọng số đúng bằng 0.
    weights = torch.softmax(scores, dim=-1)
    # Trộn value bằng trọng số attention và trả weights để kiểm tra/debug.
    return weights @ v, weights
```

## Buổi 2 — Implementation và test leakage / Session 2 — Implementation and leakage tests

Đọc `CausalSelfAttention.forward` trong [`nanoGPTsource/model.py`](../../../nanoGPTsource/model.py), đối chiếu manual attention với fused SDPA. / Compare manual attention with fused scaled-dot-product attention.

Hands-on:

1. Tạo input `x`, clone thành `x2`, chỉ thay các vị trí sau $t$. / Perturb only future positions.
2. Assert outputs `[:, :t+1]` gần bằng nhau ở eval mode. / Assert prefix outputs are unchanged.
3. Benchmark $T=64,128,256$ và vẽ memory/time theo $T^2$. / Benchmark quadratic scaling.
4. Thử bỏ mask để thấy test thất bại; khôi phục mask. / Demonstrate that the test catches leakage.

## Câu hỏi thảo luận / Discussion questions

1. Vì sao mask phải áp trước softmax? / Why mask before softmax?
2. Scale thiếu gây vấn đề gì khi $d_k$ lớn? / What fails without scaling?
3. Causal mask khác padding mask thế nào? / How do causal and padding masks differ?
4. Vì sao attention có chi phí bình phương theo context? / Why is cost quadratic?
5. Attention weights có đủ để giải thích quyết định mô hình không? / Are weights sufficient explanations?

## Bài tập về nhà / Homework

Implement một attention head không dùng module `MultiheadAttention`; nộp shape tests, normalization test, causal perturbation test, gradient finite test và benchmark ba context lengths. / Implement and thoroughly test a single causal head, including finite gradients and a scaling benchmark.

## Rubric đánh giá / Assessment rubric

| Hạng mục / Criterion | Điểm |
|---|---:|
| Công thức/shape đúng / math and shapes | 25 |
| Mask và leakage test / causality | 30 |
| Numerical/gradient tests | 20 |
| Benchmark và phân tích / benchmark | 15 |
| Mã, giải thích / quality | 10 |

## ⚠️ Ngộ nhận thường gặp / Common misconceptions

- Mask bằng 0 sau softmax vẫn đúng; khi đó cần renormalize và dễ sai. / Zeroing after softmax is not equivalent.
- Query tại $t$ chỉ attend token $t$; nó được attend toàn prefix. / A query attends the whole allowed prefix.
- `-1e9` luôn an toàn mọi dtype. / Mask constants are dtype-sensitive.
- Causal mask tự xử lý PAD. / Padding requires a separate mask.
