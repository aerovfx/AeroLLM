---
layout: course
title: "Week04"
permalink: /5_Applications/llm-applications-10weeks/lessons/week04.html
---

# Tuần 4 — RAG: kiến trúc và embedding/retrieval / Week 4 — RAG: architecture, embeddings and retrieval

[Mục lục khoá](../INDEX.md) · [Lịch](../schedule.md) · [Tuần 3 ←](week03.md) · [Tuần 5 →](week05.md)

## Mục tiêu học tập / Learning objectives

- Mô tả kiến trúc RAG: ingest → embed → retrieve → generate. / Describe the RAG pipeline.
- Giải thích embedding và cosine similarity; viết embedding mock không cần mô hình. / Explain embeddings and cosine similarity; write a mock embedder.
- Cài retriever top-k trả về đoạn văn liên quan kèm điểm. / Implement a top-k retriever with scores.
- Phân biệt retriever (trả tài liệu) với generator (trả câu trả lời). / Distinguish retriever from generator.

## Công cụ / dữ liệu

- Python 3 chuẩn (`math`, `collections`); kho văn bản giả.
- Nguồn: [`../../../docs/18_rag/index.md`](../../../docs/18_rag/index.md) — `rag_implementation_template.md`.

## Lý thuyết + ví dụ / Theory + examples

RAG tăng cường câu trả lời bằng cách truy xuất ngữ cảnh liên quan thay vì chỉ dựa vào tham số mô hình:

```
Câu hỏi → embed(query) → tìm top-k đoạn gần nhất → nạp vào prompt → generate
```

Embedding ánh xạ văn bản thành vector; độ tương đồng cosine:

$$\mathrm{sim}(A,B)=\frac{A\cdot B}{\lVert A\rVert\,\lVert B\rVert}.$$

Một embedding **mock** (không cần mô hình) có thể là bag-of-words: mỗi chiều là một từ, giá trị là tần suất. Nó đủ để minh hoạ luồng retrieval mà không gọi API. / A bag-of-words embedder is enough to illustrate the retrieval flow.

Retriever khác generator: retriever nhận query → trả danh sách đoạn văn; generator nhận đoạn văn + query → trả câu trả lời. Tách biệt này giúp đánh giá và thay thế từng tầng độc lập. / Separating them enables independent evaluation.

## Lab từng bước / Step-by-step lab

1. Tạo kho 8 đoạn văn giả về một chủ đề (ví dụ: chính sách công ty giả định).
2. Cài `embed(text)` bằng bag-of-words và `cosine(a, b)`.
3. Embed kho + câu hỏi; trả top-3 đoạn gần nhất kèm điểm.
4. Quan sát khi câu hỏi dùng từ đồng nghĩa không có trong kho (giới hạn của bag-of-words).

## Liên kết code / Code links

- [`../code/week04/01_embeddings.py`](../code/week04/01_embeddings.py) — bag-of-words + cosine + chuẩn hoá.
- [`../code/week04/02_retriever.py`](../code/week04/02_retriever.py) — top-k retriever trên kho văn bản giả.

## Câu hỏi thảo luận / Discussion questions

1. Bag-of-words mất thông tin gì so với embedding học được? / What does bag-of-words lose vs. learned embeddings?
2. Khi nào retrieval thất bại dù câu trả lời có trong kho? / When does retrieval fail despite the answer being present?
3. Tại sao tách retriever khỏi generator lại có lợi? / Why separate retriever from generator?
4. `top-k` quá nhỏ/quá lớn gây hệ quả gì? / What happens if top-k is too small or too large?

## Bài tập / Homework

- **Cơ bản**: Cài cosine similarity và kiểm tra với vài cặp vector tay; giải thích giá trị.
- **Nâng cao**: Xây retriever bag-of-words trả top-3 cho 5 câu hỏi; in điểm tương đồng.
- **Thử thách**: Cải thiện embedder bằng TF-IDF hoặc chuẩn hoá trọng số từ; so sánh chất lượng top-3 trước/sau.

## Yêu cầu nộp / Submission

- 1 file Python retriever + bảng kết quả top-k cho 5 câu hỏi + nhận xét 1 điểm yếu.
- Chỉ dùng dữ liệu giả; không cần embedding/mô hình thật.

## Rubric (100 điểm)

| Tiêu chí | Điểm |
|---|---:|
| Đúng chức năng: embed + cosine + top-k đúng, trả kèm điểm | 35 |
| An toàn & xử lý lỗi: xử lý vector rỗng, chia 0, kho trống | 25 |
| Chất lượng code/tài liệu: chú thích luồng dữ liệu rõ | 20 |
| Phân tích & bằng chứng: ví dụ truy xuất đúng/sai, bàn giới hạn | 20 |

## ⚠️ Lưu ý an toàn / Safety notes

- Retrieval trả tài liệu, không tự "biết" đúng sai — phải có bước kiểm chứng nguồn.
- Không nhúng dữ liệu riêng tư thật vào kho minh hoạ.
- Mock embedding chỉ để học luồng; không dùng để triển khai production.
