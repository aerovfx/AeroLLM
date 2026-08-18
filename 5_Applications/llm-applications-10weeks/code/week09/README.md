---
layout: course
title: "Readme"
permalink: /5_Applications/llm-applications-10weeks/code/week09/README.html
---

# Tuần 09 — Code minh họa: Guardrails & red team

| File | Chức năng | Chạy | Kết quả mong đợi |
|---|---|---|---|
| `01_guardrails.py` | Filter đầu vào/đầu ra + phát hiện injection | `python 01_guardrails.py` | In quyết định ALLOW/BLOCK cho từng mẫu |
| `02_red_team.py` | Bộ mẫu tấn công giả định + block rate | `python 02_red_team.py` | In block rate và false positive rate |

## 01_guardrails.py

**Chức năng:** Cài guardrail đầu vào (denylist + phát hiện injection) và đầu ra (chặn nội dung cấm).

```python
{% include_relative 01_guardrails.py %}
```

## 02_red_team.py

**Chức năng:** Đo hiệu quả guardrail bằng tỷ lệ chặn đúng tấn công và chặn nhầm câu vô hại.

```python
{% include_relative 02_red_team.py %}
```
