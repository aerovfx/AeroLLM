# Tuần 3 — Embedding và batching / Week 3 — Embeddings and batching

[← Tuần 2](week02.md) · [Mục lục khoá](../INDEX.md) · [40 tuần](../../WEEK_INDEX.md) · [Lịch 20 buổi](../schedule.md) · [Tuần 4 →](week04.md)

## Mục tiêu học tập / Learning objectives

- Suy luận shape của token/position embedding và logits. / Derive token, positional embedding, and logit shapes.
- Tạo input–target windows cho next-token prediction. / Construct shifted input-target windows.
- Hiểu batch, block size, padding/masking và gradient variance. / Understand batching, context length, padding, masking, and gradient variance.
- Kiểm thử data loader trước khi train. / Test a loader before training.

## Lý thuyết sâu / Deep theory

Với batch token $X\in\mathbb N^{B\times T}$, bảng embedding $E\in\mathbb R^{V\times d}$ trả $E[X]\in\mathbb R^{B\times T\times d}$. Learned position embedding $P\in\mathbb R^{T_{max}\times d}$ được cộng: $H_0=E[X]+P_{0:T}$. / Embedding lookup produces dense token states; positional information breaks permutation invariance.

Target là dịch trái một bước: $X=(x_i,\ldots,x_{i+T-1})$, $Y=(x_{i+1},\ldots,x_{i+T})$. Cross-entropy thường flatten logits $[B,T,V]$ thành $[BT,V]$. Nếu label không shift, mô hình chỉ học copy. / Targets must be shifted by one; unshifted labels create a trivial copying objective.

Batch lớn giảm variance gradient nhưng tăng memory và có thể cần learning-rate adjustment. Gradient accumulation tạo effective batch $B_{eff}=B_{micro}\times n_{acc}\times n_{devices}$ (theo sequence; nhân $T$ để ra tokens/update). Padding cần loss mask; packed fixed-length streams tránh padding nhưng phải cân nhắc document boundaries. / Effective batch and token accounting must be explicit.

## Buổi 1 — Shapes và lookup / Session 1 — Shapes and lookup

1. Theo dõi shape từ IDs đến logits; tính parameter count $Vd+T_{max}d$. / Trace shapes and parameter counts.
2. So sánh learned positions với sinusoidal encoding. / Compare learned and sinusoidal positions.
3. Kiểm tra cùng token ở hai vị trí có token vector giống nhưng tổng vector khác. / Verify token lookup versus position addition.

```python
import torch  # Tensor và các lớp neural-network của PyTorch.

# B=batch size, T=sequence length, V=vocab size, d=embedding dimension.
B, T, V, d = 4, 8, 128, 32
# Tạo batch token ID giả lập, shape (B, T), mỗi ID nằm trong [0, V).
x = torch.randint(V, (B, T))
# Bảng token embedding ánh xạ V token; position embedding ánh xạ T vị trí sang vector d.
tok = torch.nn.Embedding(V, d)
pos = torch.nn.Embedding(T, d)
# [None, :, :] thêm chiều batch để position vectors broadcast qua mọi sample.
h = tok(x) + pos(torch.arange(T))[None, :, :]
# Mỗi token ở mỗi sample giờ được biểu diễn bởi một vector d chiều.
assert h.shape == (B, T, d)
```

## Buổi 2 — Data loader đúng và tái lập / Session 2 — Correct, reproducible loader

Đối chiếu `get_batch` trong [`nanoGPTsource/train.py`](../../../nanoGPTsource/train.py). / Compare against the local implementation.

```python
def get_batch(data, batch_size, block_size, generator=None):
    # Chọn ngẫu nhiên vị trí bắt đầu; trừ block_size để không vượt cuối tensor.
    ix = torch.randint(len(data)-block_size, (batch_size,), generator=generator)
    # x chứa block_size token đầu vào tại từng vị trí đã chọn.
    x = torch.stack([data[i:i+block_size] for i in ix])
    # y dịch sang phải một token, nên y[t] là mục tiêu kế tiếp của x[t].
    y = torch.stack([data[i+1:i+1+block_size] for i in ix])
    # Cả hai có shape (batch_size, block_size).
    return x, y
```

Hands-on: dùng chuỗi tăng dần để assert `y[:, :-1] == x[:, 1:]`; kiểm tra min/max ID; seed generator; đo tokens/s; thử microbatch gây OOM giả lập và gradient accumulation. / Use a monotonic sequence to test shifts, bounds, determinism, throughput, and effective batching.

## Câu hỏi thảo luận / Discussion questions

1. Vì sao embedding lookup tương đương chọn một hàng của ma trận? / Why is lookup a row selection?
2. Khi nào padding tốt hơn concatenation? / When is padding preferable to concatenation?
3. Block size tăng ảnh hưởng memory và số sample thế nào? / How does context length affect memory and sampling?
4. Gradient accumulation giống và khác batch lớn thật ở đâu? / How does accumulation differ from a true large batch?
5. Có nên cho window vượt qua ranh giới tài liệu? / Should windows cross document boundaries?

## Bài tập về nhà / Homework

Xây loader fixed-window hỗ trợ seed, train/validation, device transfer và ít nhất 6 unit tests; báo cáo tokens/update, memory ước tính, throughput cho ba $(B,T)$ và một quyết định cấu hình. / Build and benchmark a tested fixed-window loader across three batch/context settings.

## Rubric đánh giá / Assessment rubric

| Hạng mục / Criterion | Điểm |
|---|---:|
| Shift, shapes, bounds đúng / correctness | 30 |
| Determinism và tests | 25 |
| Benchmark có kiểm soát / controlled benchmark | 20 |
| Giải thích batch/memory / reasoning | 15 |
| Chất lượng mã / code quality | 10 |

## ⚠️ Ngộ nhận thường gặp / Common misconceptions

- Embedding là one-hot được lưu tường minh; thực tế lookup tránh ma trận sparse. / Lookup avoids explicit one-hot vectors.
- Tăng batch luôn tăng chất lượng. / Larger batches are not always better.
- PAD có thể tính loss như token thường. / Padding must be masked.
- Seed duy nhất đảm bảo tái lập tuyệt đối trên mọi GPU. / Hardware kernels can still be nondeterministic.
