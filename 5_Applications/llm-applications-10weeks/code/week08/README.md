---
layout: course
title: "Readme"
permalink: /5_Applications/llm-applications-10weeks/code/week08/README.html
---

# Tuần 08 — Code minh họa: Bias & threat model

| File | Chức năng | Chạy | Kết quả mong đợi |
|---|---|---|---|
| `01_bias_metrics.py` | Demographic parity + counterfactual gap | `python 01_bias_metrics.py` | In chênh lệch dự đoán giữa nhóm và gap counterfactual |
| `02_threat_model.py` | Risk = likelihood × impact | `python 02_threat_model.py` | In bảng rủi ro xếp hạng giảm dần |

## 01_bias_metrics.py

**Chức năng:** Đo chênh lệch tỷ lệ dự đoán dương giữa các nhóm và chênh lệch qua cặp prompt đối xứng.

```python
{% include_relative 01_bias_metrics.py %}
```

## 02_threat_model.py

**Chức năng:** Chấm điểm rủi ro (likelihood × impact) cho các mối đe dọa và xếp hạng ưu tiên.

```python
{% include_relative 02_threat_model.py %}
```
