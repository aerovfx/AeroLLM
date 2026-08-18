---
layout: course
title: "Week07"
permalink: /5_Applications/llm-applications-10weeks/lessons/week07.html
---

# Tuần 7 — Đánh giá RAG (retrieval quality, faithfulness) / Week 7 — Evaluating RAG (retrieval quality, faithfulness)

[Mục lục khoá](../INDEX.md) · [Lịch](../schedule.md) · [Tuần 6 ←](week06.md) · [Tuần 8 →](week08.md)

## Mục tiêu học tập / Learning objectives

- Giải thích vì sao RAG cần đánh giá riêng hai tầng: retrieval và generation. / Explain why retrieval and generation are evaluated separately.
- Tính recall@k, precision@k, MRR và nDCG cho retrieval. / Compute recall@k, precision@k, MRR, nDCG.
- Định nghĩa faithfulness/groundedness và viết kiểm tra heuristic. / Define faithfulness and write a heuristic check.
- Xây một "golden set" (câu hỏi + nguồn đúng + câu trả lời đúng). / Build a golden set.

## Công cụ / dữ liệu

- Python 3 chuẩn; golden set giả (câu hỏi, nguồn đúng, câu trả lời).
- Nguồn: [`../../../docs/18_rag/index.md`](../../../docs/18_rag/index.md) — `rag_implementation_template.md` PHASE 8 (Evaluation & Monitoring), `rag_noibo.md`.

## Lý thuyết + ví dụ / Theory + examples

Retrieval đánh giá bằng **xếp hạng** chứ không chỉ đúng/sai:

- **Recall@k**: trong k kết quả đầu có bao nhiêu nguồn đúng.
- **Precision@k**: tỷ lệ kết quả đầu là nguồn đúng.
- **MRR** (Mean Reciprocal Rank): trung bình $\frac{1}{\mathrm{rank}}$ của nguồn đúng đầu tiên.
- **nDCG**: đo chất lượng xếp hạng có trọng số theo vị trí.

Ví dụ MRR với 3 câu hỏi có nguồn đúng ở hạng 1, 3, và không tìm thấy:

```python
mrr = (1/1 + 1/3 + 0) / 3   # = 0.444...
```

Generation đánh giá bằng **faithfulness** (câu trả lời có bám vào nguồn không) và **answer relevance** (có trả lời đúng câu hỏi không). Một heuristic không cần mô hình: kiểm tra mọi "claim" trong câu trả lời có xuất hiện (hoặc gần khớp) trong context không. / Faithfulness = every claim is supported by retrieved context.

## Lab từng bước / Step-by-step lab

1. Tạo golden set 8 câu hỏi, mỗi câu có tập nguồn đúng.
2. Cài recall@k, precision@k, MRR, nDCG; chạy trên kết quả retrieval giả.
3. Cài kiểm tra faithfulness heuristic (khớp từ khoá claim ↔ context); phân loại "hỗ trợ"/"không hỗ trợ".
4. Báo cáo một ma trận nhỏ: retrieval tốt nhưng generation sai nguồn, và ngược lại.

## Liên kết code / Code links

- [`../code/week07/01_retrieval_metrics.py`](../code/week07/01_retrieval_metrics.py) — recall@k, precision@k, MRR, nDCG.
- [`../code/week07/02_faithfulness.py`](../code/week07/02_faithfulness.py) — kiểm tra groundedness heuristic.

## Câu hỏi thảo luận / Discussion questions

1. Vì sao accuracy không đủ để đánh giá retrieval? / Why isn't accuracy enough for retrieval?
2. Recall@k và precision@k đánh đổi nhau thế nào khi tăng k? / How do recall@k and precision@k trade off?
3. Faithfulness khác "đúng sự thật" (factuality) thế nào? / How does faithfulness differ from factuality?
4. Golden set tốt cần đặc điểm gì? / What makes a good golden set?

## Bài tập / Homework

- **Cơ bản**: Tính recall@5 và MRR cho 5 câu hỏi với kết quả retrieval giả.
- **Nâng cao**: Cài nDCG và so sánh hai thứ tự xếp hạng khác nhau cho cùng một câu hỏi.
- **Thử thách**: Xây golden set 15 câu và một faithfulness heuristic; báo cáo ma trận retrieval×generation.

## Yêu cầu nộp / Submission

- 1 file metric retrieval + 1 file faithfulness + bảng kết quả trên golden set.
- Nêu rõ cách gán nhãn nguồn đúng; chỉ dùng dữ liệu giả.

## Rubric (100 điểm)

| Tiêu chí | Điểm |
|---|---:|
| Đúng chức năng: metric chính xác (kể cả biên), heuristic hợp lệ | 35 |
| An toàn & xử lý lỗi: xử lý hạng thiếu, chia 0, claim rỗng | 25 |
| Chất lượng code/tài liệu: golden set có nhãn rõ, chú thích đúng | 20 |
| Phân tích & bằng chứng: ma trận retrieval×generation, giải thích metric | 20 |

## ⚠️ Lưu ý an toàn / Safety notes

- Metric retrieval không đo được "câu trả lời có đúng sự thật không" — chỉ đo xếp hạng nguồn.
- Heuristic faithfulness chỉ là xấp xỉ; với sản phẩm thật cần đánh giá con người hoặc model judge.
- Không dùng dữ liệu thật của người dùng để dựng golden set nếu chưa được phép.
