---
layout: course
title: "Readme"
permalink: /6_Interpretability/interpretability-10weeks/exercises/week05/README.html
---

# Bài tập Tuần 05 — Layers

## Cơ bản

Chạy `01_effective_dimensionality.py` và `02_logit_lens.py`, báo cáo số chiều hiệu quả mỗi tầng và chuỗi token dự đoán qua logit lens.

## Nâng cao

Viết một ước lượng mutual information đơn giản (binning 2D + histogram → entropy) cho hai biến có quan hệ phi tuyến, so sánh với Pearson correlation (gần 0 dù phụ thuộc mạnh).

## Thử thách

Thêm một "tầng nén" (ma trận hạng thấp) vào chuỗi tầng trong `01_effective_dimensionality.py`, dự đoán trước số chiều hiệu quả sẽ thay đổi thế nào, rồi kiểm chứng.

## Bằng chứng cần nộp

- Laminar profile + bảng.
- Script MI + so sánh correlation.
- Thí nghiệm tầng nén + dự đoán/kiểm chứng.

## Rubric (100 điểm)

| Tiêu chí | Điểm |
|---|---:|
| Đúng chức năng: PCA/logit lens đúng, profile hợp lệ | 35 |
| An toàn & xử lý lỗi: chuẩn hoá, xử lý ma trận suy biến, seed | 25 |
| Chất lượng code/tài liệu: chú thích, hàm tách bạch | 20 |
| Phân tích: đọc đúng profile, nêu giới hạn PCA/MI | 20 |
