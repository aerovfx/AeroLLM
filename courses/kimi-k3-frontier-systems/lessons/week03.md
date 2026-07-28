# Tuần 3 — Attention Residuals / Selective depth mixing

[← Tuần 2](week02.md) · [Mục lục khoá](../INDEX.md) · [40 tuần](../../WEEK_INDEX.md) · [Lịch 20 buổi](../schedule.md) · [Tuần 4 →](week04.md)

## Mục tiêu / Objectives

- Xem network depth như một trục attention. / Treat depth as an attention axis.
- Cài Full AttnRes toy và phân tích Block AttnRes. / Implement and analyze AttnRes.
- Thiết kế ablation residual sum vs learned depth selection. / Design an ablation.

## Lý thuyết / Theory

AttnRes dùng layer-specific pseudo-query, RMS-normalized keys và layer outputs làm values. Full form truy xuất mọi output trước; block form sum nội bộ rồi attention qua block representations để hạ memory/communication từ \(O(Ld)\) xuống \(O(Nd)\). Đây là thay đổi đường truyền thông tin, không đơn thuần là skip connection dài hơn.

## Buổi 1 / Session 1 — Full và block forms

Vẽ dataflow cho embedding + sáu layers. Tính số state cần giữ ở full và block size 2/3; xác định partial final block.

## Buổi 2 / Session 2 — Depth mixer lab

Chạy `toy_attnres.py`; tạo synthetic task cần truy xuất early feature. So residual sum, uniform average và learned pseudo-query; báo loss, memory proxy và learned weights.

## Câu hỏi thảo luận / Discussion questions

1. Residual sum tạo bottleneck nào? / What bottleneck does residual accumulation create?
2. RMSNorm trên keys ngăn failure mode gì? / What failure does key normalization reduce?
3. Block size tác động accuracy và memory ra sao? / How does block size trade accuracy for memory?
4. Attention weight có phải causal explanation không? / Are weights causal explanations?
5. Feature đầu mạng có thể hữu ích ở output vì sao? / Why can early features matter late?

## Bài tập / Homework

Nộp ablation trên synthetic task với ≥3 baselines, seed cố định, plot weights và giới hạn diễn giải. / Submit a reproducible ablation and limitations.

## Rubric

| Implementation | Experimental control | Results | Interpretation | Reproducibility |
|---:|---:|---:|---:|---:|
| 25 | 25 | 20 | 20 | 10 |

## ⚠️ Ngộ nhận / Misconceptions

- Weight lớn chứng minh source là nguyên nhân duy nhất. / Attention weight is not causal proof.
- Block AttnRes miễn phí. / It adds computation and state management.
- Kết quả toy dự đoán trực tiếp model 93 layers. / Scaling can change behavior.
