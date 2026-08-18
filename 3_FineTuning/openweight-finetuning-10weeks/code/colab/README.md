---
layout: course
title: "Readme"
permalink: /3_FineTuning/openweight-finetuning-10weeks/code/colab/README.html
---

# Colab workflow — Fine-tuning open-weight

1. Mở notebook hiện hành từ [Unsloth Fine-tuning Guide](https://unsloth.ai/docs/get-started/fine-tuning-guide); API/model support thay đổi nên không pin cell cài đặt cũ trong khoá học.
2. Chọn GPU runtime, chạy cell kiểm tra GPU/VRAM trước khi tải model.
3. Copy kết quả từ [`qlora_planning_lab.ipynb`](../notebooks/qlora_planning_lab.ipynb) vào project brief.
4. Lưu Hugging Face/W&B token bằng **Colab Secrets**, không ghi trực tiếp trong cell.
5. Chạy 20–60 step smoke test, kiểm tra template/labels/checkpoint rồi mới tăng budget.
6. Download adapter, config, tokenizer, metrics và model card; không chỉ lưu notebook state.

Máy không có GPU vẫn hoàn thành tuần 1–4 và 7 bằng các script audit/planning/evaluation cục bộ.
