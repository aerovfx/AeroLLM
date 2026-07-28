# Tuần 5 — Continued pretraining / Week 5 — Continued pretraining

[← Tuần 4](week04.md) · [Mục lục khoá](../INDEX.md) · [40 tuần](../../WEEK_INDEX.md) · [Lịch 20 buổi](../schedule.md) · [Tuần 6 →](week06.md)

## Mục tiêu học tập / Learning objectives

- Phân biệt continued pretraining (CPT), SFT và training from scratch. / Distinguish CPT, SFT, and scratch training.
- Xây domain/general mixture và token schedule. / Design a data mixture and schedule.
- Chọn LR, warmup, checkpoint/evaluation để giảm forgetting. / Configure a stable CPT run.
- Đánh giá domain gain, general regression và safety. / Evaluate gains and regressions.

## Lý thuyết sâu / Deep theory

CPT tiếp tục causal LM objective trên raw/domain text: $\mathcal L=-\sum_t\log p_\theta(x_t\mid x_{<t})$. Nó thích hợp khi model thiếu distribution/terminology miền; không trực tiếp dạy instruction format như SFT. / CPT adapts representations to a domain distribution rather than response behavior.

Mixture $p_{train}=\lambda p_{domain}+(1-\lambda)p_{general}$ tạo trade-off specialization–retention. Chọn $\lambda$ bằng ablation và regression gates, không chỉ domain loss. Token budget và LR nhỏ thường quan trọng hơn epochs vì documents có độ dài khác nhau. / Tune by tokens and measured retention.

Catastrophic forgetting được theo dõi qua general validation loss, benchmark/task suite, language coverage và safety. Data replay, lower LR, shorter runs hoặc parameter-efficient CPT có thể giảm regression. / No single metric fully captures forgetting.

## Buổi 1 — Mixture và schedule / Session 1 — Mixture and schedule

Tạo manifests domain/general đã dedup chéo; sampling theo token chứ không row. Tính warmup steps, total updates và cosine schedule; log realized mixture mỗi interval. / Build a token-weighted mixture and verify the realized distribution.

```python
import math  # cos và pi cho cosine learning-rate decay.

def cosine_lr(step, warmup, total, peak, min_lr):
    # Warmup tuyến tính giúp tránh update quá mạnh ở giai đoạn đầu CPT.
    if step < warmup:
        return peak * (step + 1) / warmup
    # Chuẩn hoá tiến độ sau warmup; max(1,...) phòng total == warmup.
    q = (step - warmup) / max(1, total - warmup)
    # Giảm mượt từ peak về min_lr; caller nên bảo đảm step không vượt total.
    return min_lr + 0.5 * (peak - min_lr) * (1 + math.cos(math.pi * q))
```

## Buổi 2 — Pilot, eval và rollback / Session 2 — Pilot, evaluation, rollback

1. Baseline domain/general loss và downstream probes trước CPT. / Freeze pre-CPT baselines.
2. Chạy pilot 100–500 updates; monitor loss, grad norm, throughput và NaN. / Run a guarded pilot.
3. Evaluate checkpoints ở matched token budgets; so domain gain với general regression. / Evaluate at fixed budgets.
4. Reload best checkpoint và optimizer state; chứng minh resume deterministic trong tolerance. / Test reload and resume.

Đối chiếu training loop và LR scheduler trong [`nanoGPTsource/train.py`](../../../nanoGPTsource/train.py). / Compare to the local training implementation.

## Câu hỏi thảo luận / Discussion questions

1. Khi nào CPT tốt hơn RAG? / When is CPT preferable to RAG?
2. Domain loss giảm nhưng task không tăng nói gì? / What does domain-loss-only improvement mean?
3. General replay ratio nên chọn thế nào? / How should replay ratio be selected?
4. Tokenizer mismatch cản CPT ra sao? / How does tokenizer mismatch hinder CPT?
5. Stop gate nào bảo vệ khỏi forgetting? / Which gates protect against forgetting?

## Bài tập về nhà / Homework

Thiết kế và chạy (hoặc mô phỏng có số liệu) CPT pilot với hai mixture ratios; nộp manifests, token accounting, config, logs, domain/general evaluation, checkpoint lineage và go/no-go memo. / Compare two mixture ratios in a reproducible CPT pilot or evidence-based simulation.

## Rubric đánh giá / Assessment rubric

| Hạng mục / Criterion | Điểm |
|---|---:|
| Mixture/data controls | 20 |
| Schedule/token accounting | 25 |
| Training stability/logging | 20 |
| Domain + regression evaluation | 25 |
| Decision memo | 10 |

## ⚠️ Ngộ nhận thường gặp / Common misconceptions

- CPT và SFT dùng cùng loại dữ liệu/mục tiêu. / Their objectives and data formats differ.
- Chỉ domain validation loss là đủ. / Retention and safety require separate suites.
- Một epoch có ý nghĩa cố định giữa corpora. / Epochs hide token-length differences.
- Resume chỉ cần weights. / Optimizer, scheduler, scaler, and RNG matter.
