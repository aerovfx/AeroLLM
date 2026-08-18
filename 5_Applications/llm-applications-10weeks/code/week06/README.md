---
layout: course
title: "Readme"
permalink: /5_Applications/llm-applications-10weeks/code/week06/README.html
---

# Tuần 06 — Code minh họa: Generation, re-ranking, multi-hop

| File | Chức năng | Chạy | Kết quả mong đợi |
|---|---|---|---|
| `01_reranker.py` | MMR + lexical rerank | `python 01_reranker.py` | In top-k trước/sau re-rank |
| `02_rag_pipeline.py` | retrieve → rerank → generate có trích nguồn | `python 02_rag_pipeline.py` | In câu trả lời + nguồn, hoặc "không tìm thấy" |
| `03_multi_hop.py` | Truy xuất lặp hai vòng | `python 03_multi_hop.py` | In kết quả vòng 1, thực thể, vòng 2 |

## 01_reranker.py

**Chức năng:** Sắp xếp lại kết quả bằng MMR (cân bằng relevance và diversity) và lexical similarity.

```python
{% include_relative 01_reranker.py %}
```

## 02_rag_pipeline.py

**Chức năng:** Pipeline retrieve → generate với generator mock chỉ trả lời từ context và trích nguồn.

```python
{% include_relative 02_rag_pipeline.py %}
```

## 03_multi_hop.py

**Chức năng:** Minh hoạ truy xuất nhiều vòng khi câu hỏi cần nối nhiều mảnh thông tin.

```python
{% include_relative 03_multi_hop.py %}
```
