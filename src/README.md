# Chỉ mục mã nguồn và notebook thực hành

[Trang chủ](../README.md) · [Lộ trình](../COURSE.md) · [Bài giảng](../docs/index.md)

## Chuẩn bị môi trường

- [Tổng quan cài đặt](utils/setup/README.md)
- [Cài thư viện Python](utils/setup/02_installing-python-libraries/README.md)
- Tuỳ chọn: [Docker](utils/setup/03_optional-docker-environment/README.md), [AWS SageMaker](utils/setup/04_optional-aws-sagemaker-notebook/README.md)

## Tokenization và data pipeline

- [Chỉ mục tokenizer](tokenizer/ch08/README.md)
- [Main notebook và data loader](tokenizer/ch08/01_main-chapter-code/README.md)
- [Byte Pair Encoding](tokenizer/ch08/02_bonus_bytepair-encoder/README.md)
- [Embedding so với matrix multiplication](tokenizer/ch08/03_bonus_embedding-vs-matmul/README.md)
- [Trực giác data loader](tokenizer/ch08/04_bonus_dataloader-intuition/README.md)
- [BPE from scratch](tokenizer/ch08/05_bpe-from-scratch/README.md)

## Xây GPT và pre-training

1. [Attention và multi-head attention](pretrain/ch03/README.md)
2. [Cài đặt GPT](pretrain/ch04/README.md)
3. [Training, nạp trọng số và inference](pretrain/ch05/README.md)

Các thí nghiệm mở rộng nằm trong thư mục con tương ứng: performance analysis, scheduler, hyperparameter tuning, Gutenberg, GPT↔Llama, tokenizer và memory-efficient loading.

## Fine-tuning và alignment

- [Classification fine-tuning](finetune/ch06/README.md)
- [Instruction fine-tuning](finetune/ch07/README.md)
- [Dataset utilities](finetune/ch07/02_dataset-utilities/README.md)
- [Model evaluation](finetune/ch07/03_model-evaluation/README.md)
- [Preference tuning với DPO](finetune/ch07/04_preference-tuning-with-dpo/README.md)
- [Sinh dữ liệu](finetune/ch07/05_dataset-generation/README.md)

Thư mục `finetune/ch02/` chứa các notebook thử nghiệm R1, Hugging Face và chuẩn bị dữ liệu; dùng như tài liệu mở rộng, không phải phần bắt buộc.

## Công cụ trực quan

- `llm/`: visualizer Transformer/MoE dùng bởi ứng dụng Next.js.
- `app/`: các route của ứng dụng.
- `cpu/`, `fluidsim/`: demo kỹ thuật bổ trợ, ngoài lộ trình LLM cốt lõi.

## Phụ lục

- `utils/appendix-A/`: PyTorch và distributed training.
- `utils/appendix-D/`: bổ sung training.
- `utils/appendix-E/`: LoRA.
