---
layout: course
title: "Readme"
permalink: /5_Applications/llm-applications-10weeks/exercises/week05/README.html
---

# Bài tập tuần 05 — Chunking & vector store

Liên kết: [Bài học](../../lessons/week05.md) · [Code](../../code/week05/)

## Mức 1 — Cơ bản

Cắt một văn bản giả thành chunk cố định (chunk_size, overlap). In số chunk và chỉ ra đoạn overlap giữa hai chunk liền kề.

## Mức 2 — Nâng cao

Thêm metadata (`id`, `source`, `start`) cho từng chunk và lưu vào vector store in-memory. Truy xuất top-k cho một câu hỏi và in kèm nguồn của từng kết quả.

## Mức 3 — Thử thách

Cài recursive chunker theo dấu phân cách ưu tiên (đoạn → câu → từ). So sánh chất lượng chunk với fixed chunker (ví dụ: có câu bị cắt đôi không) trên cùng một văn bản và nêu trường hợp recursive tốt hơn.

## Rubric (100 điểm)

| Tiêu chí | Điểm |
|---|---:|
| Đúng chức năng: chunk đúng kích thước, overlap hợp lệ, search đúng | 35 |
| An toàn & xử lý lỗi: văn bản rỗng, chunk rỗng, k > số vector | 25 |
| Chất lượng code/tài liệu: metadata rõ, chú thích đúng chỗ | 20 |
| Phân tích & bằng chứng: so sánh chiến lược chunk, bàn ANN vs exact | 20 |
