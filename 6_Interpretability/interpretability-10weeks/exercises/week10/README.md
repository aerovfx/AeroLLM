---
layout: course
title: "Readme"
permalink: /6_Interpretability/interpretability-10weeks/exercises/week10/README.html
---

# Bài tập Tuần 10 — Token embeddings II: trajectories + capstone

## Cơ bản

Chạy `01_trajectory_pca.py` và `02_path_length.py`, mô tả quỹ đạo 2D và path length của từng loại token.

## Nâng cao

Thêm một token "lạ" mới vào `01_trajectory_pca.py`, dự đoán trước quỹ đạo của nó (tách gần/xa cụm đúng), rồi kiểm chứng và giải thích.

## Thử thách

Viết báo cáo capstone 1–2 trang kết hợp một phép quan sát (tuần 1–5) và một phép can thiệp (tuần 6–9) trên cùng một mô hình giả. Cấu trúc: giả thuyết → quan sát → can thiệp → bằng chứng → giới hạn.

## Bằng chứng cần nộp

- Quỹ đạo + bảng path length.
- Thí nghiệm token mới + dự đoán/kiểm chứng.
- Bản nháp capstone (liên kết đồ án cuối khoá).

## Rubric (100 điểm)

| Tiêu chí | Điểm |
|---|---:|
| Đúng chức năng: PCA common-space đúng, path length đúng | 35 |
| An toàn & xử lý lỗi: chuẩn hoá, xử lý ma trận suy biến, seed | 25 |
| Chất lượng code/tài liệu: chú thích, cấu trúc rõ | 20 |
| Phân tích: đọc quỹ đạo, nêu variance≠relevance, tổng hợp capstone | 20 |
