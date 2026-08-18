---
layout: course
title: "Week08"
permalink: /4_Training/openweight-training-pipeline-10weeks/lessons/week08.html
---

# Tuần 08 — Tối ưu ưu tiên và alignment / Preference optimization and alignment

[← Tuần 7](week07.md) · [Mục lục khoá](../INDEX.md) · [40 tuần](../../../courses/WEEK_INDEX.md) · [Lịch 20 buổi](../schedule.md) · [Tuần 9 →](week09.md)

## Mục tiêu học tập / Learning objectives

- Thiết kế preference collection và annotation protocol / design preference collection and annotation.
- Triển khai DPO từ checkpoint SFT / implement DPO from an SFT checkpoint.
- Theo dõi reward margin, KL/capability regressions và bias / track margins, drift, regressions, and bias.
- Quyết định alignment release bằng multi-objective gates / use multi-objective release gates.

## Lý thuyết sâu / Deep theory

DPO dùng log-ratio policy/reference:

$$\ell=-\log\sigma\{\beta[(\log\pi_\theta(y_w|x)-\log\pi_\theta(y_l|x))-(\log\pi_r(y_w|x)-\log\pi_r(y_l|x))]\}.$$

Preference labels phản ánh rubric và annotator population, không phải giá trị phổ quát. Phải đo agreement, position/length/style bias và severity. Alignment là multi-objective: helpfulness, correctness, harmlessness, calibration, latency và language coverage có thể xung đột.

## Buổi 1 — Preference pipeline / Session 1 — Preference pipeline

```yaml
pair_id: p0001  # ID duy nhất của preference pair để dedup và truy lỗi.
prompt_id: q0042  # Nối cả hai answers về cùng một prompt bất biến.
chosen_id: a  # Answer được preference aggregation chọn tốt hơn.
rejected_id: b  # Answer kém hơn nhưng vẫn phải hợp lệ/liên quan để có tín hiệu hữu ích.
rubric: [correctness, relevance, safety]  # Tiêu chí annotator phải áp dụng nhất quán.
annotator_votes: [a, a, tie]  # Giữ raw votes để đo agreement/uncertainty.
source_split: train  # Split cố định trước khi tạo pair để ngăn leakage sang evaluation.
```

### Hands-on / Thực hành

1. Blind/randomize A/B; cho phép tie/abstain và lý do.
2. Audit ≥100 pairs về correctness, shortcut và annotator agreement.
3. Split theo prompt lineage trước candidate generation.
4. Version dataset cùng rubric và annotator policy.

## Buổi 2 — Alignment run và gates / Session 2 — Alignment run and gates

- Train từ cùng SFT checkpoint với ít nhất hai beta, cùng token budget.
- Log chosen/rejected logps, reward margins, pair accuracy, response length.
- Evaluate blind win rate cùng factuality, safety, refusal, multilingual slices.
- Đặt gates trước: không critical safety regression; capability drop dưới ngưỡng; CI cho primary win rate vượt baseline.
- Nếu gate fail, không cherry-pick; phân tích pairs gây failure và data/rubric mismatch.

## Chính xác 5 câu hỏi thảo luận / Exactly 5 discussion questions

1. Preference data đại diện giá trị của ai? / Whose values does preference data represent?
2. Tie labels mang thông tin gì? / What information do ties provide?
3. Vì sao reward margin tăng có thể không cải thiện người dùng? / Why might rising reward margins not help users?
4. Alignment tax nên được đo trên slices nào? / On which slices should alignment tax be measured?
5. Khi nào cần dừng training vì safety regression? / When should safety regression halt training?

## Bài tập về nhà / Homework

Nộp preference dataset ≥500 pairs, rubric/agreement report, hai DPO runs, SFT-vs-DPO blind eval ≥100 prompts và gate decision. Phân tích ít nhất 20 disagreement/failure pairs và đề xuất revision cho rubric/data.

## Rubric đánh giá / Assessment rubric

| Tiêu chí / Criterion | Điểm / Points |
|---|---:|
| Annotation design/bias audit | 25 |
| Objective/training correctness | 25 |
| Multi-objective evaluation | 25 |
| Release gates và analysis | 15 |
| Reproducibility | 10 |

## ⚠️ Hiểu lầm thường gặp / Common misconceptions

- Preference win không đồng nghĩa factual truth / Preference is not factual truth.
- Refusal nhiều hơn không tự động an toàn hơn / More refusals are not automatically safer.
- Beta không có một giá trị tối ưu phổ quát / Beta is implementation/task dependent.
- Chỉ helpfulness score bỏ sót alignment tax / Evaluate capability and safety jointly.
