---
layout: course
title: "Week02"
permalink: /3_FineTuning/openweight-finetuning-10weeks/lessons/week02.html
---

# Tuần 2 — Model, giấy phép và phần cứng / Week 2 — Model, license, and hardware

[← Tuần 1](week01.md) · [Mục lục khoá](../INDEX.md) · [40 tuần](../../../courses/WEEK_INDEX.md) · [Lịch 20 buổi](../schedule.md) · [Tuần 3 →](week03.md)

## Mục tiêu học tập / Learning objectives

- Chọn base/instruct model theo task, ngôn ngữ, context và ecosystem. / Select a model by task and operational fit.
- Đọc model card/license và ghi nhận nghĩa vụ phân phối. / Read model cards and licenses.
- Ước tính memory cho inference, LoRA và QLoRA. / Estimate memory needs.
- Thực hiện smoke test trước training. / Run a pre-training smoke test.

## Lý thuyết sâu / Deep theory

Memory weights xấp xỉ $P\times b/8$ bytes. Full Adam training còn gradients, master weights và hai moment, thường lớn hơn nhiều lần weights. QLoRA giữ base 4-bit, dequantize khi compute và train adapter nhỏ; peak memory vẫn gồm activations, KV/temporary buffers và allocator overhead. / Quantization reduces base-weight storage but not every memory component.

Activation memory tăng theo batch, sequence, layers và hidden width; gradient checkpointing đổi compute lấy memory. Context công bố không có nghĩa hardware chịu được context đó khi training. / Published context length is not a memory guarantee.

License review gồm: quyền commercial/research, attribution, acceptable-use restrictions, redistribution, derivatives, jurisdiction và license của dataset/code tách biệt. Đây là checklist kỹ thuật, không thay thế tư vấn pháp lý. / Model, code, and dataset licenses must be reviewed separately.

## Buổi 1 — Model scorecard / Session 1 — Model scorecard

Lập scorecard có trọng số: task baseline 30%, Việt/Anh 15%, license 20%, memory 15%, context 10%, tooling 10%. Ghi chính xác revision, tokenizer revision, dtype và trust-remote-code decision. / Build a weighted scorecard and pin revisions.

```python
def weight_gib(params_b, bits):
    # params_b tính theo tỷ tham số; nhân 1e9 để đổi sang số scalar weights.
    # Mỗi weight chiếm bits/8 byte; chia 2**30 để đổi byte thành GiB.
    return params_b * 1e9 * bits / 8 / 2**30

# Ước lượng riêng dung lượng weights của model 7B ở 16/8/4 bit.
# Con số chưa gồm activation, KV cache, gradient, optimizer và runtime overhead.
for b in (16, 8, 4):
    print(b, round(weight_gib(7, b), 2))
```

## Buổi 2 — Capacity plan và smoke test / Session 2 — Capacity plan and smoke test

1. Đo free VRAM và software versions; không dựa duy nhất vào ước tính. / Record hardware and software.
2. Load model ở intended precision; kiểm tra tokenizer/template. / Load at intended precision.
3. Chạy forward/backward một microbatch và ghi peak allocated/reserved. / Run one forward/backward pass.
4. Chọn batch, sequence, accumulation và headroom ≥10–15%. / Select settings with headroom.

Tham chiếu [môi trường và chọn model](../../../docs/30_unsloth_finetuning/02_moi_truong_va_chon_model.md). / Consult the local Unsloth module.

## Câu hỏi thảo luận / Discussion questions

1. Model lớn hơn khi nào thua model nhỏ hơn? / When can a larger model lose?
2. “Open weights” khác “open source” ở đâu? / How do open weights and open source differ?
3. Vì sao 4-bit không làm memory giảm đúng 4 lần? / Why is 4-bit not exactly a 4× reduction?
4. Base hay instruct model phù hợp SFT hơn? / Base or instruct model for SFT?
5. Revision pinning ngăn loại lỗi nào? / What does revision pinning prevent?

## Bài tập về nhà / Homework

So sánh ba candidate models bằng scorecard; trích dẫn model cards/licenses; lập memory budget; chạy smoke test model khả thi nhất và ghi OOM fallback ladder. / Compare three models, document licensing, capacity, smoke test, and fallback plan.

## Rubric đánh giá / Assessment rubric

| Hạng mục / Criterion | Điểm |
|---|---:|
| Model/task fit | 25 |
| License traceability | 20 |
| Memory math và đo thực tế / capacity | 25 |
| Smoke test tái lập / smoke test | 20 |
| Risk communication | 10 |

## ⚠️ Ngộ nhận thường gặp / Common misconceptions

- Public checkpoint mặc nhiên dùng thương mại được. / Public availability is not commercial permission.
- Quantization nghĩa mọi phép tính 4-bit. / Compute may use higher precision.
- Model card benchmark đảm bảo task riêng. / Public benchmarks do not replace task evaluation.
- OOM chỉ sửa bằng GPU lớn hơn. / Sequence, microbatch, checkpointing, and adapters matter.
