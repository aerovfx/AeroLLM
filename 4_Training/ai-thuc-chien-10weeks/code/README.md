---
layout: course
title: "Readme"
permalink: /4_Training/ai-thuc-chien-10weeks/code/README.html
---

# Code & môi trường — AI Thực Chiến

Khoá này thiên về vận hành quy trình huấn luyện hơn là viết model từ đầu, nên phần lớn code nằm trong các notebook/script tham khảo của repo:

- Pre-training và sinh văn bản: [`src/pretrain/`](../../../src/pretrain/ch05/README.md)
- Fine-tuning và DPO: [`src/finetune/`](../../../src/finetune/ch07/README.md)
- Synthetic data & filtering: xem hướng dẫn trong [`references/round-3/synthetic-data.md`](../references/round-3/synthetic-data.md)
- Distributed training: [`references/round-3/model-training-guideline/distributed-training.md`](../references/round-3/model-training-guideline/distributed-training.md)

Kiểm tra môi trường trước khi bắt đầu:

```bash
python ../../tools/course-scripts/check_environment.py
```

> Mọi script phải chạy trên tập dữ liệu nhỏ trước, ghi log và lưu checkpoint thường xuyên để có thể rollback.
