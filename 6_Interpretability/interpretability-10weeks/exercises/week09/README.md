---
layout: course
title: "Readme"
permalink: /6_Interpretability/interpretability-10weeks/exercises/week09/README.html
---

# Bài tập Tuần 09 — Modifying MLP

## Cơ bản

Chạy `01_median_replacement.py`, báo cáo đường ripple-rate và ngưỡng nơi biến thiên bắt đầu xuất hiện.

## Nâng cao

Thay median bằng mean trong `01_median_replacement.py`, so sánh độ nhạy của hai phép thay thế. Giải thích vì sao median thường bền hơn trước outlier.

## Thử thách

Trong `02_subspace_removal.py`, dùng PCA tìm hướng mang tín hiệu ngữ nghĩa nhất, loại bỏ nó, và chứng minh tác động lớn hơn việc loại bỏ một hướng nhiễu ngẫu nhiên.

## Bằng chứng cần nộp

- Đường ripple-rate + ngưỡng.
- So sánh mean vs median.
- Thí nghiệm subspace removal + bằng chứng.

## Rubric (100 điểm)

| Tiêu chí | Điểm |
|---|---:|
| Đúng chức năng: replacement/subspace đúng, logit change đúng | 35 |
| An toàn & xử lý lỗi: xử lý median, chiếu subspace, seed | 25 |
| Chất lượng code/tài liệu: chú thích, hàm rõ | 20 |
| Phân tích: đọc hiệu ứng ngưỡng, nêu mã hoá thưa | 20 |
