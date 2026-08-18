---
layout: course
title: "Week04"
permalink: /7_Frontier/kimi-k3-frontier-systems-10weeks/lessons/week04.html
---

# Tuần 4 — Stable LatentMoE và Quantile Balancing

[← Tuần 3](week03.md) · [Mục lục khoá](../INDEX.md) · [40 tuần](../../../courses/WEEK_INDEX.md) · [Lịch 20 buổi](../schedule.md) · [Tuần 5 →](week05.md)

## Mục tiêu / Objectives

- Phân biệt total width, latent width, routed/shared experts. / Explain LatentMoE structure.
- Mô tả activation explosion và expert imbalance. / Describe stability failures.
- Thực thi QB và audit expert loads. / Implement and audit QB.

## Lý thuyết / Theory

LatentMoE cho routed experts làm việc trong width 3584, còn shared path giữ full-width transformations. SiTU-GLU cap hai branches mềm, giữ near-origin behavior nhưng chặn output lớn. QB xem routing như balanced assignment và cập nhật expert thresholds bằng quantiles; threshold được freeze khi inference.

## Buổi 1 / Session 1 — Router and stability

Phân tích 896 experts, top-16, hai shared experts; viết rõ sparsity 896/16 = 56 nhưng không suy ra memory giảm 56×. Thử SwiGLU và SiTU-GLU trên input lớn.

## Buổi 2 / Session 2 — QB lab

Chạy `quantile_balancing.py`; tạo biased expert, so load variance, max/min load và token assignment changes. Kiểm tra target load nguyên và tie cases.

## Câu hỏi thảo luận / Discussion questions

1. Load balance có đảm bảo specialization không? / Does balance guarantee specialization?
2. Vì sao auxiliary-loss-free routing vẫn cần bias update? / Why still update routing bias?
3. SiTU-GLU đổi gradient ở tail ra sao? / How does it change tail gradients?
4. Freeze bias ở inference bảo toàn điều gì? / What does freezing preserve?
5. QB có thể phản ứng thế nào khi domain mixture đổi? / How may QB react to domain shift?

## Bài tập / Homework

Nộp router experiment trên ba score distributions, fairness metrics, assignment churn và discussion specialization-vs-balance. / Submit three-distribution routing analysis.

## Rubric

| Algorithm | Metrics | Edge cases | Analysis | Clarity |
|---:|---:|---:|---:|---:|
| 30 | 20 | 20 | 20 | 10 |

## ⚠️ Ngộ nhận / Misconceptions

- Chỉ expert active mới cần lưu. / Inactive weights still require residency or movement.
- Perfect balance luôn tốt nhất cho quality. / Balance is a systems constraint, not the full objective.
- Bias update chạy trên cùng batch rồi dùng ngay. / Report applies it causally to the next step.
