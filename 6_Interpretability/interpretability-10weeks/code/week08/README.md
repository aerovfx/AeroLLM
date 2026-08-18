---
layout: course
title: "Readme"
permalink: /6_Interpretability/interpretability-10weeks/code/week08/README.html
---

# Tuần 08 — Code minh họa

## 01_head_ablation.py

**Chức năng:** Zero-out từng head trước c_proj, đo logit difference (Germany − France) trên một câu tri thức giả.

**Chạy:** `python 01_head_ablation.py`

**Kết quả mong đợi:** Tắt head mang tín hiệu làm logit diff giảm rõ; các head khác ít ảnh hưởng.

```python
{% include_relative 01_head_ablation.py %}
```

## 02_head_patching_ioi.py

**Chức năng:** Vá đầu ra từng head bằng giá trị từ ngữ cảnh donor để tìm head "tên" trong tác vụ IOI.

**Chạy:** `python 02_head_patching_ioi.py`

**Kết quả mong đợi:** Vá head tên (head 3) làm dự đoán lật sang Barbara; head nhiễu không đổi.

```python
{% include_relative 02_head_patching_ioi.py %}
```
