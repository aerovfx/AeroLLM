# Tuần 10 — Đóng gói, nộp bài và serving / Packaging, submission, and serving

[← Tuần 9](week09.md) · [Mục lục khoá](../INDEX.md) · [40 tuần](../../WEEK_INDEX.md) · [Lịch 20 buổi](../schedule.md)

## Mục tiêu học tập / Learning objectives

- Đóng gói model/adapter/tokenizer/config có manifest / package artifacts with a manifest.
- Triển khai endpoint có benchmark, health check và rollback / deploy with benchmarks and rollback.
- Hoàn thiện model/data cards và reproducibility bundle / complete model/data cards and reproduction bundle.
- Đánh giá tùy chọn DeepSpec khi workload phù hợp / evaluate optional DeepSpec for suitable workloads.

## Lý thuyết sâu / Deep theory

Release artifact phải định danh bất biến: base revision, adapter/checkpoint hash, tokenizer, template, license và tool versions. Serving SLO tách TTFT, inter-token latency, throughput, availability và quality gates. Quantization/batching/speculative decoding tối ưu các trục khác nhau và cần benchmark trên workload thật.

Speculative decoding dùng draft model đề xuất token và target model xác minh để giữ phân phối target khi thuật toán đúng. Speedup phụ thuộc acceptance rate, draft cost, verification efficiency và batch/context. DeepSpec tập trung huấn luyện draft model; không thay thế SFT/alignment. Xem [DeepSpec module](../../../docs/31_deepspec_training/index.md).

## Buổi 1 — Packaging và submission / Session 1 — Packaging and submission

```yaml
artifact_version: 1.0.0  # Semantic version của release package, không phải model revision.
base_model_revision: "immutable-commit-or-revision"  # Pin commit/revision, không dùng branch mutable.
files:
  # Mỗi artifact ghi path tương đối và hash thật để verify sau copy/upload.
  adapter: {path: adapter/, sha256: "computed-value"}
  # Tokenizer là artifact bắt buộc vì mismatch có thể làm model mất chất lượng hoặc lỗi runtime.
  tokenizer: {path: tokenizer/, sha256: "computed-value"}
evaluation: reports/eval.json  # Báo cáo gắn capability, safety và release gates với version này.
licenses: [MODEL_LICENSE, DATA_LICENSES]  # Các license phải được đóng gói/đối chiếu trước release.
```

### Submission checklist / Checklist nộp bài

- Source/config/environment lock; no secrets, absolute private paths or raw PII.
- Dataset manifest/provenance; redistribution policy rõ.
- Checkpoint/adapter + checksums; conversion commands.
- Frozen eval, raw outputs, red-team findings và release gates.
- README one-command smoke test; model card, data card, changelog.

## Buổi 2 — Serving, rollback và DeepSpec tùy chọn / Session 2 — Serving, rollback, and optional DeepSpec

### Core serving lab / Lab bắt buộc

1. Deploy local/container endpoint với readiness/liveness.
2. Golden prompts xác minh version/template; request limits và timeout.
3. Benchmark context 128/1024, concurrency 1/4: TTFT, p50/p95, tokens/s, memory.
4. Canary version mới; simulate regression và rollback theo checksum/version.
5. Viết capacity estimate từ arrival rate, output length và measured service time.

### Optional DeepSpec track / Nhánh DeepSpec tùy chọn

- Chỉ dùng checkpoint/dataset nhỏ phù hợp tài nguyên; không giả định pipeline target cache hàng chục TB.
- So sánh target-only với speculative trên cùng prompts, target model và sampling.
- Đo acceptance length/rate, end-to-end latency, throughput và memory.
- Xác minh output-distribution correctness theo implementation; không đánh đổi chất lượng âm thầm.
- Nếu draft training không khả thi, đánh giá checkpoint sẵn và viết feasibility/capacity plan.

## Chính xác 5 câu hỏi thảo luận / Exactly 5 discussion questions

1. Artifact manifest ngăn những lỗi triển khai nào? / Which deployment errors does a manifest prevent?
2. Vì sao throughput benchmark cần kèm TTFT và p95? / Why pair throughput with TTFT and p95?
3. Khi nào speculative decoding không tạo speedup? / When does speculative decoding fail to speed up inference?
4. Canary và rollback cần quan sát metric nào ngoài availability? / What metrics beyond availability matter for canaries?
5. Điều kiện nào đủ để tuyên bố pipeline tái lập? / What evidence establishes pipeline reproducibility?

## Bài tập cuối khoá / Final assignment

Nộp training-to-serving bundle: data manifest, SFT/alignment configs, logs, checkpoints, evaluation/red-team reports, cards, release manifest, endpoint và rollback demo. Benchmark ≥12 workload cells (context×concurrency×artifact). DeepSpec là bonus: báo baseline, acceptance, latency, memory, correctness và feasibility trung thực.

## Rubric đánh giá / Assessment rubric

| Tiêu chí / Criterion | Điểm / Points |
|---|---:|
| Pipeline correctness và provenance | 20 |
| Evaluation/safety/release gates | 20 |
| Packaging/reproducibility | 20 |
| Serving benchmark/reliability | 25 |
| Demo, documentation, defense | 15 |

Bonus DeepSpec tối đa 10 điểm nhưng tổng điểm chính vẫn 100; bonus chỉ nhận khi benchmark công bằng và correctness được kiểm chứng.

## ⚠️ Hiểu lầm thường gặp / Common misconceptions

- Checksum xác nhận bytes, không xác nhận chất lượng / Checksums verify bytes, not behavior.
- Container không tự động tạo reproducibility nếu base/data mutable / Containers cannot freeze mutable inputs.
- Speculative decoding không làm target model thông minh hơn / It accelerates, not improves, the target.
- Serving thành công một request không chứng minh capacity/reliability / One successful request is not production readiness.
