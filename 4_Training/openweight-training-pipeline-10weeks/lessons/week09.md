---
layout: course
title: "Week09"
permalink: /4_Training/openweight-training-pipeline-10weeks/lessons/week09.html
---

# Tuần 09 — Đánh giá và red teaming / Evaluation and red teaming

[← Tuần 8](week08.md) · [Mục lục khoá](../INDEX.md) · [40 tuần](../../../courses/WEEK_INDEX.md) · [Lịch 20 buổi](../schedule.md) · [Tuần 10 →](week10.md)

## Mục tiêu học tập / Learning objectives

- Xây evaluation pyramid từ unit tests đến human review / build an evaluation pyramid.
- Thiết kế red-team threat model có scope và severity / design scoped, severity-aware red teaming.
- Đo uncertainty, slices và regression gates / measure uncertainty, slices, and regression gates.
- Chuyển findings thành mitigations và retests / turn findings into mitigations and retests.

## Lý thuyết sâu / Deep theory

Evaluation pyramid: deterministic unit/schema tests → task benchmarks → behavioral/safety suites → human review → monitored pilot. Risk priority có thể dùng $P\times I\times E$, nhưng severity critical phải là gate dù tần suất mẫu thấp. Red teaming tìm failure trong threat model; không chứng minh vắng mặt của mọi rủi ro.

Contamination checks cần exact/near matching với train, benchmark canaries nếu có và provenance. Multiple comparisons làm tăng false discoveries; freeze primary metrics và báo exploratory analyses riêng.

## Buổi 1 — Evaluation suite / Session 1 — Evaluation suite

```python
def gate(metrics, limits):
    failures = []  # Thu thập mọi gate thất bại thay vì dừng ở lỗi đầu tiên.
    for name, rule in limits.items():
        # rule là predicate theo metric; KeyError cố ý làm lộ metric bắt buộc bị thiếu.
        if not rule(metrics[name]):
            failures.append(name)
    # Chỉ release khi không gate nào fail; trả danh sách để giải thích quyết định.
    return {"release": not failures, "failed_gates": failures}
```

### Hands-on / Thực hành

- Freeze ≥200 prompts: capability, instruction, calibration, robustness, safety.
- Base/SFT/aligned chạy cùng decoding settings và runtime.
- Báo aggregate + language/domain/length/risk slices + bootstrap CI.
- Lưu raw prompts, outputs, scorer versions và reviewer decisions có access control.

## Buổi 2 — Red-team exercise / Session 2 — Red-team exercise

Threat model: assets (người dùng, dữ liệu, dịch vụ), actors, capabilities, entry points và misuse cases. Nhóm probes: prompt injection trong context ứng dụng, harmful content, PII memorization bằng synthetic canaries, bias, hallucinated authority, resource exhaustion. Không thu thập hoặc phát tán dữ liệu nhạy cảm thật.

### Lab / Hands-on lab

1. Pre-register 5 risk categories × ≥10 probes và pass criteria.
2. Triage finding theo severity, reproducibility, exploitability và exposure.
3. Mitigate ở data/model/prompt/tool/API layer; ghi owner/deadline.
4. Retest exact probe + neighboring variants; chạy capability regression.
5. Viết residual-risk acceptance hoặc do-not-release decision.

## Chính xác 5 câu hỏi thảo luận / Exactly 5 discussion questions

1. Red-team coverage khác safety proof như thế nào? / How does coverage differ from proof of safety?
2. Một finding hiếm nhưng critical nên ảnh hưởng release ra sao? / How should a rare critical finding affect release?
3. Vì sao retest chỉ exact prompt là chưa đủ? / Why is exact-prompt retesting insufficient?
4. LLM judge phù hợp vai trò nào trong safety evaluation? / What role can an LLM judge safely play?
5. Khi nào application mitigation tốt hơn retraining? / When is application-layer mitigation preferable?

## Bài tập về nhà / Homework

Nộp frozen eval suite ≥200, raw results ba checkpoints, slice metrics/CI, threat model, ≥50 red-team probes, triage log và mitigation/retest report. Kết luận release dựa trên gates được viết trước khi chạy.

## Rubric đánh giá / Assessment rubric

| Tiêu chí / Criterion | Điểm / Points |
|---|---:|
| Eval coverage/contamination control | 25 |
| Statistical/slice analysis | 20 |
| Threat model và probes | 25 |
| Triage/mitigation/retest | 20 |
| Release decision | 10 |

## ⚠️ Hiểu lầm thường gặp / Common misconceptions

- Không tìm thấy lỗi không chứng minh an toàn / No finding is not proof of safety.
- Average score có thể che critical slice / Averages hide critical slices.
- Prompt filter không sửa lỗi weights / Filters do not change model weights.
- Safety data cũng có thể contaminate eval / Safety evaluations can leak too.
