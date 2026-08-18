---
layout: course
title: "Readme"
permalink: /6_Interpretability/interpretability-10weeks/code/week06/README.html
---

# Tuần 06 — Code minh họa

## 01_activation_editing.py

**Chức năng:** So sánh các chế độ sửa kích hoạt (zero/mean/median/noise) lên một neuron mạch, đo logit difference so với baseline.

**Chạy:** `python 01_activation_editing.py`

**Kết quả mong đợi:** zero/mean/median làm logit diff giảm mạnh (mất ưu thế nhãn A); noise làm nhiễu quanh baseline.

```python
{% include_relative 01_activation_editing.py %}
```

## 02_counterfactual_patching.py

**Chức năng:** Vá hidden state từ ngữ cảnh nguồn vào đích tại từng tầng, quan sát dự đoán "lật" sang đáp án nguồn.

**Chạy:** `python 02_counterfactual_patching.py`

**Kết quả mong đợi:** Vá ở tầng sâu làm dự đoán lật mạnh hơn tầng nông.

```python
{% include_relative 02_counterfactual_patching.py %}
```
