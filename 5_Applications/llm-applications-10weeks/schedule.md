---
layout: course
title: "Schedule"
permalink: /5_Applications/llm-applications-10weeks/schedule.html
---

# Lịch 10 tuần — LLM Applications (Đánh giá · RAG · An toàn)

[← Tổng quan](INDEX.md) · [Đồ án](projects/final_project.md)

Mỗi tuần gồm lý thuyết, một lab có code chạy được và một bài nộp. Ba giai đoạn chính: đánh giá (tuần 1–3), RAG (tuần 4–7), an toàn + tổng hợp (tuần 8–10).

| Tuần | Chủ đề | Lý thuyết cốt lõi | Lab / Sản phẩm nộp |
|---:|---|---|---|
| 1 | Đánh giá mô hình: metric và bẫy | Accuracy/precision/recall/F1, calibration, class imbalance | Bảng metric + phân tích bẫy |
| 2 | Benchmark & bộ dữ liệu đánh giá | HellaSwag-style scoring, length normalization, contamination | Bộ benchmark tổng hợp nhỏ |
| 3 | Eval harness & phân tích lỗi | Baseline, bootstrap CI, error buckets | Harness + báo cáo lỗi |
| 4 | RAG: kiến trúc, embedding/retrieval | Query→embed→similarity→top-k | Retriever đồ chơi |
| 5 | Indexing, chunking, vector store | Chunking, overlap, metadata, brute-force/ANN | Vector store in-memory |
| 6 | Generation, re-ranking, multi-hop | MMR, lexical+semantic rerank, iterative retrieval | Pipeline RAG có trích nguồn |
| 7 | Đánh giá RAG | Recall@k, MRR, nDCG, faithfulness | Bộ metric retrieval + faithfulness |
| 8 | AI Safety: harms, bias, threat model | Bias/fairness metrics, risk = likelihood × impact | Threat model + bias report |
| 9 | Red teaming, guardrails, can thiệp | Jailbreak, prompt injection, input/output filters | Bộ guardrail + red team log |
| 10 | Capstone | Tổng hợp RAG + guardrail + eval | Ứng dụng RAG an toàn có đánh giá |

Chi tiết từng tuần, câu hỏi thảo luận và rubric nằm trong `lessons/weekNN.md`.
