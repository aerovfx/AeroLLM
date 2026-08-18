---
layout: course
title: "Week03"
permalink: /5_Applications/llm-applications-10weeks/lessons/week03.html
---

# Tuần 3 — Eval harness, đối sánh baseline & phân tích lỗi / Week 3 — Eval harness, baselines and error analysis

[Mục lục khoá](../INDEX.md) · [Lịch](../schedule.md) · [Tuần 2 ←](week02.md) · [Tuần 4 →](week04.md)

## Mục tiêu học tập / Learning objectives

- Viết một eval harness tối giản: load dataset → chạy model → aggregate metric. / Write a minimal eval harness.
- Giải thích vai trò của baseline (random, đa số, heuristic) làm mốc so sánh. / Explain baselines as reference points.
- Tính khoảng tin cậy bằng bootstrap và đọc ý nghĩa thống kê. / Compute bootstrap confidence intervals.
- Lập "error bucket" để phân loại lỗi thành nhóm có thể hành động. / Build actionable error buckets.

## Công cụ / dữ liệu

- Python 3 chuẩn (`random`, `statistics`, `collections`); dataset giả có nhãn.
- Nguồn: [`../../../docs/09_quantitative_evaluations/index.md`](../../../docs/09_quantitative_evaluations/index.md) — `aero_llm_01_promises_and_challenges_of_quantitative_evaluations.md`, `aero_llm_016_black_box_evals.md`.

## Lý thuyết + ví dụ / Theory + examples

Harness tách ba tầng để dữ liệu, mô hình và metric độc lập:

```
Dataset (input, label) ──> Model (predict) ──> Metric (score)
```

Một baseline trả lời: pipeline có chạy đúng không, mô hình có học hơn thống kê đơn giản không, cải tiến có đáng chi phí không. / Baselines check pipeline correctness, learning signal, and cost-benefit.

Với accuracy ước lượng $\hat p$ trên $N$ mẫu, sai số chuẩn xấp xỉ $\sqrt{\hat p(1-\hat p)/N}$. Bootstrap tổng quát hơn: lấy mẫu lại có hoàn lại, tính metric nhiều lần, lấy phân vị 2.5% và 97.5% làm khoảng tin cậy 95%. / Bootstrap resamples with replacement to get a CI.

Phân tích lỗi: đừng chỉ báo một con số; nhóm lỗi theo nguyên nhân (thiếu ngữ cảnh, nhầm định dạng, lỗi tính toán, ngoài phạm vi) để biết sửa gì tiếp. / Group errors by cause, not just count them.

## Lab từng bước / Step-by-step lab

1. Tạo dataset 200 mẫu giả: mỗi mẫu có `input`, `label`, và `category`.
2. Cài 3 "model": random, đa số, và heuristic (quy tắc đơn giản); chạy qua cùng một harness.
3. Tính accuracy và bootstrap CI cho từng model; so sánh xem heuristic có hơn baseline đáng kể không.
4. Với model tốt nhất, lập error bucket theo `category` và liệt kê 5 mẫu lỗi tiêu biểu.

## Liên kết code / Code links

- [`../code/week03/01_eval_harness.py`](../code/week03/01_eval_harness.py) — harness + 3 model giả + aggregate.
- [`../code/week03/02_error_analysis.py`](../code/week03/02_error_analysis.py) — bootstrap CI + error buckets.

## Câu hỏi thảo luận / Discussion questions

1. Tại sao accuracy "cao hơn 2 điểm" có thể không có ý nghĩa nếu tập test nhỏ? / Why might +2 accuracy be meaningless on a small test set?
2. Baseline nào hợp lý cho một bài toán hỏi–đáp mở? / What baseline suits open-ended QA?
3. Error bucket tốt nên có đặc điểm gì? / What makes a good error bucket?
4. Khi nào nên tin một kết quả benchmark công bố? / When should you trust a published benchmark result?

## Bài tập / Homework

- **Cơ bản**: Chạy harness với random + đa số trên dataset giả; in accuracy từng model.
- **Nâng cao**: Thêm bootstrap CI (1000 lần lặp) và in khoảng 95% cho từng model.
- **Thử thách**: Tự định nghĩa 3 error buckets, gán từng mẫu sai vào bucket, và đề xuất một cải tiến cho bucket lớn nhất.

## Yêu cầu nộp / Submission

- 1 harness Python + bảng kết quả (accuracy, CI) cho ≥3 model + báo cáo phân tích lỗi.
- Nêu rõ seed và cách lấy mẫu; không cần mô hình thật.

## Rubric (100 điểm)

| Tiêu chí | Điểm |
|---|---:|
| Đúng chức năng: harness tách lớp rõ, chạy đúng, metric chính xác | 35 |
| An toàn & xử lý lỗi: xử lý nhãn thiếu, seed cố định, không rò rỉ test | 25 |
| Chất lượng code/tài liệu: cấu trúc rõ, chú thích đúng chỗ | 20 |
| Phân tích & bằng chứng: CI, so sánh baseline, error bucket có hành động | 20 |

## ⚠️ Lưu ý an toàn / Safety notes

- Giữ test set tách biệt khỏi mọi quyết định chọn model (tránh data leakage).
- Bootstrap chỉ ước lượng phương sai do lấy mẫu, không bù cho dữ liệu lệch/thiếu.
- Không dùng harness để tự động đánh giá mô hình của bên thứ ba chưa được phép.
