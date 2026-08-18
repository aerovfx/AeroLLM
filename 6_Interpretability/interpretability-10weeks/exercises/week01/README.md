---
layout: course
title: "Readme"
permalink: /6_Interpretability/interpretability-10weeks/exercises/week01/README.html
---

# Bài tập Tuần 01 — Nhập môn interpretability

## Cơ bản

Chạy hai script trong `code/week01/`, chép lại output và giải thích ý nghĩa từng con số (drift, R², hệ số w). Viết 3–5 câu định nghĩa "residual stream" và "observational vs causal".

## Nâng cao

Đổi `SEED`, `N_BLOCKS`, `DIM` trong `01_residual_stream.py`, chạy lại 3 lần và nhận xét drift thay đổi thế nào. Giải thích vì sao seed cố định quan trọng với tái lập.

## Thử thách

Tự viết một linear probe (hồi quy logistic thuần NumPy, dùng gradient descent) phân loại hai cụm vector giả 2D; thử với 20 mẫu và 200 mẫu, so sánh độ tin cậy (accuracy trên tập tách riêng).

## Bằng chứng cần nộp

- Output đã chạy + giải thích.
- Bảng thí nghiệm đổi tham số.
- Script probe tự viết + kết quả.

## Rubric (100 điểm)

| Tiêu chí | Điểm |
|---|---:|
| Đúng chức năng: script chạy, số liệu đúng, probe phân loại được | 35 |
| An toàn & xử lý lỗi: seed tái lập, tách train/test, không tải model thật | 25 |
| Chất lượng code/tài liệu: chú thích Việt, đặt tên rõ | 20 |
| Phân tích: diễn giải số liệu, nêu giới hạn, bằng chứng chạy | 20 |
