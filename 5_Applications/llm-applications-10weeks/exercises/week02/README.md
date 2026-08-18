---
layout: course
title: "Readme"
permalink: /5_Applications/llm-applications-10weeks/exercises/week02/README.html
---

# Bài tập tuần 02 — Benchmark & bộ dữ liệu đánh giá

Liên kết: [Bài học](../../lessons/week02.md) · [Code](../../code/week02/)

## Mức 1 — Cơ bản

Tạo 5 câu hỏi trắc nghiệm (ngữ cảnh + 4 lựa chọn + đáp án đúng). Chấm bằng một "mô hình ngẫu nhiên" và một mô hình quy tắc đơn giản; tính accuracy của từng cái và so sánh với baseline 25%.

## Mức 2 — Nâng cao

Cài hàm chấm điểm multiple-choice bằng log-likelihood **chuẩn hoá độ dài**. Chứng minh bằng một ví dụ cụ thể rằng đáp án dài không bị phạt vô cớ (so sánh điểm có/không chuẩn hoá).

## Mức 3 — Thử thách

Xây bộ benchmark 20 câu (4 chủ đề, mỗi câu 4 lựa chọn) có metadata độ khó và đáp án. Báo cáo accuracy theo từng nhóm con (chủ đề × độ khó) và nêu rõ hai giới hạn của benchmark bạn viết (contamination, shortcut learning...).

## Rubric (100 điểm)

| Tiêu chí | Điểm |
|---|---:|
| Đúng chức năng: chấm điểm đúng, chuẩn hoá độ dài, baseline hợp lệ | 35 |
| An toàn & xử lý lỗi: xử lý lựa chọn rỗng/thiếu nhãn, seed cố định | 25 |
| Chất lượng code/tài liệu: benchmark có nhãn rõ, chú thích đúng chỗ | 20 |
| Phân tích & bằng chứng: so sánh baseline, bàn về contamination/shortcut | 20 |
