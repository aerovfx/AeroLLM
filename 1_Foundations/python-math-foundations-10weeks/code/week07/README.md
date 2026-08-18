---
layout: course
title: "Readme"
permalink: /1_Foundations/python-math-foundations-10weeks/code/week07/README.html
---

# Tuần 7 — Code minh họa

## 01_classes_objects.py

**Chức năng:** Định nghĩa lớp `Student` với `__init__` và phương thức `passed()`, tạo đối tượng.

**Chạy:** `python code/week07/01_classes_objects.py`

**Kết quả mong đợi:** Thông tin và trạng thái đạt/không đạt của hai sinh viên.

```python
{% include_relative 01_classes_objects.py %}
```

## 02_tensor_basics.py

**Chức năng:** Tạo tensor, đọc shape/dtype, `reshape`, sinh ngẫu nhiên có seed, truy cập phần tử.

**Chạy:** `python code/week07/02_tensor_basics.py` (cần `pip install torch`)

**Kết quả mong đợi:** Tensor, shape/dtype, tensor đổi hình, 3 số ngẫu nhiên seed 42.

```python
{% include_relative 02_tensor_basics.py %}
```
