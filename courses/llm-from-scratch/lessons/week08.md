# Tuần 08 — Huấn luyện, optimizer và checkpoint / Training, optimization, and checkpoints

[← Tuần 7](week07.md) · [Mục lục khoá](../INDEX.md) · [40 tuần](../../WEEK_INDEX.md) · [Lịch 20 buổi](../schedule.md) · [Tuần 9 →](week09.md)

## Mục tiêu học tập / Learning objectives

- Xây training loop đúng với accumulation, clipping và mixed precision / build a correct loop with accumulation, clipping, and mixed precision.
- Giải thích AdamW, warmup và cosine decay / explain AdamW, warmup, and cosine decay.
- Lưu/khôi phục trạng thái để resume tái lập / save and restore state for reproducible resume.
- Chẩn đoán divergence bằng loss, gradient norm và throughput / diagnose divergence from metrics.

## Lý thuyết sâu / Deep theory

Adam cập nhật $m_t=\beta_1m_{t-1}+(1-\beta_1)g_t$, $v_t=\beta_2v_{t-1}+(1-\beta_2)g_t^2$, hiệu chỉnh bias rồi $\theta\leftarrow\theta-\eta\hat m/(\sqrt{\hat v}+\epsilon)$. AdamW tách weight decay: $\theta\leftarrow(1-\eta\lambda)\theta-\eta\hat m/(\sqrt{\hat v}+\epsilon)$. Bias và norm scale thường không decay.

Effective batch tokens = `micro_batch × sequence_length × accumulation × world_size`. Warmup tuyến tính tránh update quá lớn khi moments chưa ổn định; cosine schedule: $\eta=\eta_{min}+\frac12(\eta_{max}-\eta_{min})(1+\cos(\pi q))$.

## Buổi 1 — Training loop đáng tin / Session 1 — A trustworthy training loop

```python
def lr_at(step, warmup, total, peak, floor):
    # Warmup tuyến tính từ LR nhỏ lên peak để tránh update lớn khi model chưa ổn định.
    if step < warmup:
        return peak * (step + 1) / warmup
    # q là tiến độ decay trong [0,1]; max(1, ...) tránh chia cho 0.
    q = min(1.0, (step-warmup) / max(1, total-warmup))
    # Cosine decay giảm mượt từ peak xuống floor.
    return floor + 0.5*(peak-floor)*(1+__import__('math').cos(__import__('math').pi*q))

# Xoá gradient cũ; set_to_none tiết kiệm memory và giúp phát hiện param không có gradient.
optimizer.zero_grad(set_to_none=True)
# Gradient accumulation mô phỏng batch lớn bằng nhiều micro-batch.
for micro in range(accum_steps):
    x, y = next_batch()  # Lấy input và next-token targets.
    # Autocast dùng bfloat16 cho phép tính phù hợp, giảm VRAM/tăng tốc trên GPU hỗ trợ.
    with torch.autocast(device_type="cuda", dtype=torch.bfloat16):
        _, loss = model(x, y)  # Forward và cross-entropy của micro-batch.
        loss = loss / accum_steps  # Scale để tổng gradient bằng trung bình batch lớn.
    loss.backward()  # Cộng gradient vào .grad qua từng micro-batch.
# Giới hạn global gradient norm để giảm nguy cơ exploding gradients.
torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
optimizer.step()  # AdamW cập nhật tham số đúng một lần cho effective batch.
```

### Thực hành / Hands-on

- Nhóm tham số decay/no-decay; in tên từng nhóm để audit.
- So sánh update một batch lớn với accumulation tương đương khi dropout tắt.
- Log train/validation loss, LR, grad norm, tokens/s, memory và wall time.
- Tạo một failure có chủ ý bằng LR lớn, sau đó xác định tín hiệu báo trước NaN.

## Buổi 2 — Checkpoint và khả năng tái lập / Session 2 — Checkpointing and reproducibility

Checkpoint đầy đủ gồm model, optimizer, scheduler/step, scaler nếu FP16, RNG của Python/NumPy/Torch/CUDA, config, tokenizer identity và data cursor. Ghi atomically qua file tạm rồi rename; giữ `latest` và `best` riêng.

```python
state = {
 # Weights/buffers của model; đủ để khôi phục forward state.
 "model": model.state_dict(),
 # Momentum/variance của optimizer; bắt buộc để resume training đúng nghĩa.
 "optimizer": optimizer.state_dict(),
 "step": step,  # Global step dùng để tiếp tục scheduler/logging.
 "config": vars(cfg),  # Snapshot cấu hình giúp tái tạo đúng kiến trúc.
 "torch_rng": torch.get_rng_state(),  # RNG CPU cho khả năng tái lập.
 # RNG của từng CUDA device; None nếu đang chạy CPU/MPS.
 "cuda_rng": torch.cuda.get_rng_state_all() if torch.cuda.is_available() else None,
}
# Ghi file tạm trước để tránh checkpoint chính bị hỏng nếu process dừng giữa lúc ghi.
torch.save(state, "checkpoint.tmp")
import os  # os.replace cung cấp atomic replace trên cùng filesystem.
os.replace("checkpoint.tmp", "checkpoint.pt")  # Công bố checkpoint hoàn chỉnh.
```

### Lab / Hands-on lab

1. Train 100 steps liên tục; lưu hash tham số và loss steps 51–100.
2. Chạy lại 50 steps, checkpoint, khởi động process mới và resume đến 100.
3. So sánh exact/near-exact tùy kernel; giải thích nếu khác.
4. Làm hỏng config/tokenizer cố ý và thêm guard để từ chối resume không tương thích.

## Chính xác 5 câu hỏi thảo luận / Exactly 5 discussion questions

1. Vì sao AdamW không tương đương L2 regularization trong Adam? / Why is AdamW not equivalent to L2 regularization in Adam?
2. Accumulation thay đổi noise scale ra sao? / How does accumulation change gradient noise scale?
3. Khi nào gradient clipping che giấu lỗi thay vì sửa lỗi? / When does clipping hide rather than fix a bug?
4. Checkpoint tối thiểu nào đủ cho inference nhưng không đủ resume? / What checkpoint suffices for inference but not resume?
5. Metric nào phân biệt data bottleneck với compute bottleneck? / Which metrics distinguish data from compute bottlenecks?

## Bài tập về nhà / Homework

Train GPT tối thiểu 2.000 optimizer steps trên corpus nhỏ. Nộp config, logs CSV, biểu đồ, checkpoint best/latest, script resume và kiểm chứng continuous-vs-resumed. Thực hiện hai ablation (LR peak và weight decay), giữ token budget cố định, rồi khuyến nghị cấu hình bằng validation loss và chi phí.

## Rubric đánh giá / Assessment rubric

| Tiêu chí / Criterion | Điểm / Points |
|---|---:|
| Training loop và optimizer đúng / Correct loop and optimizer | 30 |
| Checkpoint/resume đầy đủ / Complete checkpoint and resume | 25 |
| Logging, chẩn đoán, reproducibility / Logging and diagnostics | 20 |
| Ablation có kiểm soát / Controlled ablation | 20 |
| Tài liệu / Documentation | 5 |

## ⚠️ Hiểu lầm thường gặp / Common misconceptions

- Chia loss cho accumulation là bắt buộc để giữ gradient scale / Scale loss during accumulation.
- `model.state_dict()` không đủ để resume optimizer / Model weights alone do not resume training.
- Validation phải ở `eval()` và không gradient / Validation needs eval and no-grad.
- BF16 thường không cần GradScaler; FP16 thường cần / BF16 usually does not need loss scaling.
