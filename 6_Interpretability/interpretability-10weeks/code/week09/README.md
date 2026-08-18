---
layout: course
title: "Readme"
permalink: /6_Interpretability/interpretability-10weeks/code/week09/README.html
---

# Tuần 09 — Code minh họa

## 01_median_replacement.py

**Chức năng:** Thay top-p% neuron mạnh nhất bằng trung vị tầng, quét p (ripple-rate) để thấy hiệu ứng ngưỡng.

**Chạy:** `python 01_median_replacement.py`

**Kết quả mong đợi:** p nhỏ (0.2–1%) mới có biến thiên lớn; từ ~1% trở lên logit về gần 0 và gần như phẳng.

```python
{% include_relative 01_median_replacement.py %}
```

## 02_subspace_removal.py

**Chức năng:** Loại bỏ một hướng (subspace) khỏi kích hoạt, so sánh tác động giữa hướng ngữ nghĩa và hướng nhiễu.

**Chạy:** `python 02_subspace_removal.py`

**Kết quả mong đợi:** Loại bỏ hướng ngữ nghĩa làm logit sụp đổ; loại bỏ hướng nhiễu gần như không đổi.

```python
{% include_relative 02_subspace_removal.py %}
```
