---
layout: course
title: "Readme"
permalink: /6_Interpretability/interpretability-10weeks/code/week05/README.html
---

# Tuần 05 — Code minh họa

## 01_effective_dimensionality.py

**Chức năng:** Tính số chiều hiệu quả (participation ratio) từ phổ giá trị riêng PCA ở mỗi tầng.

**Chạy:** `python 01_effective_dimensionality.py`

**Kết quả mong đợi:** Tầng đầu (nhiễu) có chiều hiệu quả cao; càng sâu càng giảm khi biểu diễn nén về ít chiều chính.

```python
{% include_relative 01_effective_dimensionality.py %}
```

## 02_logit_lens.py

**Chức năng:** Nhân hidden state mỗi tầng với ma trận unembedding để xem token dự đoán "hiện dần" ra sao.

**Chạy:** `python 02_logit_lens.py`

**Kết quả mong đợi:** Tầng đầu dự đoán ngẫu nhiên, tầng cuối hội tụ về token mục tiêu (3).

```python
{% include_relative 02_logit_lens.py %}
```
