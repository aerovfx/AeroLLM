# Tuần 4 — Chat templates và tokenization / Week 4 — Chat templates and tokenization

[← Tuần 3](week03.md) · [Mục lục khoá](../INDEX.md) · [40 tuần](../../WEEK_INDEX.md) · [Lịch 20 buổi](../schedule.md) · [Tuần 5 →](week05.md)

## Mục tiêu học tập / Learning objectives

- Render roles thành token sequence đúng convention của model. / Render roles using the model's expected convention.
- Phân biệt BOS/EOS/PAD và generation prompt. / Distinguish special-token roles.
- Mask prompt tokens khi mục tiêu là assistant-only loss. / Mask prompt tokens when appropriate.
- Kiểm thử parity giữa train và inference. / Test train/inference parity.

## Lý thuyết sâu / Deep theory

Chat template là serialization protocol, không phải trang trí. Nó ánh xạ danh sách `{role, content}` thành chuỗi có control tokens. Sai token hoặc double BOS/EOS tạo distribution shift dù nội dung chữ giống nhau. / Templates are part of the model interface.

Với serialized IDs $z_{1:T}$ và assistant mask $m_t$, loss $-\sum_tm_t\log p(z_t\mid z_{<t})/\sum_tm_t$. Full-sequence loss cũng dạy mô hình tái tạo system/user; assistant-only tập trung capacity vào completion nhưng mask sai có thể tạo zero loss. / Loss masking is a training-objective decision, not boilerplate.

Truncation phải có policy: giữ system + latest turn, drop oldest complete turns, không cắt giữa control token, và đo tỷ lệ truncated. PAD ID không nên tùy tiện gán nếu model/config yêu cầu khác; loss phải ignore padding. / Truncation and padding policies must be explicit and measured.

## Buổi 1 — Render, inspect, assert / Session 1 — Render, inspect, assert

1. Render một conversation bằng tokenizer template; in raw string, IDs và decoded special tokens. / Inspect all representations.
2. Assert đúng một BOS theo model card, EOS ở response boundary và generation prompt chỉ ở inference. / Assert special-token invariants.
3. So sánh cùng conversation nếu hand-format sai. / Observe protocol drift from manual formatting.

```python
# Một hội thoại SFT hoàn chỉnh: system policy, user input và assistant target.
messages = [
    {"role": "system", "content": "Trả lời ngắn."},
    {"role": "user", "content": "Attention là gì?"},
    {"role": "assistant", "content": "Cơ chế trộn thông tin theo trọng số."},
]
# Render role/content thành chuỗi đúng special-token format của model.
# tokenize=False cho phép con người audit chuỗi trước khi mã hoá.
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=False,  # False vì dữ liệu đã có assistant answer để train.
)
# Template thường đã tự thêm special tokens; tắt thêm lần hai để tránh token trùng.
ids = tokenizer(text, add_special_tokens=False)["input_ids"]
```

## Buổi 2 — Collation và loss mask / Session 2 — Collation and loss masks

Hands-on: xây collator padding động; tạo labels copy của IDs; đặt prompt/PAD labels thành `-100`; assert có ít nhất một supervised token; decode riêng supervised span; so sánh train render với inference prefix byte/token-level. / Build and validate a dynamic collator and assistant-only labels.

Tham chiếu [dataset và chat template](../../../docs/30_unsloth_finetuning/03_dataset_va_chat_template.md). / Consult local guidance.

## Câu hỏi thảo luận / Discussion questions

1. Vì sao template đúng quan trọng hơn prompt nhìn “đẹp”? / Why does protocol beat visual formatting?
2. Khi nào full-sequence loss có lợi? / When is full-sequence loss useful?
3. Double EOS ảnh hưởng generation thế nào? / How can double EOS affect generation?
4. Truncation theo token khác theo ký tự ra sao? / How does token truncation differ from character truncation?
5. Parity test nào phát hiện train/serve skew? / Which test detects train/serve skew?

## Bài tập về nhà / Homework

Xây preprocessing/collator cho multi-turn Việt–Anh; nộp 10 golden serialization tests, special-token audit, assistant-mask visualization, length/truncation report và parity test inference. / Submit a thoroughly tested bilingual chat preprocessing pipeline.

## Rubric đánh giá / Assessment rubric

| Hạng mục / Criterion | Điểm |
|---|---:|
| Template/special tokens đúng | 30 |
| Loss mask và padding đúng | 25 |
| Golden/parity tests | 20 |
| Truncation analysis | 15 |
| Documentation | 10 |

## ⚠️ Ngộ nhận thường gặp / Common misconceptions

- Mọi instruct model dùng format giống nhau. / Chat formats are model-specific.
- `add_special_tokens=True` luôn đúng sau template. / It may duplicate tokens.
- Mask prompt nghĩa xóa prompt khỏi input. / Prompt remains context; only labels are ignored.
- Decode round-trip đủ chứng minh loss mask đúng. / Label alignment needs separate tests.
