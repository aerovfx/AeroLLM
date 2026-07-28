# Tuần 5 — Cấu hình LoRA và QLoRA / Week 5 — LoRA and QLoRA configuration

[← Tuần 4](week04.md) · [Mục lục khoá](../INDEX.md) · [40 tuần](../../WEEK_INDEX.md) · [Lịch 20 buổi](../schedule.md) · [Tuần 6 →](week06.md)

## Mục tiêu học tập / Learning objectives

- Giải thích low-rank update và QLoRA memory strategy. / Explain low-rank adaptation and QLoRA.
- Chọn rank, alpha, dropout và target modules có căn cứ. / Select adapter settings deliberately.
- Tính trainable parameters và kiểm tra module matching. / Calculate and verify trainable parameters.
- Thiết kế ablation công bằng. / Design a controlled ablation.

## Lý thuyết sâu / Deep theory

LoRA đóng băng $W\in\mathbb R^{d_{out}\times d_{in}}$ và học $\Delta W=sBA$, với $A\in\mathbb R^{r\times d_{in}}$, $B\in\mathbb R^{d_{out}\times r}$, thường $s=\alpha/r$. Trainable params mỗi matrix là $r(d_{in}+d_{out})$, nhỏ hơn $d_{in}d_{out}$ khi $r$ thấp. / LoRA constrains weight updates to a low-rank subspace.

QLoRA lượng tử base weights (thường 4-bit) nhưng adapters/compute dùng dtype cao hơn. NF4 phù hợp phân phối gần chuẩn của weights; double quantization giảm overhead quantization constants. Quantization không đồng nghĩa adapter checkpoint tự chứa base model. / An adapter depends on the exact base model and tokenizer.

Target `q_proj,v_proj` là baseline tiết kiệm; thêm k/o/up/down/gate tăng capacity và parameters. Tên module khác theo architecture nên phải inspect, không copy config mù. Rank cao không bảo đảm tốt hơn; data, LR và target modules tương tác. / Configuration must match the actual architecture.

## Buổi 1 — Adapter math và audit / Session 1 — Adapter math and audit

```python
def lora_params(d_in, d_out, r, n_modules=1):
    # Mỗi module có A shape (r,d_in) và B shape (d_out,r), tổng r*(d_in+d_out).
    # Nhân số target modules để ước lượng toàn bộ trainable adapter parameters.
    return n_modules*r*(d_in+d_out)

# Ví dụ 64 linear modules 4096→4096 với rank 16; đây chỉ là phép tính tham số.
print(lora_params(4096, 4096, 16, 64))
```

Hands-on: list named modules; chọn regex targets; inject adapters; in trainable/total ratio; assert chỉ adapter parameters `requires_grad`; lưu base revision, tokenizer và PEFT config. / Audit exactly what will train.

## Buổi 2 — QLoRA smoke run và ablation / Session 2 — Smoke run and ablation

1. Load 4-bit base với compute dtype phù hợp GPU. / Load quantized weights safely.
2. Train 20–50 steps trên subset; log loss, grad norm, tokens/s, peak VRAM. / Run a short smoke training.
3. So sánh $r=8$ với $r=16$ giữ seed/data/tokens/LR schedule. / Run one controlled rank ablation.
4. Reload adapter trong process mới và so logits/generation. / Test artifact reload.

Tham chiếu [LoRA/QLoRA nội bộ](../../../docs/30_unsloth_finetuning/04_lora_qlora.md). / Use the local detailed module.

## Câu hỏi thảo luận / Discussion questions

1. Rank biểu diễn capacity nào? / What capacity does rank represent?
2. Target nhiều modules đổi trade-off gì? / What changes when targeting more modules?
3. Vì sao adapter nhỏ vẫn cần base model đúng revision? / Why is exact base revision required?
4. Khi nào LoRA 16-bit phù hợp hơn QLoRA? / When is 16-bit LoRA preferable?
5. Ablation nào tách ảnh hưởng rank khỏi training budget? / How do we isolate rank effects?

## Bài tập về nhà / Homework

Tạo hai QLoRA configs khác đúng một biến; nộp parameter audit, memory estimate/measurement, smoke logs, validation samples, reload test và recommendation. / Compare two one-variable configurations and submit a reproducible recommendation.

## Rubric đánh giá / Assessment rubric

| Hạng mục / Criterion | Điểm |
|---|---:|
| Config/module audit đúng | 25 |
| Trainable parameter math | 20 |
| Controlled experiment | 25 |
| Memory, logs, reload test | 20 |
| Recommendation | 10 |

## ⚠️ Ngộ nhận thường gặp / Common misconceptions

- LoRA giảm activation memory về gần 0. / Activations remain significant.
- QLoRA train base weights 4-bit trực tiếp. / Base weights remain frozen.
- Copy target-module list dùng được mọi model. / Module names vary.
- Adapter file độc lập với model/tokenizer. / It is a dependent artifact.
