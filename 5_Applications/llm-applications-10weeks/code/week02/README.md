---
layout: course
title: "Readme"
permalink: /5_Applications/llm-applications-10weeks/code/week02/README.html
---

# Tuần 02 — Code minh họa: Benchmark & bộ dữ liệu

| File | Chức năng | Chạy | Kết quả mong đợi |
|---|---|---|---|
| `01_hellaswag_scoring.py` | Chấm điểm MCQ bằng log-likelihood chuẩn hoá độ dài | `python 01_hellaswag_scoring.py` | In dự đoán từng câu, accuracy và baseline 0.25 |
| `02_benchmark_builder.py` | Sinh bộ benchmark tổng hợp có nhãn + metadata | `python 02_benchmark_builder.py` | In phân bố chủ đề, baseline 0.25, ghi `benchmark_fake.json` |

## 01_hellaswag_scoring.py

**Chức năng:** Nhận bộ MCQ giả (context + 4 lựa chọn), tính điểm chuẩn hoá độ dài và chọn đáp án; so sánh với baseline ngẫu nhiên.

```python
{% include_relative 01_hellaswag_scoring.py %}
```

## 02_benchmark_builder.py

**Chức năng:** Sinh 20 câu benchmark giả theo 4 chủ đề, gán độ khó và đáp án, ghi JSON.

```python
{% include_relative 02_benchmark_builder.py %}
```
