---
layout: course
title: "Readme"
permalink: /5_Applications/llm-applications-10weeks/exercises/week01/README.html
---

# Bài tập tuần 01 — Metric cơ bản và bẫy

Liên kết: [Bài học](../../lessons/week01.md) · [Code](../../code/week01/)

## Mức 1 — Cơ bản

Viết hàm tính accuracy, precision, recall, F1 từ một confusion matrix (TP/TN/FP/FN). Tạo một tập nhãn giả lệch (90% nhãn 0) và so sánh accuracy của "đoán toàn 0" với F1. Giải thích vì sao accuracy một mình gây hiểu lầm.

## Mức 2 — Nâng cao

Cài softmax ổn định (trừ max trước khi exp) và hàm tính perplexity. Viết test xác nhận: (1) tổng phân phối softmax = 1; (2) perplexity hữu hạn khi có token chưa từng thấy; (3) model gán xác suất đúng cao có perplexity thấp hơn model phân vân.

## Mức 3 — Thử thách

Viết một "evaluation contract" hoàn chỉnh cho một bài toán đánh giá chatbot: dữ liệu (nguồn, kích thước, split), seed, metric chính/phụ, đơn vị token, giới hạn và điều kiện so sánh công bằng. Kèm một đoạn code nhỏ minh hoạ cách kiểm tra rằng split không bị rò rỉ (train/test không trùng).

## Rubric (100 điểm)

| Tiêu chí | Điểm |
|---|---:|
| Đúng chức năng: công thức metric/softmax/perplexity chính xác, xử lý biên | 35 |
| An toàn & xử lý lỗi: tránh chia 0, validate đầu vào, không log secret | 25 |
| Chất lượng code/tài liệu: chú thích đúng chỗ, dễ đọc | 20 |
| Phân tích & bằng chứng: baseline, ví dụ minh hoạ bẫy, contract đầy đủ | 20 |
