# Bài 5 — SFT và hyperparameters

[← Bài 4](04_lora_qlora.md) · [Chỉ mục](index.md) · [Bài 6 →](06_danh_gia.md)

## Mục tiêu

- cấu hình một run ngắn để kiểm tra pipeline trước full run;
- hiểu effective batch size, learning rate, steps/epochs và sequence length;
- đọc loss mà không coi loss là metric chất lượng duy nhất.

## Quy trình hai run

### 1. Smoke test

Chạy khoảng vài chục step trên một phần nhỏ dữ liệu để xác nhận:

- batch có token/label đúng;
- loss hữu hạn và có xu hướng giảm;
- checkpoint có thể lưu/nạp;
- inference sau training không hỏng template.

### 2. Full run

Chỉ chạy sau khi smoke test đạt. Hướng dẫn Unsloth dùng các giá trị khởi đầu như batch/device nhỏ, gradient accumulation để tạo effective batch lớn hơn, và 1–3 epoch để hạn chế overfit. Đây là baseline, không phải quy luật cho mọi dataset.

$$\text{effective batch} = \text{batch/device} \times \text{gradient accumulation} \times \text{số GPU}$$

## Nhật ký thí nghiệm tối thiểu

```text
run_id, model_revision, dataset_revision, split_hash
chat_template, max_seq_length, precision
lora_r, lora_alpha, target_modules
batch_size, grad_accumulation, learning_rate, epochs/steps
seed, peak_vram, wall_time
train_loss, validation_loss, task_metrics
```

## Chẩn đoán nhanh

| Hiện tượng | Kiểm tra trước |
|---|---|
| OOM | context, batch/device, gradient checkpointing, model size |
| Loss không giảm | format/labels, learning rate, data quality |
| Loss về gần 0 | leakage, duplicates, dataset quá nhỏ, quá nhiều epoch |
| Train tốt, validation xấu | overfit hoặc split lệch phân phối |
| Output lặp/rác | chat template, EOS, truncation, learning rate |

## Checkpoint

- [ ] Smoke test hoàn tất trước full run.
- [ ] Có validation loss và metric tác vụ.
- [ ] Có thể tái lập cấu hình từ log.
- [ ] Không chọn checkpoint chỉ vì train loss thấp nhất.

Nguồn: [Unsloth Fine-tuning Guide — Training + Evaluation](https://unsloth.ai/docs/get-started/fine-tuning-guide), [Troubleshooting](https://unsloth.ai/docs/basics/troubleshooting-and-faqs).
