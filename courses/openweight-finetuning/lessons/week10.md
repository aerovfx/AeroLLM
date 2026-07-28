# Tuần 10 — Capstone và model card / Capstone and model card

[← Tuần 9](week09.md) · [Mục lục khoá](../INDEX.md) · [40 tuần](../../WEEK_INDEX.md) · [Lịch 20 buổi](../schedule.md)

## Mục tiêu học tập / Learning objectives

- Hoàn thiện fine-tuning artifact có thể tái lập / deliver a reproducible fine-tuning artifact.
- Chứng minh cải thiện so với base bằng eval đóng băng / demonstrate improvement over the base model.
- Viết model card, data card và risk assessment / write model/data cards and a risk assessment.
- Trình diễn deployment cùng failure/rollback plan / demo deployment with failure and rollback plans.

## Lý thuyết sâu / Deep theory

Một claim tốt có dạng: “trên population P, metric M theo protocol E, model A tốt hơn baseline B với uncertainty U và cost C.” Model card không phải quảng cáo; nó là interface về provenance, intended use, evaluation, limitations và ethical considerations. Release decision nên dùng gates cho correctness, safety, reproducibility và license, không chỉ tổng điểm.

## Buổi 1 — Project review / Session 1 — Project review

### Required artifact bundle / Gói bắt buộc

- Base model ID + immutable revision + license review.
- Dataset manifest, provenance, consent/license, dedup và split policy.
- Chat template, training config, seed, environment lock, logs và adapter.
- Base/SFT/(DPO nếu có) raw generations và frozen eval set.
- Exported artifact, checksums, benchmark và serving command.
- Model card, data card, safety report, known failures và rollback.

```yaml
claim:
  population: "Vietnamese domain-support prompts"  # Phạm vi dữ liệu mà tuyên bố áp dụng.
  metric: "blind rubric pass rate"  # Metric chính; người chấm không biết model identity.
  baseline: "pinned base revision"  # Revision bất biến để phép so sánh tái lập được.
  uncertainty: "document-bootstrap 95% CI"  # Cách ước lượng khoảng bất định.
release_gates:
  - no_license_blocker  # Model/data/artifact đều cho phép use và distribution dự kiến.
  - no_critical_safety_regression  # Không phát hành nếu safety regression nghiêm trọng.
  - clean_environment_smoke_test  # Artifact phải nạp/chạy trong môi trường sạch.
```

### Hands-on / Thực hành

Peer audit theo chuỗi: data→rendered prompt→labels→checkpoint→export→runtime output. Mỗi nhóm tái tạo smoke training và 10-prompt evaluation của nhóm khác; ghi issue severity và evidence.

## Buổi 2 — Demo, defense và retrospective / Session 2 — Demo, defense, retrospective

Demo 12 phút: problem/data (2), method (2), evaluation (3), deployment (2), limitations/safety (2), decision (1). Dùng prompt list đóng băng; trình bày ít nhất hai failure cases. Q&A phải phân biệt observed fact, inference và future hypothesis.

### Release drill / Diễn tập phát hành

1. Clean install và health check.
2. Load checksum-verified artifact; chạy golden prompts.
3. Simulate bad release; rollback về version trước.
4. Viết incident note: impact, detection, containment, prevention.
5. Chốt “release / limited pilot / do not release” có lý do.

## Chính xác 5 câu hỏi thảo luận / Exactly 5 discussion questions

1. Kết quả nào đủ để tuyên bố fine-tuning thành công? / What evidence is sufficient to claim success?
2. Model card cần ghi những negative results nào? / Which negative results belong in a model card?
3. License của base và dataset ảnh hưởng distribution ra sao? / How do model and data licenses affect distribution?
4. Khi nào limited pilot phù hợp hơn public release? / When is a limited pilot preferable?
5. Rollback test tiết lộ rủi ro nào mà offline eval không thấy? / What risks does rollback testing reveal?

## Bài tập cuối khoá / Final assignment

Nộp bundle đầy đủ, report ≤10 trang và video ≤12 phút. Baseline-vs-final trên ≥100 items, blind review ≥50 pairs, slice metrics + CI, deployment benchmark và safety probes là bắt buộc. Kết luận release phải nêu residual risks và owner cho follow-up.

## Rubric đánh giá / Assessment rubric

| Tiêu chí / Criterion | Điểm / Points |
|---|---:|
| Data/training correctness | 20 |
| Evaluation và evidence | 25 |
| Artifact/reproducibility/deployment | 20 |
| Model card, license, safety | 20 |
| Demo, defense, decision | 15 |

## ⚠️ Hiểu lầm thường gặp / Common misconceptions

- Adapter không thể phân phối độc lập mà bỏ qua base license / Adapter release still implicates licenses.
- Model card không phải README cài đặt / A model card is not merely setup instructions.
- Win rate không phản ánh mọi safety slice / Win rate does not cover all risks.
- “Không release” có thể là kết quả kỹ thuật đúng / Do-not-release can be a valid outcome.
