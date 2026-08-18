---
layout: course
title: "Readme"
permalink: /6_Interpretability/interpretability-10weeks/exercises/week08/README.html
---

# Bài tập Tuần 08 — Interfering with attention

## Cơ bản

Chạy `01_head_ablation.py` và `02_head_patching_ioi.py`, liệt kê head nhạy nhất và vai trò phỏng đoán (mang tín hiệu gì).

## Nâng cao

Thay zero-out bằng mean-ablation (trừ trung bình đầu ra head) trong `01_head_ablation.py`, so sánh kết quả với zero-out. Giải thích khác biệt.

## Thử thách

Dùng head patching để vẽ sơ đồ "head nào chuyển thông tin từ token nào" trong một câu IOI giả (mở rộng `02_head_patching_ioi.py` cho nhiều vị trí token).

## Bằng chứng cần nộp

- Bảng head + logit diff (ablation lẫn patching).
- So sánh mean-ablation vs zero-out.
- Sơ đồ mạch phỏng đoán.

## Rubric (100 điểm)

| Tiêu chí | Điểm |
|---|---:|
| Đúng chức năng: tách head đúng, logit difference đúng | 35 |
| An toàn & xử lý lỗi: reshape head đúng shape, baseline, seed | 25 |
| Chất lượng code/tài liệu: chú thích, hàm rõ | 20 |
| Phân tích: đọc mạch phân tán, nêu tính dư thừa | 20 |
