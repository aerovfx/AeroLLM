---
layout: course
title: "Week10"
permalink: /5_Applications/llm-applications-10weeks/lessons/week10.html
---

# Tuần 10 — Capstone: ứng dụng RAG an toàn có đánh giá / Week 10 — Capstone: a safe, evaluated RAG application

[Mục lục khoá](../INDEX.md) · [Lịch](../schedule.md) · [Đồ án](../projects/final_project.md) · [Tuần 9 ←](week09.md)

## Mục tiêu học tập / Learning objectives

- Tích hợp ba mảng đã học thành một hệ thống: RAG + guardrails + đánh giá. / Integrate RAG + guardrails + evaluation into one system.
- Chạy pipeline end-to-end có trích nguồn và từ chối ngoài phạm vi. / Run the pipeline end-to-end with citation and out-of-scope refusal.
- Tính metric retrieval + faithfulness trên golden set. / Compute retrieval and faithfulness metrics on a golden set.
- Viết system card: giới hạn, rủi ro, biện pháp giảm thiểu. / Write a system card.

## Công cụ / dữ liệu

- Python 3 chuẩn; toàn bộ module code của 9 tuần trước tái sử dụng.
- Nguồn: tổng hợp cả ba module + `rag_implementation_template.md` PHASE 9 (Security & Governance).

## Lý thuyết + ví dụ / Theory + examples

Capstone là phép kiểm tra **tích hợp**: một hệ thống thật không phải là tổng các phần, mà là các phần phối hợp và có đo lường. Kiến trúc gợi ý:

```
Ingest → Chunk → Vector store → [Guardrail input] → Retrieve → Rerank
      → Generate (grounded) → [Guardrail output] → Metric
```

Ba yêu cầu "sống còn":

1. **Grounded**: chỉ trả lời từ context, kèm nguồn; thiếu bằng chứng → "không tìm thấy".
2. **Guarded**: chặn injection đầu vào và nội dung cấm đầu ra.
3. **Measured**: mọi tuyên bố chất lượng đi kèm con số (recall@k, MRR, faithfulness) và mẫu lỗi.

System card ghi lại: mục đích, dữ liệu, giới hạn đã biết, rủi ro và biện pháp giảm thiểu — để người dùng hiểu đúng năng lực hệ thống. / A system card documents purpose, limits, risks, and mitigations.

## Lab từng bước / Step-by-step lab

1. Lắp pipeline từ code tuần 4–6 (ingest, retrieve, generate) và tuần 9 (guardrails).
2. Nạp golden set tuần 7; chạy metric retrieval + faithfulness.
3. Chạy 5 câu hỏi demo: 3 có đáp án, 1 ngoài phạm vi, 1 prompt injection.
4. Viết system card 1 trang và chuẩn bị demo 5 phút.

## Liên kết code / Code links

- [`../code/week10/01_safe_rag.py`](../code/week10/01_safe_rag.py) — pipeline tích hợp RAG + guardrail.
- [`../code/week10/02_report.py`](../code/week10/02_report.py) — tổng hợp metric và in báo cáo.

## Câu hỏi thảo luận / Discussion questions

1. Điểm nào trong pipeline dễ bị "âm thầm hỏng" nhất? / Which pipeline point fails most silently?
2. Một metric tốt nhưng người dùng vẫn không hài lòng — vì sao? / Why can good metrics still leave users unhappy?
3. System card nên được cập nhật khi nào? / When should a system card be updated?
4. Bạn sẽ dừng triển khai nếu metric nào dưới ngưỡng? / Which metric below threshold blocks deployment?

## Bài tập / Homework

- **Cơ bản**: Chạy pipeline end-to-end trên kho giả; in câu trả lời + nguồn cho 3 câu hỏi.
- **Nâng cao**: Thêm guardrail và đo block rate + faithfulness trên golden set nhỏ.
- **Thử thách**: Hoàn thiện system card và báo cáo đánh giá đầy đủ cho dự án cuối khóa.

## Yêu cầu nộp / Submission

- Dự án cuối khóa theo [`../projects/final_project.md`](../projects/final_project.md) + bản demo.
- Nộp README tái lập, mã nguồn, bảng metric, và system card.

## Rubric (100 điểm)

| Tiêu chí | Điểm |
|---|---:|
| Đúng chức năng: pipeline tích hợp chạy end-to-end, tái lập được | 35 |
| An toàn & xử lý lỗi: guardrail + từ chối ngoài phạm vi + cleanup | 25 |
| Chất lượng code/tài liệu: cấu trúc module, README, system card | 20 |
| Đánh giá & phân tích: metric retrieval + faithfulness, mẫu lỗi, bằng chứng | 20 |

## ⚠️ Lưu ý an toàn / Safety notes

- Không triển khai hệ thống với dữ liệu thật của người dùng khi chưa có đánh giá an toàn và ủy quyền.
- Không dùng generator mock để trả lời thông tin thực tế có hậu quả (y tế, pháp lý, tài chính).
- Mọi con số phải tái lập được (seed + lệnh chạy); không "trang trí" kết quả.
