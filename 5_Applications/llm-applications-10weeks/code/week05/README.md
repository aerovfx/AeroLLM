---
layout: course
title: "Readme"
permalink: /5_Applications/llm-applications-10weeks/code/week05/README.html
---

# Tuần 05 — Code minh họa: Chunking & vector store

| File | Chức năng | Chạy | Kết quả mong đợi |
|---|---|---|---|
| `01_chunker.py` | Chunk fixed/recursive + overlap + metadata | `python 01_chunker.py` | In số chunk và vị trí từng chunk |
| `02_vector_store.py` | Vector store in-memory với cosine search | `python 02_vector_store.py` | In top-k vector gần nhất kèm payload |

## 01_chunker.py

**Chức năng:** Cắt văn bản thành chunk theo kích thước cố định (có overlap) hoặc theo đoạn; mỗi chunk gắn metadata.

```python
{% include_relative 01_chunker.py %}
```

## 02_vector_store.py

**Chức năng:** Lưu vector + payload, tìm kiếm top-k bằng cosine similarity (brute-force).

```python
{% include_relative 02_vector_store.py %}
```
