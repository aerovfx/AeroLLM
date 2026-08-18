---
layout: course
title: "Week02"
permalink: /5_Applications/llm-applications-10weeks/lessons/week02.html
---

# Tuần 2 — Benchmark & bộ dữ liệu đánh giá / Week 2 — Benchmarks and evaluation datasets

[Mục lục khoá](../INDEX.md) · [Lịch](../schedule.md) · [Tuần 1 ←](week01.md) · [Tuần 3 →](week03.md)

## Mục tiêu học tập / Learning objectives

- Phân biệt benchmark **kỹ thuật** (khả năng suy luận) và **phi kỹ thuật** (hữu ích, trung thực, an toàn). / Distinguish technical vs. non-technical benchmarks.
- Giải thích cơ chế chấm điểm multiple-choice: log-likelihood chuẩn hoá độ dài. / Explain length-normalized log-likelihood scoring.
- Phát biểu khái niệm contamination và shortcut learning. / Define contamination and shortcut learning.
- Tự xây một bộ benchmark nhỏ có nhãn và baseline ngẫu nhiên. / Build a small labeled benchmark with a random baseline.

## Công cụ / dữ liệu

- Python 3 chuẩn (`math`, `random`), dữ liệu MCQ giả.
- Nguồn: [`../../../docs/09_quantitative_evaluations/index.md`](../../../docs/09_quantitative_evaluations/index.md) — `aero_llm_06_hellaswag.md`, `aero_llm_13_superglue_and_other_amalgamations.md`, `aero_llm_15_non_technical_benchmarks.md`.

## Lý thuyết + ví dụ / Theory + examples

Một bài toán multiple-choice gồm ngữ cảnh $c$ và các lựa chọn $a_i$. Với mô hình tự hồi quy:

$$\log P(a_i\mid c)=\sum_{t=1}^{T_i}\log P(w_t\mid c, w_{<t}).$$

Để tránh thiên vị độ dài (đáp án dài bị phạt vô cớ), dùng điểm chuẩn hoá:

$$\mathrm{Score}(a_i)=\frac{1}{T_i}\sum_{t=1}^{T_i}\log P(w_t\mid c, w_{<t}).$$

Đáp án được chọn là $\arg\max_i \mathrm{Score}(a_i)$; accuracy là tỷ lệ chọn đúng, baseline ngẫu nhiên = $1/K$ (ví dụ 25% với 4 lựa chọn). / Length normalization prevents penalizing longer choices.

Ba khái niệm cần cảnh giác:

1. **Contamination**: dữ liệu test từng xuất hiện trong train → điểm cao giả. / Test data in train inflates scores.
2. **Shortcut learning**: mô hình học tín hiệu nông (văn phong, từ khoá) thay vì suy luận. / Models latch onto shallow cues.
3. **Overfitting leaderboard**: tối ưu để "ăn" đúng một benchmark mà mất tổng quát. / Leaderboard overfitting.

## Lab từng bước / Step-by-step lab

1. Viết bộ 8 câu MCQ giả (ngữ cảnh + 4 lựa chọn + đáp án đúng).
2. Cài hàm chấm điểm bằng log-likelihood đã chuẩn hoá; mô phỏng một "mô hình giả" gán log-prob cho từng token.
3. So sánh accuracy của mô hình giả với baseline ngẫu nhiên 25%.
4. Thử một phiên bản **không** chuẩn hoá độ dài; quan sát thiên lệch khi đáp án dài ngắn khác nhau.

## Liên kết code / Code links

- [`../code/week02/01_hellaswag_scoring.py`](../code/week02/01_hellaswag_scoring.py) — chấm điểm MCQ, chuẩn hoá độ dài, baseline.
- [`../code/week02/02_benchmark_builder.py`](../code/week02/02_benchmark_builder.py) — sinh bộ benchmark tổng hợp có nhãn.

## Câu hỏi thảo luận / Discussion questions

1. Vì sao phải chuẩn hoá log-likelihood theo độ dài đáp án? / Why length-normalize?
2. Làm sao phát hiện contamination trong thực tế? / How do you detect contamination?
3. Benchmark "an toàn" khác benchmark "khả năng" ở điểm nào về dữ liệu và cách chấm? / How do safety benchmarks differ?
4. Khi nào một benchmark đã "bão hoà" (mọi model đều gần tối đa) và nên làm gì? / What to do when a benchmark saturates?

## Bài tập / Homework

- **Cơ bản**: Tạo 5 câu MCQ và chấm bằng random + một mô hình quy tắc đơn giản; so sánh accuracy.
- **Nâng cao**: Cài chấm điểm chuẩn hoá độ dài; chứng minh bằng ví dụ đáp án dài không bị phạt vô cớ.
- **Thử thách**: Xây bộ benchmark 20 câu với 4 lựa chọn, thêm metadata (độ khó, chủ đề) và báo cáo accuracy theo từng nhóm con.

## Yêu cầu nộp / Submission

- 1 file Python chấm điểm + 1 bộ benchmark (JSON/CSV giả) + bảng kết quả theo nhóm.
- Nêu rõ baseline ngẫu nhiên và một giới hạn của bộ benchmark bạn viết.

## Rubric (100 điểm)

| Tiêu chí | Điểm |
|---|---:|
| Đúng chức năng: chấm điểm đúng, chuẩn hoá độ dài, baseline hợp lệ | 35 |
| An toàn & xử lý lỗi: xử lý đáp án rỗng/thiếu nhãn, không hardcode kết quả | 25 |
| Chất lượng code/tài liệu: benchmark có nhãn rõ, chú thích đúng chỗ | 20 |
| Phân tích & bằng chứng: so sánh baseline, bàn về contamination/shortcut | 20 |

## ⚠️ Lưu ý an toàn / Safety notes

- Benchmark bạn tự viết chỉ để học; không dùng nó để công bố so sánh mô hình thật.
- Không tải dữ liệu benchmark có bản quyền/đóng nếu chưa rõ giấy phép; dùng dữ liệu giả.
- Ghi rõ nguồn và split để tránh vô tình làm rò rỉ test vào train.
