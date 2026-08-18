---
layout: course
title: "Readme"
permalink: /5_Applications/llm-applications-10weeks/code/week10/README.html
---

# Tuần 10 — Code minh họa: Capstone

| File | Chức năng | Chạy | Kết quả mong đợi |
|---|---|---|---|
| `01_safe_rag.py` | Pipeline RAG tích hợp guardrail | `python 01_safe_rag.py` | In câu trả lời + nguồn, hoặc BLOCKED/từ chối |
| `02_report.py` | Tổng hợp metric + báo cáo | `python 02_report.py` | In recall@k, MRR, faithfulness |

## 01_safe_rag.py

**Chức năng:** Lắp pipeline end-to-end: guardrail đầu vào → retrieve → generate grounded → từ chối ngoài phạm vi.

```python
{% include_relative 01_safe_rag.py %}
```

## 02_report.py

**Chức năng:** Gom metric retrieval và faithfulness trên golden set giả thành báo cáo tái lập được.

```python
{% include_relative 02_report.py %}
```
