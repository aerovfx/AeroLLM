---
layout: course
title: "Readme"
permalink: /5_Applications/llm-applications-10weeks/exercises/week10/README.html
---

# Bài tập tuần 10 — Capstone

Liên kết: [Bài học](../../lessons/week10.md) · [Đồ án](../../projects/final_project.md) · [Code](../../code/week10/)

## Mức 1 — Cơ bản

Chạy pipeline RAG end-to-end trên kho giả (≥8 văn bản); in câu trả lời + nguồn cho 3 câu hỏi có đáp án và 1 câu ngoài phạm vi.

## Mức 2 — Nâng cao

Thêm guardrail (đầu vào + đầu ra) vào pipeline; đo block rate và faithfulness trên một golden set nhỏ (≥10 câu).

## Mức 3 — Thử thách

Hoàn thiện dự án cuối khóa theo `projects/final_project.md`: pipeline tích hợp, golden set ≥30 câu, bảng metric (retrieval + faithfulness), phân tích lỗi và system card 1 trang.

## Rubric (100 điểm)

| Tiêu chí | Điểm |
|---|---:|
| Đúng chức năng: pipeline tích hợp chạy end-to-end, tái lập được | 35 |
| An toàn & xử lý lỗi: guardrail + từ chối ngoài phạm vi + cleanup | 25 |
| Chất lượng code/tài liệu: cấu trúc module, README, system card | 20 |
| Đánh giá & phân tích: metric retrieval + faithfulness, mẫu lỗi, bằng chứng | 20 |
