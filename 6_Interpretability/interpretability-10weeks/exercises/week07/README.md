---
layout: course
title: "Readme"
permalink: /6_Interpretability/interpretability-10weeks/exercises/week07/README.html
---

# Bài tập Tuần 07 — Editing hidden states

## Cơ bản

Chạy `01_activation_patching_ioi.py` và `02_skip_layer.py`, báo cáo tầng bắt đầu "chuyển pha" và tầng nào gây lệch lớn nhất khi bị bỏ.

## Nâng cao

Trong `01_activation_patching_ioi.py`, vá tại các vị trí token khác nhau (chủ ngữ vs tân ngữ) và so mức ảnh hưởng lên logit difference. Giải thích vì sao vị trí "tên" nhạy hơn.

## Thử thách

Dựng heatmap vị trí × tầng cho logit difference trên mô hình giả, dùng nó để khoanh vùng "mạch IOI" (vị trí và tầng nào mang thông tin tên).

## Bằng chứng cần nộp

- Bảng logit diff theo tầng.
- So sánh vá theo vị trí token.
- Heatmap + kết luận khoanh vùng.

## Rubric (100 điểm)

| Tiêu chí | Điểm |
|---|---:|
| Đúng chức năng: patching/skip đúng, metric IOI đúng | 35 |
| An toàn & xử lý lỗi: donor/recipient tách bạch, baseline, seed | 25 |
| Chất lượng code/tài liệu: chú thích, cấu trúc rõ | 20 |
| Phân tích: xác định chuyển pha, nêu tính dư thừa | 20 |
