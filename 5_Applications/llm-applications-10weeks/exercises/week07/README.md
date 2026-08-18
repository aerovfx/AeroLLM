---
layout: course
title: "Readme"
permalink: /5_Applications/llm-applications-10weeks/exercises/week07/README.html
---

# Bài tập tuần 07 — Đánh giá RAG

Liên kết: [Bài học](../../lessons/week07.md) · [Code](../../code/week07/)

## Mức 1 — Cơ bản

Tính recall@5 và MRR cho 5 câu hỏi với kết quả retrieval giả (mỗi câu có danh sách kết quả và tập nguồn đúng).

## Mức 2 — Nâng cao

Cài nDCG@k và so sánh hai thứ tự xếp hạng khác nhau cho cùng một câu hỏi; giải thích vì sao nDCG phân biệt được chất lượng xếp hạng tốt hơn recall.

## Mức 3 — Thử thách

Xây golden set 15 câu (câu hỏi, nguồn đúng, câu trả lời đúng) và một faithfulness heuristic. Báo cáo ma trận 2×2: retrieval tốt/kém × generation bám nguồn/lệch nguồn, kèm ví dụ mỗi ô.

## Rubric (100 điểm)

| Tiêu chí | Điểm |
|---|---:|
| Đúng chức năng: metric chính xác (kể cả biên), heuristic hợp lệ | 35 |
| An toàn & xử lý lỗi: xử lý hạng thiếu, chia 0, claim rỗng | 25 |
| Chất lượng code/tài liệu: golden set có nhãn rõ, chú thích đúng | 20 |
| Phân tích & bằng chứng: ma trận retrieval×generation, giải thích metric | 20 |
