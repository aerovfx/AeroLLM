---
layout: course
title: "Readme"
permalink: /6_Interpretability/interpretability-10weeks/code/week03/README.html
---

# Tuần 03 — Code minh họa

## 01_cosine_similarity.py

**Chức năng:** Tính ma trận cosine similarity cho nhúng có cấu trúc (động vật vs thành phố) và đối chiếu nhúng ngẫu nhiên.

**Chạy:** `python 01_cosine_similarity.py`

**Kết quả mong đợi:** Nhúng có cấu trúc cho similarity cao trong cùng cụm; nhúng ngẫu nhiên cũng tạo vài giá trị cao (tín hiệu giả).

```python
{% include_relative 01_cosine_similarity.py %}
```

## 02_analogy_arithmetic.py

**Chức năng:** Kiểm chứng `king - man + woman ~ queen` và dựng trục ngữ nghĩa tuyến tính để chiếu mọi vector.

**Chạy:** `python 02_analogy_arithmetic.py`

**Kết quả mong đợi:** Kết quả analogy gần "queen"; chiếu theo trục tách rõ nhóm nam (âm) khỏi nhóm nữ (dương).

```python
{% include_relative 02_analogy_arithmetic.py %}
```
