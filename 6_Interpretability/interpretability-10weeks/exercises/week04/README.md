---
layout: course
title: "Readme"
permalink: /6_Interpretability/interpretability-10weeks/exercises/week04/README.html
---

# Bài tập Tuần 04 — Neurons và dimensions

## Cơ bản

Chạy `01_activation_maximization.py` và `02_neuron_selectivity.py`. Báo cáo: đặc trưng neuron tìm được (cosine similarity), accuracy logistic, t và p-value của t-test.

## Nâng cao

Trong `02_neuron_selectivity.py`, thêm nhiễu tăng dần vào nhóm A và B (giảm tỉ lệ tín hiệu/nhiễu), quan sát accuracy và p-value mất ý nghĩa khi nào. Giải thích sự khác biệt giữa "không phân tách được" và "khác biệt không có ý nghĩa thống kê".

## Thử thách

Viết "data sampling" đơn giản: quét 1000 vector giả ngẫu nhiên, lấy top-k theo kích hoạt của neuron mục tiêu, so sánh kết quả với gradient ascent (đặc trưng tìm được có khớp không).

## Bằng chứng cần nộp

- Bảng neuron + đặc trưng + hai phép thử.
- Thí nghiệm nhiễu + nhận xét.
- Script data sampling + so sánh.

## Rubric (100 điểm)

| Tiêu chí | Điểm |
|---|---:|
| Đúng chức năng: tối ưu hội tụ, hai phép thử tính đúng | 35 |
| An toàn & xử lý lỗi: learning rate ổn định, seed, xử lý p-value | 25 |
| Chất lượng code/tài liệu: chú thích, cấu trúc hàm rõ | 20 |
| Phân tích: đối chiếu hai công cụ, nêu giới hạn multi-token | 20 |
