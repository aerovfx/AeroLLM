---
layout: course
title: "Readme"
permalink: /5_Applications/llm-applications-10weeks/code/README.html
---

# Code lab — LLM Applications (Đánh giá · RAG · An toàn)

[Khoá học](../INDEX.md) · [Lịch](../schedule.md)

Toàn bộ code chạy bằng **Python 3**, không cần GPU, không cần mạng, dùng dữ liệu giả và có thể mock embedding/retrieval. Không file nào chứa secret/token.

| Tuần | Chủ đề | File chính |
|---:|---|---|
| 1 | Metric & bẫy | `week01/01_metrics.py`, `week01/02_calibration.py` |
| 2 | Benchmark & bộ dữ liệu | `week02/01_hellaswag_scoring.py`, `week02/02_benchmark_builder.py` |
| 3 | Eval harness & phân tích lỗi | `week03/01_eval_harness.py`, `week03/02_error_analysis.py` |
| 4 | RAG: embedding/retrieval | `week04/01_embeddings.py`, `week04/02_retriever.py` |
| 5 | Chunking & vector store | `week05/01_chunker.py`, `week05/02_vector_store.py` |
| 6 | Generation, re-rank, multi-hop | `week06/01_reranker.py`, `week06/02_rag_pipeline.py`, `week06/03_multi_hop.py` |
| 7 | Đánh giá RAG | `week07/01_retrieval_metrics.py`, `week07/02_faithfulness.py` |
| 8 | Bias & threat model | `week08/01_bias_metrics.py`, `week08/02_threat_model.py` |
| 9 | Guardrails & red team | `week09/01_guardrails.py`, `week09/02_red_team.py` |
| 10 | Capstone | `week10/01_safe_rag.py`, `week10/02_report.py` |

## Cách chạy chung

Mỗi tuần có `README.md` riêng ghi lệnh chạy và kết quả mong đợi. Ví dụ:

```bash
python 5_Applications/llm-applications-10weeks/code/week01/01_metrics.py
```

## Quy ước an toàn

- Chỉ chạy local trên dữ liệu giả.
- Embedding/retrieval dùng mock (hash/bag-of-words) — không cần mô hình hay API thật.
- Không in secret; không gọi mạng.
- Code red team chỉ minh họa trên mẫu câu giả định, không nhắm vào hệ thống thật.
