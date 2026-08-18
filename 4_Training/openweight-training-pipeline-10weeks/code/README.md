---
layout: course
title: "Readme"
permalink: /4_Training/openweight-training-pipeline-10weeks/code/README.html
---

# Code lab — Pipeline training open-weight

[Khoá học](../INDEX.md) · [Cấu hình máy](../../../courses/COMPUTER_REQUIREMENTS.md)

| Tuần | Code | Mục tiêu |
|---:|---|---|
| 1 | [`python/capacity_planner.py`](python/capacity_planner.py) | FLOPs, thời gian, disk và go/no-go |
| 2–3 | [`python/governance_audit.py`](python/governance_audit.py) | License/PII/lineage release gates |
| 1–10 | [`notebooks/training_pipeline_lab.ipynb`](notebooks/training_pipeline_lab.ipynb) | Stage-gate walkthrough không cần GPU |
| 7 | [`cpp/shard_manifest.cpp`](cpp/shard_manifest.cpp) | Kiểm tra shard manifest bằng C++17 |
| 5–10 | [`colab/README.md`](colab/README.md) | Reduced experiments và giới hạn Colab |

Các ví dụ mặc định là planning/audit; không tự khởi chạy distributed training hoặc DeepSpec.
