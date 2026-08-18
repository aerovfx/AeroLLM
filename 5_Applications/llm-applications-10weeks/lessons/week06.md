---
layout: course
title: "Week06"
permalink: /5_Applications/llm-applications-10weeks/lessons/week06.html
---

# Tuần 6 — Generation, re-ranking và multi-hop RAG / Week 6 — Generation, re-ranking and multi-hop RAG

[Mục lục khoá](../INDEX.md) · [Lịch](../schedule.md) · [Tuần 5 ←](week05.md) · [Tuần 7 →](week07.md)

## Mục tiêu học tập / Learning objectives

- Giải thích luồng retrieve → re-rank → generate và vai trò của re-ranking. / Explain retrieve → re-rank → generate.
- Cài MMR (Maximum Marginal Relevance) cân bằng độ liên quan và độ đa dạng. / Implement MMR.
- Viết generator mock trả lời chỉ từ context kèm trích nguồn. / Write a mock generator grounded in context with citations.
- Mô tả multi-hop RAG (truy xuất nhiều vòng) và khi nào cần nó. / Describe multi-hop RAG and when it is needed.

## Công cụ / dữ liệu

- Python 3 chuẩn; kho văn bản giả nhiều tài liệu.
- Nguồn: [`../../../docs/18_rag/index.md`](../../../docs/18_rag/index.md) — advanced retrievers (MMR, ensemble) trong `advanced_rag_with_vector_databases_and_retrievers/`.

## Lý thuyết + ví dụ / Theory + examples

Re-ranking sắp xếp lại top-k thô bằng một tín hiệu mạnh hơn. MMR chọn lặp lại đoạn tối đa:

$$\mathrm{MMR}=\arg\max_{D_i\in R\setminus S}\Big[\lambda\,\mathrm{sim}(Q,D_i)-(1-\lambda)\max_{D_j\in S}\mathrm{sim}(D_i,D_j)\Big],$$

với $\lambda$ cân bằng **relevance** (gần câu hỏi) và **diversity** (khác các đoạn đã chọn). / λ balances relevance vs. diversity.

Generator "grounded": chỉ trả lời từ context được cung cấp, trích nguồn rõ, và trả "không tìm thấy" khi thiếu bằng chứng — đây là cách giảm hallucination trực tiếp. / A grounded generator cites sources and refuses when evidence is missing.

Multi-hop RAG lặp: câu trả lời vòng 1 trở thành truy vấn vòng 2 để tìm thông tin bổ sung. Cần khi câu hỏi đòi hỏi nối nhiều mảnh (ví dụ: "ai là CEO của công ty đã mua lại X?"). / Multi-hop joins multiple pieces across retrieval rounds.

## Lab từng bước / Step-by-step lab

1. Chuẩn bị kho 10 đoạn giả trong đó một vài đoạn gần trùng nhau về chủ đề.
2. Cài MMR trên kết quả similarity; so sánh top-3 trước/sau re-rank.
3. Cài generator mock: chọn đoạn chứa từ khoá của câu hỏi, trả câu trả lời + nguồn; nếu không đủ → "không tìm thấy".
4. Cài một vòng multi-hop: truy vấn vòng 1 → rút thực thể → truy vấn vòng 2.

## Liên kết code / Code links

- [`../code/week06/01_reranker.py`](../code/week06/01_reranker.py) — MMR + lexical rerank.
- [`../code/week06/02_rag_pipeline.py`](../code/week06/02_rag_pipeline.py) — retrieve → rerank → generate có trích nguồn.
- [`../code/week06/03_multi_hop.py`](../code/week06/03_multi_hop.py) — truy xuất lặp hai vòng.

## Câu hỏi thảo luận / Discussion questions

1. Khi nào re-rank cải thiện rõ nhất? / When does re-ranking help most?
2. λ = 0 và λ = 1 trong MMR nghĩa là gì? / What do λ=0 and λ=1 mean?
3. "Trích nguồn" làm giảm hallucination thế nào? / How does citation reduce hallucination?
4. Multi-hop có thể lan truyền lỗi ở vòng đầu không? Làm sao giảm? / Can multi-hop propagate early errors?

## Bài tập / Homework

- **Cơ bản**: Chạy retrieve → generate mock trên 3 câu hỏi; in context và nguồn.
- **Nâng cao**: Cài MMR và so sánh top-3 (relevance vs. diversity) với λ khác nhau.
- **Thử thách**: Dựng multi-hop 2 vòng trên kho giả; chỉ ra một câu hỏi cần multi-hop và một câu không cần.

## Yêu cầu nộp / Submission

- 1 pipeline RAG (retrieve + rerank + generate) + bảng kết quả 5 câu hỏi kèm nguồn.
- Chỉ dùng dữ liệu giả và generator mock; không gọi API.

## Rubric (100 điểm)

| Tiêu chí | Điểm |
|---|---:|
| Đúng chức năng: pipeline chạy end-to-end, MMR đúng, trích nguồn hợp lệ | 35 |
| An toàn & xử lý lỗi: từ chối khi thiếu bằng chứng, xử lý context rỗng | 25 |
| Chất lượng code/tài liệu: tách tầng rõ, chú thích đúng chỗ | 20 |
| Phân tích & bằng chứng: so sánh re-rank, bàn multi-hop và lan truyền lỗi | 20 |

## ⚠️ Lưu ý an toàn / Safety notes

- Generator mock không phải mô hình thật; đừng dùng nó để trả lời thông tin thực tế.
- Luôn gắn câu trả lời với nguồn; nếu nguồn không đủ thì phải từ chối rõ ràng.
- Re-ranking chỉ thay đổi thứ tự, không kiểm chứng tính đúng đắn của nội dung.
