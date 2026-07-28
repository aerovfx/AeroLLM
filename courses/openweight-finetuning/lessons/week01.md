# Tuần 1 — Bài toán, baseline và chọn phương pháp / Week 1 — Task, baseline, and method choice

## Mục tiêu học tập / Learning objectives

- Chuyển nhu cầu thành task, acceptance criteria và evaluation set. / Translate a need into a task, acceptance criteria, and evaluation set.
- Phân biệt prompting, RAG, SFT, LoRA/QLoRA, continued pretraining và preference tuning. / Distinguish adaptation methods.
- Thiết lập baseline trước fine-tuning và quyết định go/no-go. / Establish a pre-training baseline and a go/no-go gate.
- Nhận diện rủi ro safety, privacy và catastrophic forgetting. / Identify safety, privacy, and forgetting risks.

## Lý thuyết sâu / Deep theory

Fine-tuning tối ưu $\theta$ trên ví dụ $(x,y)$: $\mathcal L_{SFT}=-\sum_t m_t\log p_\theta(y_t\mid x,y_{<t})$, với $m_t$ quyết định token nào chịu loss. SFT chủ yếu dạy hành vi/format; RAG đưa tri thức có thể cập nhật vào context; continued pretraining thay đổi phân phối ngôn ngữ/miền. / SFT teaches response behavior, RAG supplies retrievable knowledge, and continued pretraining adapts domain distribution.

Decision ladder: thử prompt + structured output; nếu thiếu tri thức động, thử RAG; nếu hành vi ổn định chưa đạt, dùng PEFT/SFT; chỉ full fine-tune khi có bằng chứng PEFT thiếu capacity. Preference optimization cần dữ liệu so sánh và evaluator đủ tin cậy. / Choose the least complex intervention that addresses the observed failure.

Baseline phải chạy trên tập test đóng băng, gồm quality, format validity, refusal/safety, latency và cost. Chỉ số tổng hợp $S=\sum_iw_is_i$ chỉ hợp lệ khi weights được chốt trước. / Freeze metrics and weights before experiments to prevent goalpost movement.

Tham chiếu: [Module Unsloth — chọn phương pháp](../../../docs/30_unsloth_finetuning/01_bai_toan_va_phuong_phap.md). / Use the local decision guide.

## Buổi 1 — Task contract / Session 1 — Task contract

Nhóm viết một task card: người dùng, input/output schema, 20 positive cases, 10 edge/adversarial cases, exclusions, privacy class và success threshold. / Teams write a task card with users, schemas, evaluation cases, exclusions, and thresholds.

```python
def exact_schema_ok(answer):
    # Ba key bắt buộc định nghĩa output contract của bài toán minh hoạ.
    required = {"summary", "risk", "action"}
    # Yêu cầu đúng kiểu dict và đúng tập key: không thiếu cũng không có field ngoài schema.
    return isinstance(answer, dict) and set(answer) == required
```

## Buổi 2 — Baseline và decision memo / Session 2 — Baseline and decision memo

1. Chạy base/instruct model với prompt versioned, temperature 0 và seed nếu hỗ trợ. / Run a versioned deterministic baseline.
2. Chấm blind ít nhất 30 cases; tách quality khỏi format. / Blind-score at least 30 cases.
3. Phân loại failure: knowledge, instruction following, style, reasoning, safety. / Classify failures.
4. Viết memo chọn prompt/RAG/SFT/QLoRA/CPT và tiêu chí dừng. / Write a method-selection memo and stop criteria.

## Câu hỏi thảo luận / Discussion questions

1. Khi nào fine-tuning là giải pháp sai cho thiếu kiến thức? / When is fine-tuning wrong for missing knowledge?
2. Baseline instruct và base model nên so thế nào? / How should base and instruct models be compared?
3. Metric tự động có thể bị “game” ra sao? / How can automatic metrics be gamed?
4. Bao nhiêu improvement đủ bù chi phí vận hành? / What gain justifies operational cost?
5. Failure nào phải là hard safety gate? / Which failures should be hard safety gates?

## Bài tập về nhà / Homework

Nộp task card, 40-case evaluation set không chứa PII, baseline report, taxonomy lỗi và decision memo có phương án không fine-tune. / Submit a task card, safe evaluation set, baseline, failure taxonomy, and adaptation decision.

## Rubric đánh giá / Assessment rubric

| Hạng mục / Criterion | Điểm |
|---|---:|
| Task/acceptance rõ / task definition | 25 |
| Evaluation và baseline tái lập / evaluation | 25 |
| Failure analysis | 20 |
| Method choice có bằng chứng / evidence-based choice | 20 |
| Safety và trình bày / safety, clarity | 10 |

## ⚠️ Ngộ nhận thường gặp / Common misconceptions

- Fine-tuning là cơ sở dữ liệu đáng tin cậy. / Weights are not a reliable database.
- Train loss thấp đảm bảo task quality. / Training loss is not task success.
- RAG và SFT loại trừ nhau; chúng có thể bổ trợ. / RAG and SFT can complement each other.
- Không cần baseline vì “nhìn mẫu thấy tốt”. / Anecdotes are not a baseline.
