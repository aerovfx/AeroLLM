---
layout: course
title: "Readme"
permalink: /5_Applications/llm-applications-10weeks/code/week01/README.html
---

# Tuần 01 — Code minh họa: Metric & bẫy

| File | Chức năng | Chạy | Kết quả mong đợi |
|---|---|---|---|
| `01_metrics.py` | Confusion matrix, precision/recall/F1, bẫy imbalance | `python 01_metrics.py` | Accuracy của "baseline đa số" ~0.90 nhưng F1 = 0 |
| `02_calibration.py` | Softmax ổn định, log-prob, perplexity | `python 02_calibration.py` | Tổng softmax = 1; model tự tin có PPL thấp |

## 01_metrics.py

**Chức năng:** Nhận nhãn thật + nhãn dự đoán giả, trả confusion matrix và các metric; so sánh model A với baseline đa số để lộ bẫy accuracy.

```python
{% include_relative 01_metrics.py %}
```

## 02_calibration.py

**Chức năng:** Tính softmax ổn định (trừ max trước khi exp) và perplexity từ danh sách xác suất.

```python
{% include_relative 02_calibration.py %}
```
