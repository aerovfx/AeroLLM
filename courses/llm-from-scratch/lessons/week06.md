# Tuần 06 — MLP, chuẩn hoá và kết nối dư / MLP, normalization, and residual connections

[← Tuần 5](week05.md) · [Mục lục khoá](../INDEX.md) · [40 tuần](../../WEEK_INDEX.md) · [Lịch 20 buổi](../schedule.md) · [Tuần 7 →](week07.md)

## Mục tiêu học tập / Learning objectives

Sau tuần này, học viên có thể / By the end of this week, learners can:

- Giải thích vai trò của MLP/FFN trong việc biến đổi đặc trưng theo từng token / explain how the MLP/FFN transforms each token representation.
- Cài đặt GELU, SwiGLU, LayerNorm và RMSNorm ổn định số / implement numerically stable GELU, SwiGLU, LayerNorm, and RMSNorm.
- So sánh pre-norm với post-norm qua đường truyền gradient / compare pre-norm and post-norm through gradient paths.
- Lắp một Transformer block có residual, dropout và kiểm thử hình dạng / assemble and shape-test a Transformer block.

## Lý thuyết sâu / Deep theory

Với đầu vào $X\in\mathbb{R}^{B\times T\times d}$, FFN hoạt động độc lập trên từng vị trí:

$$\operatorname{FFN}(X)=\phi(XW_1+b_1)W_2+b_2,$$

trong đó $W_1\in\mathbb{R}^{d\times d_{ff}}$, thường $d_{ff}\approx4d$. GELU là $x\Phi(x)$; gần đúng thường dùng:

$$\operatorname{GELU}(x)\approx\tfrac12x[1+\tanh(\sqrt{2/\pi}(x+0.044715x^3))].$$

SwiGLU dùng cổng học được: $\operatorname{SwiGLU}(x)=(xW_g\odot\operatorname{SiLU}(xW_u))W_d$. Khi giữ ngân sách tham số tương đương, chiều ẩn SwiGLU thường nhỏ hơn $4d$.

LayerNorm chuẩn hoá theo chiều đặc trưng: $\mu=d^{-1}\sum_i x_i$, $\sigma^2=d^{-1}\sum_i(x_i-\mu)^2$, rồi $y_i=\gamma_i(x_i-\mu)/\sqrt{\sigma^2+\epsilon}+\beta_i$. RMSNorm bỏ phép trừ trung bình: $y_i=\gamma_i x_i/\sqrt{d^{-1}\sum_jx_j^2+\epsilon}$.

Pre-norm: $x'=x+\operatorname{Attn}(N(x));\ y=x'+\operatorname{MLP}(N(x'))$. Nhánh identity cho gradient một đường đi trực tiếp. Post-norm chuẩn hoá sau phép cộng; có thể khó tối ưu hơn khi mạng sâu.

## Buổi 1 — MLP và activation / Session 1 — MLP and activations

### Triển khai / Implementation

```python
import torch  # Tensor và tham số learnable.
import torch.nn as nn  # Linear, Dropout và Module.
import torch.nn.functional as F  # GELU/SiLU dạng hàm.

class MLP(nn.Module):
    def __init__(self, d_model: int, expansion: int = 4, dropout: float = 0.0):
        super().__init__()  # Khởi tạo base Module.
        hidden = expansion * d_model  # Mở rộng chiều trong MLP, thường gấp 4 lần.
        self.up = nn.Linear(d_model, hidden)  # Chiếu từ residual width lên hidden width.
        self.down = nn.Linear(hidden, d_model)  # Nén lại để cộng được vào residual stream.
        self.dropout = nn.Dropout(dropout)  # Regularization, chỉ hoạt động ở train mode.

    def forward(self, x):
        # Thứ tự: expand → GELU phi tuyến → contract → dropout.
        return self.dropout(self.down(F.gelu(self.up(x))))

class SwiGLU(nn.Module):
    def __init__(self, d_model: int, hidden: int):
        super().__init__()  # Đăng ký ba linear projections.
        # gate quyết định kênh nào đi qua; up tạo nhánh giá trị song song.
        self.gate, self.up = nn.Linear(d_model, hidden), nn.Linear(d_model, hidden)
        self.down = nn.Linear(hidden, d_model, bias=False)  # Trở về residual width.

    def forward(self, x):
        # SwiGLU nhân element-wise nhánh SiLU gate với nhánh value trước khi down-project.
        return self.down(F.silu(self.gate(x)) * self.up(x))
```

### Thực hành có hướng dẫn / Guided hands-on

1. Khởi tạo tensor `(2, 16, 128)` và xác minh đầu ra giữ nguyên shape.
2. Đếm tham số GELU-MLP và chọn `hidden` cho SwiGLU để ngân sách chênh dưới 5%.
3. Chạy forward/backward với cùng seed; ghi loss, chuẩn activation và gradient.
4. Thử đầu vào biên độ `1e-3`, `1`, `1e3`; kiểm tra `isfinite`.

## Buổi 2 — Norm, residual và block / Session 2 — Norm, residual, and the block

```python
class RMSNorm(nn.Module):
    def __init__(self, dim, eps=1e-6):
        super().__init__()  # Khởi tạo Module.
        self.eps = eps  # Tránh chia cho 0 khi RMS rất nhỏ.
        self.weight = nn.Parameter(torch.ones(dim))  # Scale học được theo từng feature.

    def forward(self, x):
        # Tính inverse RMS bằng float32 để ổn định khi input là fp16/bf16.
        scale = (x.float().pow(2).mean(-1, keepdim=True) + self.eps).rsqrt()
        # Normalize, trả về dtype gốc rồi nhân scale learnable.
        return (x.float() * scale).to(x.dtype) * self.weight

class Block(nn.Module):
    def __init__(self, dim, attention, mlp):
        super().__init__()  # Đăng ký norm, attention và MLP.
        self.n1 = RMSNorm(dim)  # Pre-norm trước attention.
        self.n2 = RMSNorm(dim)  # Pre-norm trước MLP.
        self.attn, self.mlp = attention, mlp

    def forward(self, x):
        # Residual thứ nhất giữ đường truyền identity quanh attention.
        x = x + self.attn(self.n1(x))
        # Residual thứ hai giữ đường truyền identity quanh MLP.
        return x + self.mlp(self.n2(x))
```

### Thực hành / Hands-on lab

- Viết unit test cho shape, dtype, finite output và gradient của từng tham số.
- So sánh pre-norm/post-norm trên mô hình 12 block với minibatch cố định; log gradient norm theo tầng.
- Ablation: LayerNorm/RMSNorm × GELU/SwiGLU; giữ seed, dữ liệu và số bước không đổi.
- Báo cáo median step time, loss cuối, peak memory và trường hợp mất ổn định.

## Chính xác 5 câu hỏi thảo luận / Exactly 5 discussion questions

1. Vì sao FFN vẫn quan trọng khi attention đã trộn thông tin giữa token? / Why is the FFN needed after attention mixes tokens?
2. Khi nào SwiGLU đáng chi phí tham số và FLOPs? / When is SwiGLU worth its parameter and FLOP cost?
3. RMSNorm đánh đổi điều gì khi bỏ phép trừ trung bình? / What does RMSNorm trade away by omitting mean subtraction?
4. Vì sao pre-norm thường ổn định hơn ở mạng sâu? / Why is pre-norm usually more stable in deep networks?
5. Một ablation công bằng giữa hai block cần cố định biến nào? / Which variables must a fair block ablation control?

## Bài tập về nhà / Homework

Nộp `block.py`, `test_block.py` và báo cáo 2 trang. Cài GELU-MLP, SwiGLU, LayerNorm tự viết, RMSNorm và cả pre/post-norm; chạy ma trận ablation tối thiểu 4 cấu hình trong 300 bước trên cùng corpus nhỏ. Báo cáo công thức, ngân sách tham số, loss curve, gradient norm, tốc độ, bộ nhớ và kết luận có điều kiện.

## Rubric đánh giá / Assessment rubric

| Tiêu chí / Criterion | Điểm / Points |
|---|---:|
| Cài đặt đúng và ổn định số / Correct, numerically stable implementation | 30 |
| Kiểm thử shape, gradient, dtype, causality liên quan / Tests | 20 |
| Ablation công bằng, tái lập được / Fair reproducible ablation | 25 |
| Phân tích bằng bằng chứng / Evidence-based analysis | 20 |
| Trình bày song ngữ rõ ràng / Clear bilingual presentation | 5 |

## ⚠️ Hiểu lầm thường gặp / Common misconceptions

- Norm không chuẩn hoá qua batch hoặc time; nó chuẩn hoá chiều feature của từng token / Norm is not over batch or time.
- Residual không có nghĩa là hai nhánh luôn cùng độ lớn / Residual branches need not have equal magnitude.
- Tăng `d_ff` không miễn phí; chi phí MLP thường chiếm phần lớn FLOPs / Wider FFNs are not free.
- `eps` quá nhỏ trong precision thấp có thể gây NaN / Tiny epsilon can destabilize low precision.
