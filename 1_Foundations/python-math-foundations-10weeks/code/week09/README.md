---
layout: course
title: "Readme"
permalink: /1_Foundations/python-math-foundations-10weeks/code/week09/README.html
---

# Tuần 9 — Code minh họa

## 01_gradient_descent_1d.py

**Chức năng:** GD 1D cho $f(x)=(x-0.5)^2$, so sánh learning rate vừa/quá lớn/quá nhỏ.

**Chạy:** `python code/week09/01_gradient_descent_1d.py`

**Kết quả mong đợi:** `eta=0.1` hội tụ ~0.5; `eta=1.5` phân kỳ; `eta=0.001` còn xa 0.5.

```python
{% include_relative 01_gradient_descent_1d.py %}
```

## 02_gradient_descent_2d.py

**Chức năng:** GD 2D cho $f(x,y)=x^2+y^2$, so sánh learning rate cố định và động.

**Chạy:** `python code/week09/02_gradient_descent_2d.py`

**Kết quả mong đợi:** Cả hai tiến về (0, 0); in vài giá trị loss giảm dần.

```python
{% include_relative 02_gradient_descent_2d.py %}
```
