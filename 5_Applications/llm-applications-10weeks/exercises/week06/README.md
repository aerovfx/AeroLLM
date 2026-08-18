---
layout: course
title: "Readme"
permalink: /5_Applications/llm-applications-10weeks/exercises/week06/README.html
---

# Bài tập tuần 06 — Generation, re-ranking, multi-hop

Liên kết: [Bài học](../../lessons/week06.md) · [Code](../../code/week06/)

## Mức 1 — Cơ bản

Chạy luồng retrieve → generate (mock) trên 3 câu hỏi với kho văn bản giả; in context được nạp và nguồn trích dẫn.

## Mức 2 — Nâng cao

Cài MMR và so sánh top-3 với các giá trị λ khác nhau (0, 0.5, 1); giải thích sự khác biệt giữa "chỉ relevance" và "cân bằng relevance + diversity".

## Mức 3 — Thử thách

Dựng multi-hop 2 vòng trên kho giả. Chỉ ra một câu hỏi thực sự cần multi-hop và một câu không cần; thảo luận cách phát hiện và giảm lan truyền lỗi ở vòng đầu.

## Rubric (100 điểm)

| Tiêu chí | Điểm |
|---|---:|
| Đúng chức năng: pipeline end-to-end, MMR đúng, trích nguồn hợp lệ | 35 |
| An toàn & xử lý lỗi: từ chối khi thiếu bằng chứng, xử lý context rỗng | 25 |
| Chất lượng code/tài liệu: tách tầng rõ, chú thích đúng chỗ | 20 |
| Phân tích & bằng chứng: so sánh re-rank, bàn multi-hop và lan truyền lỗi | 20 |
