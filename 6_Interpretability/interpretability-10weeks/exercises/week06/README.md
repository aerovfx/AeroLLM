---
layout: course
title: "Readme"
permalink: /6_Interpretability/interpretability-10weeks/exercises/week06/README.html
---

# Bài tập Tuần 06 — Modify activations

## Cơ bản

Chạy `01_activation_editing.py`, lập bảng chế độ (zero/mean/median/noise) × logit difference. Giải thích chế độ nào "mạnh tay" nhất.

## Nâng cao

Trong `01_activation_editing.py`, quét cường độ scale (0, 0.25, 0.5, 0.75, 1.0) cho 2 vị trí neuron khác nhau, so sánh độ dốc (độ nhạy) của từng vị trí.

## Thử thách

Thiết kế một giả thuyết nhân quả cụ thể ("neuron X gây ra phân biệt A/B"), rồi dùng patching (tham khảo `02_counterfactual_patching.py`) để ủng hộ hoặc bác bỏ. Trình bày như một đoạn nghiên cứu ngắn.

## Bằng chứng cần nộp

- Bảng can thiệp.
- Đồ thị/bảng quét scale.
- Giả thuyết + kết luận patching.

## Rubric (100 điểm)

| Tiêu chí | Điểm |
|---|---:|
| Đúng chức năng: can thiệp đúng vị trí, logit difference đúng | 35 |
| An toàn & xử lý lỗi: baseline sạch, xử lý scale, seed | 25 |
| Chất lượng code/tài liệu: chú thích, cấu trúc rõ | 20 |
| Phân tích: giả thuyết rõ, nêu compensation/ground truth | 20 |
