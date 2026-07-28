# Tuần 07 — Huấn luyện phân tán và observability / Distributed training and observability

[← Tuần 6](week06.md) · [Mục lục khoá](../INDEX.md) · [40 tuần](../../WEEK_INDEX.md) · [Lịch 20 buổi](../schedule.md) · [Tuần 8 →](week08.md)

## Mục tiêu học tập / Learning objectives

- Giải thích data parallel, FSDP/ZeRO và sharding trade-offs / explain parallelism and sharding trade-offs.
- Tính global token batch và scaling efficiency / compute global token batch and scaling efficiency.
- Thiết lập metrics/logging đủ để debug distributed jobs / instrument distributed jobs for debugging.
- Khôi phục checkpoint an toàn khi worker/node lỗi / recover safely from worker or node failure.

## Lý thuyết sâu / Deep theory

Data parallel sao chép model và all-reduce gradients. ZeRO/FSDP shard optimizer states, gradients và/hoặc parameters để giảm memory mỗi rank, đổi lại communication và complexity. Global tokens/update = $b\times T\times a\times w$; throughput = processed non-padding tokens / wall time.

Scaling efficiency từ 1 lên $n$ devices: $E_n=\text{throughput}_n/(n\,\text{throughput}_1)$. Không kỳ vọng 100% do communication, input pipeline và imbalance. Observability phải phân biệt rank-local và globally reduced metrics.

## Buổi 1 — Distributed execution / Session 1 — Distributed execution

```python
import torch  # Tạo tensor metric trên đúng device của process.
import torch.distributed as dist  # Collective communication giữa workers.

def global_mean(value, device):
    # Mỗi rank đóng gói local scalar bằng float64 để giảm sai số cộng dồn.
    x = torch.tensor([value], dtype=torch.float64, device=device)
    # SUM là in-place collective: sau lệnh này mọi rank nhận tổng global.
    dist.all_reduce(x, op=dist.ReduceOp.SUM)
    # Chia world size để lấy mean giữa ranks rồi đổi tensor 1 phần tử thành Python float.
    return (x / dist.get_world_size()).item()
```

### Hands-on / Thực hành

1. Chạy 1 GPU/rank baseline, sau đó 2+ ranks với global token batch giữ cố định.
2. Kiểm tra DistributedSampler seed/epoch; không để ranks đọc cùng batch.
3. So sánh DDP với sharding về VRAM, tokens/s và checkpoint size/time.
4. Audit gradient accumulation/no_sync để tránh all-reduce mọi micro-step.

## Buổi 2 — Observability và fault recovery / Session 2 — Observability and recovery

Metric tối thiểu: train/eval loss, LR, grad norm, update norm, tokens/s, data wait, step time, GPU utilization/memory, communication time, skipped/NaN steps và checkpoint duration. Log config, git SHA, container/environment, dataset manifest hash và topology.

### Failure injection lab / Lab tiêm lỗi

- Tạo data stall và nhận biết qua low utilization + high data wait.
- Tạo một NaN batch; dump IDs an toàn, skip/stop theo policy, không tiếp tục im lặng.
- Dừng một run sau checkpoint rồi resume với cùng data cursor.
- So sánh final weights/loss với continuous run trong tolerance đã định.
- Tạo dashboard có alert cho loss spike, no progress và disk capacity.

## Chính xác 5 câu hỏi thảo luận / Exactly 5 discussion questions

1. Khi nào sharding giảm memory nhưng làm job chậm hơn? / When can sharding save memory but slow training?
2. Vì sao global loss không nên lấy riêng rank 0? / Why is rank-0 loss not necessarily global loss?
3. Tín hiệu nào nhận diện input bottleneck? / Which signals identify an input bottleneck?
4. Resume distributed cần lưu trạng thái nào ngoài weights? / What state beyond weights is required to resume?
5. Strong scaling và weak scaling trả lời câu hỏi khác nhau thế nào? / How do strong and weak scaling differ?

## Bài tập về nhà / Homework

Benchmark 1 và ≥2 devices/ranks trên cùng workload; nộp throughput, efficiency, VRAM, step breakdown. Thực hiện ba failure injections (data stall, NaN, interruption), chứng minh alert/recovery và viết runbook xử lý incident.

## Rubric đánh giá / Assessment rubric

| Tiêu chí / Criterion | Điểm / Points |
|---|---:|
| Distributed correctness | 25 |
| Benchmark/scaling analysis | 20 |
| Observability coverage | 25 |
| Recovery/failure injection | 20 |
| Runbook/reproducibility | 10 |

## ⚠️ Hiểu lầm thường gặp / Common misconceptions

- Nhiều GPU không tự động nhanh tuyến tính / More GPUs do not imply linear speedup.
- Local batch không phải global batch / Local and global batches differ.
- Loss của rank 0 có thể lệch do data slice / Rank-0 loss may be unrepresentative.
- Checkpoint sharded cần đúng world-size/load procedure / Sharded checkpoints require a defined load path.
