---
layout: course
title: "Readme"
permalink: /1_Foundations/python-math-foundations-10weeks/code/week10/README.html
---

# Tuần 10 — Code minh họa

## 01_perceptron.py

**Chức năng:** Cài đặt perceptron (dot product + bias + ReLU) và quan sát hiệu ứng phi tuyến.

**Chạy:** `python code/week10/01_perceptron.py` (cần `pip install numpy`)

**Kết quả mong đợi:** `z` và `relu(z)` cho 3 vector đầu vào giả.

```python
{% include_relative 01_perceptron.py %}
```

## 02_linear_regression_pytorch.py

**Chức năng:** Huấn luyện hồi quy tuyến tính $y=3x+1$ bằng forward/backward + autograd.

**Chạy:** `python code/week10/02_linear_regression_pytorch.py` (cần `pip install torch`)

**Kết quả mong đợi:** Loss giảm dần; `w` ~ 3 và `b` ~ 1.

```python
{% include_relative 02_linear_regression_pytorch.py %}
```
