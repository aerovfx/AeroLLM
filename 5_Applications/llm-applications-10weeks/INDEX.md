---
layout: course
title: "Index"
permalink: /5_Applications/llm-applications-10weeks/INDEX.html
---

# LLM Applications — Đánh giá, RAG & AI Safety (10 tuần)

Khóa học 10 tuần về **ứng dụng mô hình ngôn ngữ lớn (LLM)**, mở rộng từ ba module tài liệu gốc của AeroLLM: đánh giá định lượng, Retrieval-Augmented Generation (RAG) và AI Safety. Học viên học cách đo lường mô hình một cách đáng tin cậy, xây dựng hệ thống truy xuất-tăng cường (RAG), rồi bọc toàn bộ bằng lớp an toàn và đánh giá.

## Cấu trúc

- [Lịch học](schedule.md)
- `lessons/week01.md` … `week10.md`: bài học theo tuần.
- [Code & môi trường](code/README.md): script Python minh họa, chạy local với dữ liệu giả.
- `exercises/week01/README.md` … `week10/README.md`: bài tập 3 mức kèm rubric.
- [Dự án cuối khóa](projects/final_project.md)
- [References](references/README.md): bảng ánh xạ tuần → module docs nguồn.

## Lộ trình 10 tuần

| Tuần | Chủ đề | Module gốc |
|---:|---|---|
| 1 | Đánh giá mô hình: mục tiêu, metric cơ bản và bẫy | 09 |
| 2 | Benchmark & bộ dữ liệu đánh giá | 09 |
| 3 | Eval harness, đối sánh baseline & phân tích lỗi | 09 |
| 4 | RAG: kiến trúc và embedding/retrieval | 18 |
| 5 | Indexing, chunking và vector store | 18 |
| 6 | Generation + re-ranking + multi-hop RAG | 18 (mở rộng) |
| 7 | Đánh giá RAG (retrieval quality, faithfulness) | 18 |
| 8 | AI Safety: harms, bias và mô hình đe dọa | 19 |
| 9 | Red teaming, guardrails và can thiệp an toàn | 19 |
| 10 | Capstone: ứng dụng RAG an toàn có đánh giá | tổng hợp |

## Quy tắc thực hành

Chỉ chạy thí nghiệm trong môi trường do bạn kiểm soát. Toàn bộ code trong khóa dùng dữ liệu giả/local, có thể mock embedding và retrieval — không cần API thật, không chứa secret/token. Khi đánh giá hoặc red team một mô hình thật, chỉ làm trên mô hình bạn sở hữu hoặc được ủy quyền rõ ràng.
