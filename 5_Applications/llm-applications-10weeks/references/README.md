---
layout: course
title: "Readme"
permalink: /5_Applications/llm-applications-10weeks/references/README.html
---

# References — Ánh xạ tuần → module docs nguồn

Bảng dưới đây ánh xạ từng tuần của khóa học về tài liệu gốc trong `docs/`. Ký hiệu `../../../` bên dưới tính từ thư mục `references/` để về gốc repo.

| Tuần | Chủ đề | Nguồn chính (docs) |
|---:|---|---|
| 1 | Metric cơ bản và bẫy | [`../../../docs/09_quantitative_evaluations/index.md`](../../../docs/09_quantitative_evaluations/index.md) — `aero_llm_03_perplexity.md`, `aero_llm_02_numerical_issues_in_logits_and_softmax.md` |
| 2 | Benchmark & bộ dữ liệu | `aero_llm_06_hellaswag.md`, `aero_llm_13_superglue_and_other_amalgamations.md`, `aero_llm_15_non_technical_benchmarks.md` |
| 3 | Harness, baseline, phân tích lỗi | `aero_llm_01_promises_and_challenges_of_quantitative_evaluations.md`, `aero_llm_016_black_box_evals.md` |
| 4 | RAG kiến trúc, embedding/retrieval | [`../../../docs/18_rag/index.md`](../../../docs/18_rag/index.md) — `rag_implementation_template.md` |
| 5 | Indexing, chunking, vector store | `full_template_local_rag_voi_ollama_qdrant_fastapi.md`, `advanced_rag_with_vector_databases_and_retrievers/02_build_a_comprehensive_rag_application/01_introduction_to_faiss_for_rag/` |
| 6 | Generation, re-ranking, multi-hop | `advanced_rag_with_vector_databases_and_retrievers/01_advanced_retrievers_for_rag/02_work_with_advanced_retrievers_in_langchain/` |
| 7 | Đánh giá RAG | `rag_implementation_template.md` (PHASE 8: Evaluation & Monitoring), `rag_noibo.md` |
| 8 | AI Safety: harms, bias, threat model | [`../../../docs/19_ai_safety/index.md`](../../../docs/19_ai_safety/index.md) — `aero_llm_01_ai_safety_and_alignment.md`, `aero_llm_02_why_can_t_ai_just_be_safe_and_moral.md`; `aero_llm_14_assessing_bias_and_fairness.md` (module 09) |
| 9 | Red teaming, guardrails, can thiệp | `aero_llm_017_red_teaming.md` (module 09), `aero_llm_05_hands_on_hack_an_ai_to_steal_a_password_.md` (module 19) |
| 10 | Capstone tổng hợp | Tổng hợp cả ba module + `rag_implementation_template.md` PHASE 9 (Security & Governance) |

## Lưu ý sử dụng nguồn

- Các file gốc là tài liệu chuyên sâu; bài học chỉ **mở rộng** lý thuyết cốt lõi, không chép nguyên văn.
- Code trong khóa dùng dữ liệu giả và có thể mock embedding/retrieval để chạy local an toàn, không cần API thật.
- Không chạy red team / đánh giá an toàn trên mô hình của bên thứ ba mà chưa được ủy quyền.
