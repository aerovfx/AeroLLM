---
layout: course
title: "Readme"
permalink: /6_Interpretability/interpretability-10weeks/code/week04/README.html
---

# Tuần 04 — Code minh họa

## 01_activation_maximization.py

**Chức năng:** Tối ưu đầu vào bằng gradient ascent để cực đại hoá một neuron, rồi so đầu vào tối ưu với đặc trưng thật.

**Chạy:** `python 01_activation_maximization.py`

**Kết quả mong đợi:** Đầu vào tối ưu xoay về hướng đặc trưng (cosine similarity gần 1).

```python
{% include_relative 01_activation_maximization.py %}
```

## 02_neuron_selectivity.py

**Chức năng:** Đo tính chọn lọc của một neuron giữa hai nhóm bằng hồi quy logistic và t-test, đối chiếu hai kết luận.

**Chạy:** `python 02_neuron_selectivity.py`

**Kết quả mong đợi:** Logistic cho accuracy cao; t-test cho p-value rất nhỏ (khác biệt có ý nghĩa).

```python
{% include_relative 02_neuron_selectivity.py %}
```
