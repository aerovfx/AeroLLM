---
layout: course
title: "Readme"
permalink: /1_Foundations/python-math-foundations-10weeks/code/week03/README.html
---

# Tuần 3 — Code minh họa

## 01_functions.py

**Chức năng:** Viết hàm `double`, `average`, `max_of` có docstring, xử lý danh sách rỗng, dùng `help()`.

**Chạy:** `python code/week03/01_functions.py`

**Kết quả mong đợi:** Kết quả các hàm và nội dung docstring của `double`.

```python
{% include_relative 01_functions.py %}
```

## 02_numpy_random.py

**Chức năng:** Sinh số ngẫu nhiên tái lập được bằng `default_rng(seed)`, so sánh hai seed.

**Chạy:** `python code/week03/02_numpy_random.py` (cần `pip install numpy`)

**Kết quả mong đợi:** Hai dãy seed 42 giống nhau, dãy seed 7 khác; in trung bình/độ lệch chuẩn.

```python
{% include_relative 02_numpy_random.py %}
```
