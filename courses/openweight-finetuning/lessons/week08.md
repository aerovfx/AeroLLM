# Tuần 08 — Tối ưu ưu tiên với DPO / Preference optimization with DPO

[← Tuần 7](week07.md) · [Mục lục khoá](../INDEX.md) · [40 tuần](../../WEEK_INDEX.md) · [Lịch 20 buổi](../schedule.md) · [Tuần 9 →](week09.md)

## Mục tiêu học tập / Learning objectives

- Hiểu dữ liệu chosen/rejected và objective DPO / understand preference pairs and the DPO objective.
- Chuẩn bị pairs chất lượng, tránh length/style shortcuts / curate pairs without shortcuts.
- Chọn beta, reference model và train adapter / choose beta, reference model, and train an adapter.
- Đánh giá alignment gain cùng capability/safety regressions / evaluate gains and regressions.

## Lý thuyết sâu / Deep theory

Với prompt $x$, chosen $y_w$, rejected $y_l$, DPO tối ưu:

$$\mathcal L_{DPO}=-\log\sigma\left(\beta\left[\log\frac{\pi_\theta(y_w|x)}{\pi_{ref}(y_w|x)}-\log\frac{\pi_\theta(y_l|x)}{\pi_{ref}(y_l|x)}\right]\right).$$

Log-prob phải cộng trên response tokens với mask đúng. $\beta$ điều chỉnh mức phạt lệch khỏi reference trong cách tham số hoá này; ý nghĩa thực tế phụ thuộc implementation. DPO không cần reward model riêng nhưng vẫn kế thừa noise/bias của labels.

## Buổi 1 — Preference data và objective / Session 1 — Preference data and objective

```python
# Preference record gồm cùng prompt và hai câu trả lời có thứ hạng rõ ràng.
record = {"prompt": messages_without_answer,
          "chosen": high_quality_answer,  # Câu trả lời rubric/human ưu tiên.
          "rejected": plausible_but_worse_answer}  # Câu kém hơn nhưng vẫn hợp ngữ cảnh.
# Cặp giống nhau không cung cấp tín hiệu preference và thường là lỗi dữ liệu.
assert record["chosen"] != record["rejected"]
```

### Data audit / Kiểm toán dữ liệu

- Pair phải khác về phẩm chất mục tiêu, không chỉ khác chiều dài/markdown.
- Prompt không chứa lời giải hoặc nhãn “chosen”.
- Giữ hard negatives hợp lý; rejected vô nghĩa cho gradient ít giá trị.
- Split theo prompt/source trước khi tạo variants; audit annotator agreement.

## Buổi 2 — Train và đánh giá / Session 2 — Train and evaluate

```python
from trl import DPOConfig  # Cấu hình Direct Preference Optimization trainer.

cfg = DPOConfig(
    output_dir="runs/dpo",  # Adapter/checkpoint/log của stage DPO, tách khỏi SFT.
    learning_rate=5e-6,  # Thường nhỏ hơn SFT để hạn chế phá năng lực đã học.
    beta=0.1,  # Điều khiển độ mạnh preference so với reference-policy constraint.
    per_device_train_batch_size=1,  # Một preference pair/GPU/micro-step.
    gradient_accumulation_steps=16,  # Tạo effective batch lớn hơn trong VRAM nhỏ.
    max_length=2048,  # Tổng token prompt + response sau tokenize/truncate.
    max_prompt_length=1024,  # Dành ngân sách còn lại cho chosen/rejected completion.
    eval_strategy="steps",  # Chạy validation preference theo step.
    eval_steps=50,  # Theo dõi over-optimization/regression định kỳ.
)
```

### Hands-on lab / Lab thực hành

1. Bắt đầu từ checkpoint SFT; chạy 20-pair overfit smoke test.
2. Log chosen/rejected rewards, margins, accuracy, KL proxy và length.
3. Ablate beta `{0.05, 0.1, 0.5}` cùng token budget.
4. Blind pairwise eval: base, SFT, DPO; thêm factual/safety regression set.
5. Kiểm tra verbosity: win rate theo response-length bins.

## Chính xác 5 câu hỏi thảo luận / Exactly 5 discussion questions

1. Vì sao rejected quá tệ tạo tín hiệu học yếu? / Why can trivial negatives provide weak learning signals?
2. Reference model có vai trò gì trong DPO? / What role does the reference model play?
3. Length bias xâm nhập preference data bằng cách nào? / How does length bias enter preference data?
4. DPO win rate tăng nhưng factuality giảm thì quyết định ra sao? / What if DPO raises win rate but lowers factuality?
5. Khi nào cần thu thập lại labels thay vì tune beta? / When should labels be recollected rather than beta tuned?

## Bài tập về nhà / Homework

Tạo/audit ≥500 preference pairs; train ba beta từ cùng SFT checkpoint. Nộp data card, audit shortcut, logs margins, blind pairwise eval ≥50 prompts, capability/safety regressions và lựa chọn cấu hình có lý do.

## Rubric đánh giá / Assessment rubric

| Tiêu chí / Criterion | Điểm / Points |
|---|---:|
| Chất lượng/audit preference data | 25 |
| DPO implementation và masks | 25 |
| Ablation/reproducibility | 20 |
| Pairwise + regression evaluation | 20 |
| Phân tích bias/risk | 10 |

## ⚠️ Hiểu lầm thường gặp / Common misconceptions

- DPO không tự tạo preference truth / DPO does not create preference truth.
- Không dùng prompt tokens trong response log-ratio / Mask prompt tokens correctly.
- Chosen không nhất thiết dài hơn rejected / Length is not quality.
- Alignment gain có thể gây capability regression / Alignment can regress capability.
