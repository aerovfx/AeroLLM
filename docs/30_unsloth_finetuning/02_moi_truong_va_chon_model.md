# Bài 2 — Môi trường, GPU và chọn model

[← Bài 1](01_bai_toan_va_phuong_phap.md) · [Chỉ mục](index.md) · [Bài 3 →](03_dataset_va_chat_template.md)

## Mục tiêu

- chọn model theo task, license, ngôn ngữ, context và ngân sách VRAM;
- tải model lượng tử hoá phù hợp;
- xác nhận inference baseline trước khi gắn adapter.

## Quy trình chọn model

1. **Task fit:** text, vision, embedding, audio hay reasoning?
2. **Instruct hay base:** người mới nên dùng instruct model cho hội thoại/SFT; base model cần nhiều dữ liệu và định dạng cẩn thận hơn.
3. **Kích thước:** bắt đầu bằng model nhỏ nhất có baseline hợp lý.
4. **License và quyền truy cập:** kiểm tra trước khi tải hoặc phân phối derivative.
5. **Context:** thử `max_seq_length=2048` trước; context dài làm tăng chi phí bộ nhớ.
6. **Precision:** QLoRA 4-bit là baseline tiết kiệm; chỉ đổi sau khi đo.

Tên model có hậu tố `unsloth-bnb-4bit` là dynamic 4-bit quant của Unsloth; `bnb-4bit` là BitsAndBytes 4-bit tiêu chuẩn. Đây là quy ước có thể thay đổi, nên kiểm tra model card hiện hành.

## Lab môi trường

- Mở một notebook được liên kết từ tài liệu chính thức; tạo bản sao riêng.
- Ghi GPU, VRAM, Python, CUDA và phiên bản các package vào đầu notebook.
- Chạy cell tải model/tokenizer với `max_seq_length`, `dtype` và `load_in_4bit` được ghi rõ.
- Sinh câu trả lời cho bộ baseline của Bài 1.
- Ghi peak VRAM, thời gian tải và tốc độ sinh tương đối.

## Quy tắc an toàn vận hành

- Không đưa token Hugging Face/W&B vào notebook commit công khai.
- Không cài package từ nguồn không kiểm chứng.
- Không tiếp tục training nếu tokenizer/chat template không khớp model.
- Chỉ bật một chế độ tải/training (4-bit, 8-bit, 16-bit hoặc full fine-tuning) tại một thời điểm.

## Checkpoint

- [ ] Model sinh được trước training.
- [ ] Prompt dùng đúng chat template của model.
- [ ] Cấu hình và peak VRAM được ghi lại.
- [ ] License/model card đã được đọc.

Nguồn: [Unsloth Fine-tuning Guide — phần chọn model và cài đặt](https://unsloth.ai/docs/get-started/fine-tuning-guide), [Requirements](https://unsloth.ai/docs/get-started/beginner-start-here/unsloth-requirements).
