---
layout: course
title: "Readme"
permalink: /6_Interpretability/interpretability-10weeks/code/week10/README.html
---

# Tuần 10 — Code minh họa

## 01_trajectory_pca.py

**Chức năng:** Fit PCA một lần trên toàn bộ dữ liệu ghép (common space), chiếu quỹ đạo token xuống 2D và đo khoảng cách giữa cụm đúng và token sai ngữ pháp.

**Chạy:** `python 01_trajectory_pca.py`

**Kết quả mong đợi:** him/her gần nhau; token "round" tách xa cụm đúng ở tầng cuối.

```python
{% include_relative 01_trajectory_pca.py %}
```

## 02_path_length.py

**Chức năng:** Đo path length (tổng độ dài từng bước cập nhật residual) của token bình thường vs token bất thường.

**Chạy:** `python 02_path_length.py`

**Kết quả mong đợi:** Token bất thường ("surprising") có path length lớn hơn token bình thường.

```python
{% include_relative 02_path_length.py %}
```
