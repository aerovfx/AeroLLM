---
layout: course
title: "Readme"
permalink: /6_Interpretability/interpretability-10weeks/code/week01/README.html
---

# Tuần 01 — Code minh họa

## 01_residual_stream.py

**Chức năng:** Sinh embedding giả có seed, mô phỏng 4 block cập nhật residual stream (attention + MLP giả), in độ "trôi" của vector token so với trạng thái đầu.

**Chạy:** `python 01_residual_stream.py`

**Kết quả mong đợi:** Giá trị drift tăng dần qua các block (vector token được "làm giàu" ngữ cảnh dần).

```python
{% include_relative 01_residual_stream.py %}
```

## 02_linear_probe_baseline.py

**Chức năng:** So sánh một mô hình tuyến tính (diễn giải được) với một mô hình phi tuyến (hộp đen) bằng cách fit hồi quy tuyến tính lên cả hai.

**Chạy:** `python 02_linear_probe_baseline.py`

**Kết quả mong đợi:** Probe khớp tốt mô hình tuyến tính (R² cao, hệ số ≈ 2.5) nhưng thất bại trên mô hình phi tuyến (R² thấp).

```python
{% include_relative 02_linear_probe_baseline.py %}
```
