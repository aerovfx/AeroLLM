---
layout: course
title: "Readme"
permalink: /5_Applications/llm-applications-10weeks/code/week07/README.html
---

# Tuần 07 — Code minh họa: Đánh giá RAG

| File | Chức năng | Chạy | Kết quả mong đợi |
|---|---|---|---|
| `01_retrieval_metrics.py` | recall@k, precision@k, MRR, nDCG | `python 01_retrieval_metrics.py` | In 4 metric retrieval |
| `02_faithfulness.py` | Kiểm tra groundedness heuristic | `python 02_faithfulness.py` | In tỷ lệ claim được hỗ trợ cho 2 câu trả lời |

## 01_retrieval_metrics.py

**Chức năng:** Tính các metric xếp hạng chuẩn cho retrieval từ danh sách kết quả và tập nguồn đúng.

```python
{% include_relative 01_retrieval_metrics.py %}
```

## 02_faithfulness.py

**Chức năng:** Tách câu trả lời thành claim và kiểm tra từng claim có được context hỗ trợ không (heuristic).

```python
{% include_relative 02_faithfulness.py %}
```
