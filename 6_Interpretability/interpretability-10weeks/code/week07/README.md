---
layout: course
title: "Readme"
permalink: /6_Interpretability/interpretability-10weeks/code/week07/README.html
---

# Tuần 07 — Code minh họa

## 01_activation_patching_ioi.py

**Chức năng:** Vá hidden state từ donor vào recipient tại từng tầng trên tác vụ IOI, quan sát chuyển pha (tầng sớm kháng nhiễu, tầng sau nhạy cảm).

**Chạy:** `python 01_activation_patching_ioi.py`

**Kết quả mong đợi:** Vá trước tầng tích hợp bị "rửa trôi" (vẫn Bob); vá sau tầng tích hợp làm lật sang Barbara.

```python
{% include_relative 01_activation_patching_ioi.py %}
```

## 02_skip_layer.py

**Chức năng:** Bỏ từng tầng (nối residual thẳng) và đo độ lệch output so với baseline đầy đủ.

**Chạy:** `python 02_skip_layer.py`

**Kết quả mong đợi:** Bỏ tầng quan trọng (tầng 4) gây lệch lớn nhất.

```python
{% include_relative 02_skip_layer.py %}
```
