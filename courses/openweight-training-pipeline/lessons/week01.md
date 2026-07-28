# Tuần 1 — Vòng đời huấn luyện và capacity / Week 1 — Training lifecycle and capacity

## Mục tiêu học tập / Learning objectives

- Vẽ vòng đời từ objective đến release/monitoring. / Map the lifecycle from objective to release.
- Tính parameter, token, FLOP, storage và wall-clock budget. / Estimate compute, storage, and runtime.
- Thiết kế gates, artifacts và experiment lineage. / Design gates and lineage.
- Chọn scale thí nghiệm an toàn trước full run. / Choose a safe experimental scale.

## Lý thuyết sâu / Deep theory

Pipeline gồm: task contract → governance → ingest/clean/dedup → tokenize → shard → train → evaluate → red-team → checkpoint/package → deploy/monitor. Mỗi stage có input/output contract, checksum, owner và acceptance gate. / A pipeline is a chain of versioned contracts, not merely a training script.

Ước tính dense Transformer training thường dùng $C\approx6PT$ FLOPs với $P$ non-embedding parameters và $T$ training tokens; đây là planning approximation, không thay benchmark. Wall time $t=C/(nF_{peak}u)$ với $u$ model FLOP utilization. / Runtime depends heavily on utilization, communication, and kernels.

Tokens/step $=B_{micro}\times T_{seq}\times n_{acc}\times n_{GPU}$. Steps $=T_{budget}/\text{tokens/step}$. Checkpoint storage cần weights, optimizer, RNG/scheduler và retention multiplier. / Token accounting connects data, optimization, and cost.

## Buổi 1 — Lifecycle map và gates / Session 1 — Lifecycle and gates

Nhóm tạo DAG với gates: license approved; dedup leakage threshold; tokenizer round-trip; 100-step smoke stability; validation improvement; safety threshold; reproducible reload. Mỗi artifact có content hash và parent run ID. / Build a lifecycle DAG and explicit go/no-go gates.

```python
def plan(params_b, tokens_b, gpus, peak_tflops, mfu):
    # Quy tắc ước lượng training compute: khoảng 6 × parameters × training tokens.
    # params_b và tokens_b đều tính theo tỷ nên cần nhân 1e9 cho mỗi đại lượng.
    flops = 6 * params_b * 1e9 * tokens_b * 1e9
    # Tổng effective FLOP/s = GPU count × peak TFLOP/s × MFU; 1 TFLOP = 1e12 FLOP.
    seconds = flops / (gpus * peak_tflops * 1e12 * mfu)
    # 86400 giây/ngày; đây là estimate lý tưởng, chưa gồm failure/checkpoint/eval overhead.
    return {"flops": flops, "days": seconds / 86400}
```

## Buổi 2 — Capacity worksheet / Session 2 — Capacity worksheet

1. Chốt tokens/update và steps; thêm eval/checkpoint overhead. / Calculate updates and overhead.
2. Lập low/base/high scenarios cho MFU và failure retries. / Build three scenarios.
3. Đo một short benchmark để hiệu chỉnh estimate. / Calibrate with a short benchmark.
4. Đặt stop conditions: NaN, loss spike, data fault, budget ceiling. / Define automatic stop conditions.

Tham chiếu sizing trong [`nanoGPTsource/transformer_sizing.ipynb`](../../../nanoGPTsource/transformer_sizing.ipynb) và training loop [`train.py`](../../../nanoGPTsource/train.py). / Inspect local sizing and training artifacts.

## Câu hỏi thảo luận / Discussion questions

1. Vì sao FLOP estimate không đủ dự báo wall time? / Why do FLOPs not determine wall time?
2. Gate nào phải chặn training trước khi GPU chạy? / Which gates precede GPU use?
3. Checkpoint retention ảnh hưởng budget thế nào? / How does retention affect cost?
4. Khi nào pilot nhỏ không dự báo được run lớn? / When does a pilot fail to predict scale?
5. Lineage tối thiểu cần lưu gì? / What is minimum viable lineage?

## Bài tập về nhà / Homework

Thiết kế pipeline DAG cho model 0.1–1B, capacity sheet ba kịch bản, artifact registry schema, failure/stop matrix và memo giảm 30% chi phí. / Submit a lifecycle and capacity plan with risks and a cost-reduction scenario.

## Rubric đánh giá / Assessment rubric

| Hạng mục / Criterion | Điểm |
|---|---:|
| Lifecycle/contracts/gates | 25 |
| Compute/token/storage math | 30 |
| Assumptions/scenarios | 20 |
| Failure and lineage design | 15 |
| Communication | 10 |

## ⚠️ Ngộ nhận thường gặp / Common misconceptions

- Peak TFLOPS bằng sustained throughput. / Peak is not sustained performance.
- Chỉ checkpoint weights là resume được. / Exact resume needs optimizer/RNG state.
- Pilot loss tốt đủ phê duyệt full run. / Governance and safety gates remain.
- Tokens và examples hoán đổi được. / Example lengths vary.
