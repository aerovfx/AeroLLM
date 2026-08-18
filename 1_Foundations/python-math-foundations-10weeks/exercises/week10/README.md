---
layout: course
title: "Readme"
permalink: /1_Foundations/python-math-foundations-10weeks/exercises/week10/README.html
---

# Tuần 10 — Bài tập: Bản chất mạng nơ-ron + capstone mini

## Cơ bản

Cài đặt perceptron một đầu vào với ReLU; tính `z` và `relu(z)` cho vài giá trị.

- **Đạt:** Công thức perceptron và ReLU đúng.

## Nâng cao

Huấn luyện hồi quy tuyến tính PyTorch cho $y=2x-1$; báo cáo `w`, `b` hội tụ.

- **Đạt:** `w` ~ 2, `b` ~ -1, loss giảm dần, zero-grad đúng.

## Thử thách

Thêm một tầng ẩn ReLU để xấp xỉ $y=x^2$; so sánh loss với mô hình tuyến tính.

- **Đạt:** Mô hình phi tuyến đạt loss thấp hơn, giải thích vì sao.

## Rubric (100 điểm)

| Tiêu chí | Điểm |
|---|---:|
| Đúng chức năng | 35 |
| Xử lý lỗi/an toàn (zero grad, tránh NaN) | 25 |
| Chất lượng code/tài liệu | 20 |
| Phân tích/giải thích | 20 |
