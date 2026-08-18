---
layout: course
title: "Week05"
permalink: /5_Applications/llm-applications-10weeks/lessons/week05.html
---

# Tuần 5 — Indexing, chunking và vector store / Week 5 — Indexing, chunking and vector stores

[Mục lục khoá](../INDEX.md) · [Lịch](../schedule.md) · [Tuần 4 ←](week04.md) · [Tuần 6 →](week06.md)

## Mục tiêu học tập / Learning objectives

- Giải thích vì sao phải chunk tài liệu và vai trò của overlap. / Explain chunking and why overlap matters.
- Cài chunker cố định/đệ quy và gán metadata (id, nguồn, vị trí). / Implement fixed/recursive chunking with metadata.
- Xây vector store in-memory hỗ trợ thêm + tìm kiếm cosine. / Build an in-memory vector store with add + search.
- Phân biệt tìm kiếm chính xác (brute-force) với ANN (xấp xỉ). / Distinguish exact vs. approximate nearest neighbor.

## Công cụ / dữ liệu

- Python 3 chuẩn; tài liệu giả nhiều đoạn.
- Nguồn: [`../../../docs/18_rag/index.md`](../../../docs/18_rag/index.md) — `full_template_local_rag_voi_ollama_qdrant_fastapi.md`, FAISS intro trong `advanced_rag_with_vector_databases_and_retrievers/`.

## Lý thuyết + ví dụ / Theory + examples

Chunking cắt văn bản dài thành đoạn ngắn để retrieval trả về đơn vị ngữ nghĩa vừa phải, không phải cả tài liệu. Overlap giữ các câu ở ranh giới để không mất ngữ cảnh bị cắt đôi. / Chunking yields retrieval units; overlap preserves boundary context.

Ba chiến lược chunking:

1. **Fixed size**: cắt theo số ký tự/token; đơn giản nhưng có thể cắt giữa câu.
2. **Recursive**: cắt theo dấu phân cách ưu tiên (đoạn → câu → từ).
3. **Semantic**: cắt theo ý nghĩa (khó hơn, cần embedding).

Metadata là "chìa khoá" để lọc và re-rank: mỗi chunk nên mang `id`, `source`, `position` để biết đoạn nào thuộc tài liệu nào. / Metadata enables filtering and source citation.

Vector store: tìm kiếm **chính xác** quét toàn bộ (độ phức tạp $O(N\cdot D)$), phù hợp tập nhỏ; ANN (HNSW/IVF/PQ) đánh đổi chút chính xác lấy tốc độ khi $N$ lớn. / Exact search is $O(N\cdot D)$; ANN trades a little accuracy for speed.

## Lab từng bước / Step-by-step lab

1. Viết tài liệu giả ~1200 từ; cài chunker cố định với `chunk_size` và `overlap`.
2. Gán metadata cho từng chunk (`id`, `source`, `start`); xác nhận overlap giữ nguyên câu ranh giới.
3. Xây vector store in-memory: `add(vector, payload)` và `search(query, k)` bằng cosine.
4. Tìm top-3 cho một câu hỏi; kiểm tra metadata giúp trích nguồn đúng tài liệu.

## Liên kết code / Code links

- [`../code/week05/01_chunker.py`](../code/week05/01_chunker.py) — fixed/recursive chunking + overlap + metadata.
- [`../code/week05/02_vector_store.py`](../code/week05/02_vector_store.py) — vector store in-memory với cosine search.

## Câu hỏi thảo luận / Discussion questions

1. Overlap quá lớn gây hệ quả gì (trùng lặp, chi phí)? / What does too much overlap cost?
2. Khi nào chunk theo section tốt hơn chunk cố định? / When is section-based chunking better?
3. Vì sao metadata yếu làm RAG yếu? / Why does weak metadata weaken RAG?
4. Khi nào cần ANN thay vì brute-force? / When do you need ANN over brute-force?

## Bài tập / Homework

- **Cơ bản**: Cắt một văn bản giả thành chunk cố định; in số chunk và đoạn overlap.
- **Nâng cao**: Thêm metadata cho chunk và lưu vào vector store; truy xuất top-k kèm nguồn.
- **Thử thách**: Cài recursive chunker theo dấu phân cách ưu tiên; so sánh chất lượng chunk với fixed chunker.

## Yêu cầu nộp / Submission

- 1 file Python chunker + 1 vector store + bảng kết quả truy xuất kèm metadata.
- Chỉ dùng dữ liệu giả; không cần vector DB thật.

## Rubric (100 điểm)

| Tiêu chí | Điểm |
|---|---:|
| Đúng chức năng: chunk đúng kích thước, overlap hợp lệ, search đúng | 35 |
| An toàn & xử lý lỗi: văn bản rỗng, chunk rỗng, k > số vector | 25 |
| Chất lượng code/tài liệu: metadata rõ, chú thích đúng chỗ | 20 |
| Phân tích & bằng chứng: so sánh chiến lược chunk, bàn ANN vs exact | 20 |

## ⚠️ Lưu ý an toàn / Safety notes

- Chunk quá nhỏ dễ mất ngữ cảnh → tăng hallucination khi generate.
- Đừng lưu văn bản nhạy cảm thật vào store minh hoạ; mask PII nếu có.
- Metadata chứa thông tin phân quyền (permission) cần được kiểm tra trước khi trả kết quả.
