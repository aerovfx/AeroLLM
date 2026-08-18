---
layout: course
title: "Readme"
permalink: /5_Applications/llm-applications-10weeks/code/week04/README.html
---

# Tuần 04 — Code minh họa: RAG embedding/retrieval

| File | Chức năng | Chạy | Kết quả mong đợi |
|---|---|---|---|
| `01_embeddings.py` | Bag-of-words + cosine similarity | `python 01_embeddings.py` | In cosine giữa query và từng doc |
| `02_retriever.py` | Retriever top-k trả đoạn văn kèm điểm | `python 02_retriever.py` | In top-2 đoạn gần nhất cho 3 câu hỏi |

## 01_embeddings.py

**Chức năng:** Xây vector bag-of-words cho các văn bản và tính cosine similarity, minh hoạ embedding không cần mô hình.

```python
{% include_relative 01_embeddings.py %}
```

## 02_retriever.py

**Chức năng:** Xây retriever từ kho văn bản, nhận câu hỏi và trả top-k đoạn liên quan kèm điểm.

```python
{% include_relative 02_retriever.py %}
```
