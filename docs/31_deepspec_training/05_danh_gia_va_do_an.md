# Bài 5 — Đánh giá và đồ án

[← Bài 4](04_huan_luyen_draft_model.md) · [Chỉ mục](index.md)

## Mục tiêu

- chạy evaluation đúng target/draft pair;
- đo Pareto quality–latency–throughput thay vì một metric;
- trình bày kết quả có thể tái lập.

## Evaluation chính thức

`scripts/eval/eval.sh` gọi `eval.py`. Cần đặt đúng `target_name_or_path` và `draft_name_or_path`. Repo cung cấp benchmark cho GSM8K, MATH-500, AIME25, HumanEval, MBPP, LiveCodeBench, MT-Bench, Alpaca và Arena-Hard-v2.

Không nhất thiết chạy mọi benchmark. Chọn bộ phù hợp workload, nhưng luôn có:

- target-only baseline;
- cùng prompts, sampling, context/output limits;
- warmup và nhiều lần đo;
- concurrency sweep;
- acceptance và end-to-end latency/throughput;
- quality/regression check.

## Đề bài cuối module

Chọn một released checkpoint hoặc checkpoint tự train. So sánh target-only với speculative decoding ở ít nhất ba mức concurrency.

### Deliverables

1. Environment và commit/model revisions.
2. Data/cache/config provenance.
3. Bảng acceptance, latency, throughput, GPU memory và quality.
4. Biểu đồ Pareto hoặc bảng trade-off.
5. Error analysis: workload nào nhanh/chậm, suffix acceptance, thinking/non-thinking mismatch.
6. Kết luận triển khai hoặc quyết định không triển khai.

## Rubric 100 điểm

| Hạng mục | Điểm |
|---|---:|
| Baseline và thiết kế benchmark | 20 |
| Provenance/config có thể tái lập | 20 |
| Đo acceptance + latency + throughput chính xác | 25 |
| Quality/regression và error analysis | 20 |
| Resource/safety/license và kết luận | 15 |

Repo lưu ý rằng so sánh với kết quả công bố chỉ có ý nghĩa khi setup training tương thích; với domain riêng hoặc target ở thinking mode, draft model có thể cần huấn luyện lại.

Nguồn: [DeepSpec README — Evaluation và Released Checkpoints](https://github.com/deepseek-ai/DeepSpec#evaluation), [DSpark paper](https://arxiv.org/abs/2607.05147).
