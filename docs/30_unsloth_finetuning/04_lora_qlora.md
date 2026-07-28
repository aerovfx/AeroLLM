# Bài 4 — LoRA, QLoRA và cấu hình adapter

[← Bài 3](03_dataset_va_chat_template.md) · [Chỉ mục](index.md) · [Bài 5 →](05_sft_va_hyperparameters.md)

## Mục tiêu

- giải thích LoRA/QLoRA bằng tham số và bộ nhớ;
- chọn rank, alpha, target modules và gradient checkpointing;
- kiểm tra số tham số trainable trước training.

## Trực giác

Thay vì cập nhật ma trận trọng số lớn $W$, LoRA học cập nhật hạng thấp:

$$W' = W + \frac{\alpha}{r}BA$$

với rank $r$ nhỏ hơn nhiều kích thước của $W$. QLoRA giữ base weights ở 4-bit trong khi adapter được học ở precision phù hợp. Vì vậy checkpoint adapter nhỏ hơn đáng kể so với bản sao toàn bộ model.

## Các núm điều chỉnh

| Tham số | Vai trò | Cách bắt đầu |
|---|---|---|
| `r` | năng lực của adapter | 8 hoặc 16; tăng khi underfit đã được chứng minh |
| `lora_alpha` | scale cập nhật | thường bắt đầu gần `r` hoặc `2r`, theo notebook của model |
| `target_modules` | lớp nhận adapter | dùng danh sách notebook/model khuyến nghị; không đoán tên module |
| `lora_dropout` | regularization | bắt đầu theo notebook; chỉ tăng khi có bằng chứng overfit |
| gradient checkpointing | đổi compute lấy VRAM | bật khi context/model lớn |
| seed | khả năng tái lập | cố định và ghi lại |

## Lab ablation nhỏ

Giữ nguyên data, split, seed và training budget; chạy hai cấu hình rank (ví dụ 8 và 16). Với mỗi run ghi:

- trainable parameters và phần trăm tổng tham số;
- peak VRAM, thời gian, train/validation loss;
- metric test và 10 đánh giá định tính cố định.

Không thay đồng thời rank, learning rate và dataset vì sẽ không biết nguyên nhân khác biệt.

## Checkpoint

- [ ] Base weights không bị cập nhật ngoài ý muốn.
- [ ] Target modules tồn tại trong model.
- [ ] Số tham số trainable hợp lý và được log.
- [ ] Có lý do cho mọi thay đổi khỏi cấu hình notebook mặc định.

Nguồn: [Unsloth Fine-tuning Guide — LoRA/QLoRA](https://unsloth.ai/docs/get-started/fine-tuning-guide).
