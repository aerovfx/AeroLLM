---
layout: course
title: "Readme"
permalink: /5_Applications/llm-applications-10weeks/exercises/week04/README.html
---

# Bài tập tuần 04 — RAG: embedding/retrieval

Liên kết: [Bài học](../../lessons/week04.md) · [Code](../../code/week04/)

## Mức 1 — Cơ bản

Cài cosine similarity và kiểm tra với vài cặp vector tay (giống nhau, vuông góc, ngược hướng). Giải thích ý nghĩa từng giá trị trả về.

## Mức 2 — Nâng cao

Xây retriever bag-of-words trả top-3 cho 5 câu hỏi trên một kho ≥8 đoạn văn giả; in điểm tương đồng và đoạn được chọn.

## Mức 3 — Thử thách

Cải thiện embedder bằng TF-IDF (hoặc chuẩn hoá trọng số từ theo độ hiếm) thay cho bag-of-words thuần. So sánh chất lượng top-3 trước/sau và chỉ ra một trường hợp TF-IDF truy xuất tốt hơn rõ rệt.

## Rubric (100 điểm)

| Tiêu chí | Điểm |
|---|---:|
| Đúng chức năng: embed + cosine + top-k đúng, trả kèm điểm | 35 |
| An toàn & xử lý lỗi: xử lý vector rỗng, chia 0, kho trống | 25 |
| Chất lượng code/tài liệu: chú thích luồng dữ liệu rõ | 20 |
| Phân tích & bằng chứng: ví dụ truy xuất đúng/sai, bàn giới hạn | 20 |
