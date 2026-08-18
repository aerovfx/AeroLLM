---
layout: course
title: "Readme"
permalink: /5_Applications/llm-applications-10weeks/exercises/week03/README.html
---

# Bài tập tuần 03 — Eval harness & phân tích lỗi

Liên kết: [Bài học](../../lessons/week03.md) · [Code](../../code/week03/)

## Mức 1 — Cơ bản

Viết một harness tối giản tách ba tầng: dataset, model, metric. Chạy hai model giả (ngẫu nhiên và đoán đa số) trên dataset giả và in accuracy.

## Mức 2 — Nâng cao

Thêm bootstrap confidence interval (≥1000 lần lặp, seed cố định) cho accuracy và in khoảng 95% của từng model. Giải thích khi nào chênh lệch accuracy giữa hai model "có ý nghĩa".

## Mức 3 — Thử thách

Tự định nghĩa 3 error bucket (ví dụ: thiếu ngữ cảnh, nhầm định dạng, ngoài phạm vi), gán từng mẫu sai vào bucket, và đề xuất một cải tiến cụ thể cho bucket lớn nhất kèm cách đo lại hiệu quả.

## Rubric (100 điểm)

| Tiêu chí | Điểm |
|---|---:|
| Đúng chức năng: harness tách lớp, chạy đúng, metric chính xác | 35 |
| An toàn & xử lý lỗi: xử lý nhãn thiếu, seed cố định, không rò rỉ test | 25 |
| Chất lượng code/tài liệu: cấu trúc rõ, chú thích đúng chỗ | 20 |
| Phân tích & bằng chứng: CI, so sánh baseline, error bucket có hành động | 20 |
