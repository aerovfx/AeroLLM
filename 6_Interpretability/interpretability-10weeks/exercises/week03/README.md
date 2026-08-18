---
layout: course
title: "Readme"
permalink: /6_Interpretability/interpretability-10weeks/exercises/week03/README.html
---

# Bài tập Tuần 03 — Token embeddings I: probing

## Cơ bản

Chạy `01_cosine_similarity.py`, liệt kê 3 cặp token tương đồng nhất và giải thích dựa trên cấu trúc cấy sẵn. Nêu vì sao cosine bỏ qua độ lớn vector.

## Nâng cao

Trong `02_analogy_arithmetic.py`, tự thêm một trục ngữ nghĩa mới (ví dụ "thành phố lớn vs làng quê") bằng hiệu hai vector, rồi chiếu tập token lên đó và báo cáo thứ hạng.

## Thử thách

Sinh nhúng ngẫu nhiên 10 lần với seed khác nhau, đếm xem có bao nhiêu "cụm giả" (similarity > 0.5) xuất hiện tình cờ. Viết một đoạn ngắn bàn về nguy cơ overinterpretation từ heatmap.

## Bằng chứng cần nộp

- Ma trận similarity + giải thích.
- Trục ngữ nghĩa mới + thứ hạng chiếu.
- Thí nghiệm ngẫu nhiên + nhận xét.

## Rubric (100 điểm)

| Tiêu chí | Điểm |
|---|---:|
| Đúng chức năng: cosine/analogy tính đúng, trục chiếu đúng | 35 |
| An toàn & xử lý lỗi: chuẩn hoá vector, xử lý norm 0, seed | 25 |
| Chất lượng code/tài liệu: chú thích, in kết quả rõ | 20 |
| Phân tích: nhận diện ảo giác diễn giải, nêu giới hạn | 20 |
