---
layout: course
title: "Readme"
permalink: /6_Interpretability/interpretability-10weeks/exercises/week02/README.html
---

# Bài tập Tuần 02 — Identifying circuits

## Cơ bản

Chạy `01_sparse_probe.py` và `02_sae_toy.py`, ghi lại: neuron/feature "sống sót", accuracy, cosine similarity. Giải thích phạt L1 ép hệ số về 0 như thế nào.

## Nâng cao

Trong `01_sparse_probe.py`, quét 5 giá trị `lam` (ví dụ 0.01, 0.1, 0.3, 0.6, 1.5), lập bảng accuracy vs số neuron sống, tìm điểm gãy và giải thích.

## Thử thách

Cấy 2 feature tương quan (không trực giao) vào dữ liệu của sparse probe hoặc SAE. Quan sát xem công cụ có tách được chúng không; giải thích hiện tượng (gợi ý: statistical suppression, feature superposition).

## Bằng chứng cần nộp

- Bảng mạch + accuracy.
- Đường quét λ (bảng hoặc đồ thị).
- Thí nghiệm feature tương quan + nhận xét.

## Rubric (100 điểm)

| Tiêu chí | Điểm |
|---|---:|
| Đúng chức năng: probe/SAE chạy, tìm đúng feature cấy | 35 |
| An toàn & xử lý lỗi: seed, xử lý hội tụ, không overfit dữ liệu nhỏ | 25 |
| Chất lượng code/tài liệu: chú thích, cấu trúc rõ | 20 |
| Phân tích: đọc đúng độ thưa, nêu statistical suppression | 20 |
