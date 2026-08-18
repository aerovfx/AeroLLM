---
layout: course
title: "Week06"
permalink: /3_FineTuning/openweight-finetuning-10weeks/lessons/week06.html
---

# Tuần 06 — SFT và siêu tham số / SFT and hyperparameters

[← Tuần 5](week05.md) · [Mục lục khoá](../INDEX.md) · [40 tuần](../../../courses/WEEK_INDEX.md) · [Lịch 20 buổi](../schedule.md) · [Tuần 7 →](week07.md)

## Mục tiêu học tập / Learning objectives

- Thiết kế objective SFT và completion-only masking đúng / design SFT and completion-only masking correctly.
- Chọn LR, batch token, epoch, sequence length và LoRA rank / choose LR, token batch, epochs, sequence length, and LoRA rank.
- Chạy pilot có baseline, logging và stop criteria / run a controlled pilot with logging and stop criteria.
- Phân biệt underfitting, overfitting và lỗi formatting / distinguish underfitting, overfitting, and formatting failures.

## Lý thuyết sâu / Deep theory

SFT cực đại hoá likelihood của câu trả lời mục tiêu: $\mathcal L=-\sum_t m_t\log p_\theta(y_t|x,y_{<t})$, với $m_t=1$ cho token cần học. Completion-only masking tránh phạt model vì prompt do người dùng cung cấp. LoRA cập nhật $W'=W+sBA$, $s=\alpha/r$ (hoặc biến thể rsLoRA); rank kiểm soát capacity nhưng không đảm bảo chất lượng đơn điệu.

Token budget mỗi update = `micro_batch × seq_len thực × accumulation × world_size`. Với packing, số sequence không còn đại diện đúng lượng dữ liệu; cần log non-padding tokens. LR quá cao gây quên và format collapse; quá thấp tạo adapter gần như không học.

Tham khảo local: [Module Unsloth](../../../docs/30_unsloth_finetuning/index.md) và [fine-tuning nền tảng](../../../docs/07_fine_tune_pretrained_models/index.md).

**Unsloth defaults:** `gradient_accumulation_steps=4` (mô phỏng batch lớn không tăng VRAM), `max_steps=60` để chạy nhanh hoặc `num_train_epochs=1` (1–3 epochs), LR khởi điểm `2e-4` rồi thử `1e-4`/`5e-5`/`2e-5`. Đọc loss: ~0.5–1.0 thường tốt; loss về 0 nghi ngờ overfitting. Chi tiết: [Công nghệ Unsloth](../references/unsloth-technology.md).

## Buổi 1 — Objective và cấu hình / Session 1 — Objective and configuration

```python
from trl import SFTConfig  # Cấu hình trainer cho supervised fine-tuning.

args = SFTConfig(
    output_dir="runs/sft-pilot",  # Thư mục checkpoint/log; nên gắn run_id riêng.
    learning_rate=2e-4,  # Điểm khởi đầu cho LoRA, không phải mặc định tối ưu mọi task.
    per_device_train_batch_size=2,  # Số sequence/GPU/micro-step.
    gradient_accumulation_steps=8,  # Tích gradient 8 lần trước optimizer.step.
    num_train_epochs=1,  # Một lượt qua train set để tạo baseline chống overfit.
    warmup_ratio=0.05,  # 5% update đầu tăng LR từ nhỏ lên peak.
    max_length=2048,  # Giới hạn token sau template; cần audit truncation.
    logging_steps=5,  # Ghi metric mỗi 5 optimizer steps.
    eval_strategy="steps",  # Đánh giá theo số step thay vì chỉ cuối epoch.
    eval_steps=50,  # Tần suất validation; nhỏ hơn làm chậm nhưng quan sát dày hơn.
    save_strategy="steps",  # Lưu checkpoint theo step để có thể resume/chọn model.
    save_steps=50,  # Đồng bộ với eval giúp gắn checkpoint với metric.
    bf16=True,  # Chỉ bật trên GPU hỗ trợ bfloat16; nếu không cần cấu hình khác.
)
```

Giá trị trên là điểm khởi đầu, không phải “best defaults”. Batch hiệu dụng phải báo bằng tokens; sequence dài làm attention memory tăng gần bậc hai nếu không dùng kernel tối ưu.

### Hands-on có hướng dẫn / Guided hands-on

1. Render 20 examples bằng đúng chat template; decode lại và kiểm tra role/EOS.
2. Trực quan hoá labels: prompt phải là `-100`, assistant phải có target tokens.
3. Chạy 30-step overfit trên 32 examples; model phải học format và giảm loss.
4. Chạy pilot 200 steps với eval định kỳ; lưu config, seed, data hash và adapter.

## Buổi 2 — Tuning và chẩn đoán / Session 2 — Tuning and diagnosis

Thiết kế ma trận nhỏ: LR `{5e-5, 2e-4}`, rank `{8, 32}`, cùng token budget. Metric gồm validation NLL trên response tokens, format pass rate, task accuracy và memory. Early stopping chỉ dựa một metric có thể bỏ lỡ trade-off.

```python
def trainable_ratio(model):
    # Chỉ đếm parameters có requires_grad=True, thường là LoRA adapters.
    trainable = sum(p.numel() for p in model.parameters() if p.requires_grad)
    # Tổng gồm base model frozen và adapter trainable.
    total = sum(p.numel() for p in model.parameters())
    # Trả số tuyệt đối và tỷ lệ phần trăm để audit cấu hình PEFT.
    return trainable, total, 100 * trainable / total
```

### Lab / Hands-on lab

- Kiểm tra chỉ adapter (và modules được chủ ý chọn) có gradient.
- So sánh base, pilot và tuned trên cùng 30 prompts đóng băng.
- Plot train/eval loss theo tokens, không chỉ theo steps.
- Ghi failure taxonomy: format, refusal, hallucination, incompleteness, language drift.

## Chính xác 5 câu hỏi thảo luận / Exactly 5 discussion questions

1. Khi nào nên tính loss trên prompt tokens? / When should prompt tokens contribute to loss?
2. Vì sao epoch không phải budget công bằng khi packing khác nhau? / Why are epochs unfair across packing schemes?
3. Rank LoRA cao có thể làm hại tổng quát hoá thế nào? / How can high LoRA rank hurt generalization?
4. Tín hiệu nào phân biệt format bug với underfitting? / What distinguishes a formatting bug from underfitting?
5. Khi validation loss giảm nhưng task score giảm, nên điều tra gì? / What should be investigated when validation loss improves but task score falls?

## Bài tập về nhà / Homework

Fine-tune một open-weight model nhỏ với completion-only loss. Nộp audit 30 examples, pilot, ma trận 2×2 LR/rank cùng token budget, logs, adapter và bảng base-vs-final. Viết quyết định chọn cấu hình dựa trên ít nhất ba metric và chi phí.

## Rubric đánh giá / Assessment rubric

| Tiêu chí / Criterion | Điểm / Points |
|---|---:|
| Template/mask đúng / Correct template and mask | 25 |
| Thiết kế tuning công bằng / Fair tuning design | 25 |
| Logging và reproducibility / Logging and reproducibility | 20 |
| Evaluation và error analysis / Evaluation and errors | 20 |
| Lập luận kỹ thuật / Technical reasoning | 10 |

## ⚠️ Hiểu lầm thường gặp / Common misconceptions

- Training loss thấp không chứng minh model hữu ích / Low training loss is insufficient.
- `max_length` không có nghĩa mọi sample dùng đủ length / Max length is not actual tokens.
- Packing không được làm trộn loss qua ranh giới sai / Packing must preserve boundaries/masks.
- Adapter nhỏ vẫn có thể overfit / Small adapters can overfit.
