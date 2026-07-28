# Code lab — Fine-tuning open-weight

[Khoá học](../INDEX.md) · [Cấu hình máy](../../COMPUTER_REQUIREMENTS.md)

| Tuần | Code | Mục tiêu |
|---:|---|---|
| 1–3 | [`python/dataset_audit.py`](python/dataset_audit.py) | Schema, duplicate, split và provenance audit |
| 2, 5 | [`python/lora_vram_planner.py`](python/lora_vram_planner.py) | Ước lượng weights/adapter và chọn cấu hình |
| 4–7 | [`notebooks/qlora_planning_lab.ipynb`](notebooks/qlora_planning_lab.ipynb) | Dataset → token budget → LoRA → evaluation |
| 5–9 | [`python/unsloth_sft_template.py`](python/unsloth_sft_template.py) | Template có dry-run; chỉ train khi chủ động bật `--run` |
| 5–10 | [`colab/README.md`](colab/README.md) | Cách chọn notebook/GPU và bảo vệ credential |

Các script planning/audit chạy bằng standard library. Template Unsloth không tự tải model ở chế độ mặc định.
