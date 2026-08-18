---
layout: course
title: "Readme"
permalink: /5_Applications/llm-applications-10weeks/code/week03/README.html
---

# Tuần 03 — Code minh họa: Eval harness & phân tích lỗi

| File | Chức năng | Chạy | Kết quả mong đợi |
|---|---|---|---|
| `01_eval_harness.py` | Harness tách dataset/model/metric; 3 model giả | `python 01_eval_harness.py` | In accuracy của random/majority/heuristic |
| `02_error_analysis.py` | Bootstrap CI + error buckets | `python 02_error_analysis.py` | In accuracy kèm CI 95% và bảng lỗi theo category |

## 01_eval_harness.py

**Chức năng:** Sinh dataset giả và chạy 3 model (random, đa số, heuristic) qua cùng một harness; so sánh với baseline.

```python
{% include_relative 01_eval_harness.py %}
```

## 02_error_analysis.py

**Chức năng:** Ước lượng khoảng tin cậy 95% bằng bootstrap và nhóm lỗi theo category để biết nên sửa gì.

```python
{% include_relative 02_error_analysis.py %}
```
