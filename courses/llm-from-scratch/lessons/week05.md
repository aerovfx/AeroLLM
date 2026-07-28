# Tuần 5 — Multi-head attention / Week 5 — Multi-head attention

## Mục tiêu học tập / Learning objectives

- Mở rộng single-head thành multi-head attention (MHA). / Extend a single head into MHA.
- Suy luận điều kiện $d_{model}\bmod h=0$ và shapes reshape/transpose. / Derive head dimensions and tensor layouts.
- Hiểu concatenation, output projection, dropout và parameter count. / Understand concatenation, projection, dropout, and parameters.
- So sánh implementation thủ công với fused kernel. / Compare manual and fused implementations.

## Lý thuyết sâu / Deep theory

Với $h$ heads, $d_h=d_{model}/h$:

$$\text{head}_i=\operatorname{Attn}(XW_i^Q,XW_i^K,XW_i^V),\quad \mathrm{MHA}(X)=\operatorname{Concat}(\text{head}_1,\ldots,\text{head}_h)W^O.$$

Khi QKV và output đều dense $d\times d$, parameter chính xấp xỉ $4d^2$ (cộng bias), gần như không đổi theo số heads nếu $d$ cố định. Tuy vậy, nhiều heads làm $d_h$ nhỏ, thay đổi expressivity và kernel efficiency. / Head count redistributes a fixed representation width rather than automatically adding parameters.

Shape chuẩn: `[B,T,3d] → [B,T,3,h,d_h] → [3,B,h,T,d_h]`; attention scores `[B,h,T,T]`; concat trở lại `[B,T,d]`. `transpose` có thể tạo tensor non-contiguous; dùng `contiguous().view` hoặc `reshape` có chủ ý. / Layout errors are a common source of silent head mixing.

## Buổi 1 — Shapes, parameters, invariants / Session 1 — Shapes, parameters, invariants

1. Tính shapes cho $B=2,T=16,d=64,h=4$. / Calculate all shapes.
2. So sánh parameter count $h=1,4,8$ khi giữ $d=64$. / Compare parameter counts.
3. Xác nhận mỗi head có causal row sums bằng 1 và không có upper-triangle mass. / Validate per-head causality.

```python
import torch  # Tensor reshape và scaled-dot-product attention.
import torch.nn as nn  # Linear layers và base class Module.

class MHA(nn.Module):
    def __init__(self, d, h):
        super().__init__()  # Đăng ký đúng các submodule/tham số của PyTorch.
        assert d % h == 0  # Mỗi head phải nhận cùng số chiều nguyên.
        self.h = h  # Số attention heads.
        self.dh = d // h  # Kích thước vector của một head.
        # Một phép chiếu sinh đồng thời Q/K/V; phép chiếu cuối trộn các head.
        self.qkv = nn.Linear(d, 3*d)
        self.proj = nn.Linear(d, d)

    def forward(self, x):
        B, T, D = x.shape  # Batch, sequence length và model dimension.
        # Reshape rồi permute thành (3, B, heads, T, d_head), sau đó unpack Q/K/V.
        q, k, v = self.qkv(x).reshape(B, T, 3, self.h, self.dh).permute(2, 0, 3, 1, 4)
        # Kernel PyTorch thực hiện scale, causal mask, softmax và weighted sum.
        y = torch.nn.functional.scaled_dot_product_attention(q, k, v, is_causal=True)
        # Ghép các head về (B,T,D), rồi áp output projection.
        return self.proj(y.transpose(1,2).reshape(B,T,D))
```

## Buổi 2 — So sánh, benchmark, ablation / Session 2 — Compare, benchmark, ablate

Đọc implementation trong [`nanoGPTsource/model.py`](../../../nanoGPTsource/model.py). Đặt cùng weights cho manual và fused versions, tắt dropout, eval mode, rồi assert output/gradient gần nhau. / Align weights and compare outputs and gradients.

Hands-on: benchmark $h\in\{1,2,4,8\}$ ở $d$ cố định; ghi latency, peak memory và parameter count; chạy một mini-training controlled seed; không tuyên bố “head chuyên ngữ pháp” chỉ từ một heatmap. / Benchmark head-count choices and avoid unsupported interpretability claims.

## Câu hỏi thảo luận / Discussion questions

1. Vì sao tăng số head không nhất thiết tăng số tham số? / Why need head count not increase parameters?
2. Điều gì xảy ra khi $d_h$ quá nhỏ? / What happens when head dimension is too small?
3. Output projection có vai trò gì? / What does the output projection do?
4. Vì sao fused kernel nhanh hơn dù cùng công thức? / Why can fused kernels be faster?
5. Bằng chứng nào cần để nói các head chuyên biệt? / What evidence supports head specialization?

## Bài tập về nhà / Homework

Hoàn thiện MHA có dropout và causal behavior; nộp tests parity manual/fused, gradient, parameter counts, benchmark bốn head counts và memo chọn cấu hình. / Submit a tested MHA implementation, parity checks, benchmark, and configuration memo.

## Rubric đánh giá / Assessment rubric

| Hạng mục / Criterion | Điểm |
|---|---:|
| Reshape/transpose và output đúng / tensor correctness | 30 |
| Causality, parity, gradient tests | 25 |
| Benchmark công bằng / fair benchmark | 20 |
| Phân tích trade-off / analysis | 15 |
| Chất lượng mã và báo cáo / quality | 10 |

## ⚠️ Ngộ nhận thường gặp / Common misconceptions

- Mỗi head nhận toàn bộ $d$ chiều; thông thường mỗi head nhận $d/h$. / Each head usually receives $d/h$ dimensions.
- Nhiều head luôn tốt hơn. / More heads are not universally better.
- `view` sau transpose luôn hợp lệ. / Non-contiguous tensors require care.
- Fused attention là thuật toán khác; nó tối ưu cùng phép tính với khác biệt số nhỏ. / Fused attention optimizes the same operation.
