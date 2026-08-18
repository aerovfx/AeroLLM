---
layout: course
title: "Readme"
permalink: /6_Interpretability/interpretability-10weeks/code/week02/README.html
---

# Tuần 02 — Code minh họa

## 01_sparse_probe.py

**Chức năng:** Huấn luyện hồi quy logistic phạt L1 (proximal gradient descent) để tìm tập neuron tối thiểu phân loại được dữ liệu giả.

**Chạy:** `python 01_sparse_probe.py`

**Kết quả mong đợi:** Chỉ vài neuron "sống sót" (hệ số ≠ 0), trùng hoặc gần với 3 neuron thật đã cấy, độ chính xác cao.

```python
{% include_relative 01_sparse_probe.py %}
```

## 02_sae_toy.py

**Chức năng:** Huấn luyện sparse autoencoder tuyến tính (encoder ReLU + decoder) để khôi phục các hướng feature thưa từ biểu diễn dày đặc.

**Chạy:** `python 02_sae_toy.py`

**Kết quả mong đợi:** Cosine similarity giữa feature học được và feature thật gần 1 (sau khi ghép theo hướng gần nhất).

```python
{% include_relative 02_sae_toy.py %}
```
