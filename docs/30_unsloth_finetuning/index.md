# Module 30 — Fine-tuning LLM với Unsloth

[Trang chủ](../../README.md) · [Lộ trình](../../COURSE.md) · [Fine-tuning nền tảng](../07_fine_tune_pretrained_models/index.md)

Khoá thực hành 8 buổi đưa một ý tưởng fine-tuning đi trọn vòng đời: xác định mục tiêu, chọn model, thiết kế dữ liệu, QLoRA/SFT, đánh giá, lưu và triển khai.

## Thông tin khoá học

- **Đầu vào:** Python/PyTorch cơ bản; hiểu tokenization, Transformer và supervised learning.
- **Thời lượng:** 8 buổi, mỗi buổi 90–120 phút; thêm 1–2 tuần cho đồ án.
- **Môi trường:** notebook chính thức trên Colab/Kaggle hoặc Linux/WSL/Windows có GPU phù hợp.
- **Đầu ra:** adapter LoRA, báo cáo before/after, model card và một bản chạy local hoặc server.

> API, model và notebook thay đổi nhanh. Luôn mở [Fine-tuning LLMs Guide chính thức](https://unsloth.ai/docs/get-started/fine-tuning-guide) trước khi chạy và dùng notebook mới nhất do Unsloth liên kết, thay vì sao chép cứng phiên bản package từ tài liệu này.

## Chỉ mục bài học

| Buổi | Bài học | Sản phẩm |
|---:|---|---|
| 1 | [Bài toán fine-tuning và chọn phương pháp](01_bai_toan_va_phuong_phap.md) | Project brief + baseline |
| 2 | [Môi trường, GPU và chọn model](02_moi_truong_va_chon_model.md) | Notebook tải model chạy được |
| 3 | [Dataset và chat template](03_dataset_va_chat_template.md) | Dataset card + dữ liệu đã format |
| 4 | [LoRA, QLoRA và cấu hình adapter](04_lora_qlora.md) | Bảng ngân sách VRAM + cấu hình LoRA |
| 5 | [SFT và hyperparameters](05_sft_va_hyperparameters.md) | Training run có log |
| 6 | [Đánh giá và chẩn đoán lỗi](06_danh_gia.md) | Báo cáo before/after |
| 7 | [Inference, lưu và triển khai](07_luu_va_trien_khai.md) | Adapter hoặc GGUF + hướng dẫn chạy |
| 8 | [Đồ án cuối khoá](08_do_an_cuoi_khoa.md) | Demo + model card |

## Nhịp học chuẩn mỗi buổi

1. Đọc mục tiêu và khái niệm.
2. Chạy baseline trước khi thay đổi model.
3. Thực hành bằng notebook chính thức.
4. Ghi cấu hình, seed, phiên bản và số liệu.
5. Hoàn thành checkpoint cuối bài trước khi chuyển buổi.

## Nguồn chính thức

- [Fine-tuning LLMs Guide](https://unsloth.ai/docs/get-started/fine-tuning-guide)
- [Datasets Guide](https://unsloth.ai/docs/get-started/fine-tuning-llms-guide/datasets-guide)
- [Chat Templates](https://unsloth.ai/docs/basics/chat-templates)
- [Requirements](https://unsloth.ai/docs/get-started/beginner-start-here/unsloth-requirements)
- [Troubleshooting & FAQs](https://unsloth.ai/docs/basics/troubleshooting-and-faqs)

Nội dung được biên soạn theo tài liệu trên; tài liệu Unsloth là nguồn chuẩn khi có khác biệt.
