# Tuần 7 — SFT, RL, reasoning effort và distillation

[← Tuần 6](week06.md) · [Mục lục khoá](../INDEX.md) · [40 tuần](../../WEEK_INDEX.md) · [Lịch 20 buổi](../schedule.md) · [Tuần 8 →](week08.md)

## Mục tiêu / Objectives

- Mô tả SFT → domain/effort RL → MOPD. / Explain the post-training sequence.
- Phân tích partial rollout, staleness và per-problem budgets. / Analyze long-horizon RL.
- Thiết kế experiment plan thay vì giả vờ reproduce RL frontier. / Build a feasible simulation.

## Lý thuyết / Theory

SFT tạo cold-start tool/reasoning policy và dùng XTML. RL tạo chín policies từ 3 domains × 3 effort levels. Partial rollouts giảm straggler waiting nhưng đưa stale trajectories qua nhiều iterations. Budget threshold \(\tau b_0(x)\) điều khiển thinking/tool tokens; MOPD hợp nhất teachers bằng clipped per-token log-ratio reward.

## Buổi 1 / Session 1 — Policy matrix

Lập ma trận domain × effort, định nghĩa reward/verifier, baseline budget, overshoot penalty và cross-domain validation. Chỉ ra data nào cần human review.

## Buổi 2 / Session 2 — Simulator

Mô phỏng 100 trajectories với random duration/quality; so synchronous wait-all và partial rollout. Đo idle time proxy, staleness, completion và budget violations.

## Câu hỏi thảo luận / Discussion questions

1. Vì sao SFT chưa đủ cho long-horizon execution? / Why is SFT insufficient?
2. Partial rollout đổi data distribution ra sao? / How does it change sampled data?
3. Per-token regularization cần vì sao? / Why regularize stale trajectories?
4. Budget penalty có thể làm underthinking không? / Can budget control cause underthinking?
5. Distillation hợp nhất experts có thể mất gì? / What may consolidation lose?

## Bài tập / Homework

Nộp simulator, 3×3 policy matrix, plots latency/staleness và risk register reward hacking. / Submit simulator and post-training plan.

## Rubric

| Simulation | Metrics | Policy design | Risks | Explanation |
|---:|---:|---:|---:|---:|
| 25 | 20 | 25 | 20 | 10 |

## ⚠️ Ngộ nhận / Misconceptions

- Nhiều reasoning tokens luôn tốt hơn. / Effort has quality–cost trade-offs.
- Distillation chỉ là SFT trên teacher outputs. / K3 describes on-policy dense reward.
- Resume rollout không gây off-policy risk. / Policy changes create staleness.
