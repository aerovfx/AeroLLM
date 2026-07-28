# Tuần 06 — SFT và dữ liệu chỉ dẫn / SFT and instruction data

## Mục tiêu học tập / Learning objectives

- Xây pipeline instruction data có provenance và version / build versioned instruction data with provenance.
- Render chat templates và response masks đúng / render chat templates and response masks correctly.
- Chạy SFT pilot, kiểm tra contamination và quality / run a quality-controlled SFT pilot.
- Tạo data-centric feedback loop từ failure analysis / create a data-centric feedback loop.

## Lý thuyết sâu / Deep theory

SFT tối ưu $\mathcal L=-\sum_tm_t\log p(y_t|x,y_{<t})$. Chất lượng phụ thuộc cả distribution coverage, correctness, diversity, formatting và label consistency. Dataset lớn nhưng duplicate/nhiễu có thể giảm effective sample size. Split theo source/document trước augmentation để tránh cùng nội dung xuất hiện ở train và eval.

Schema khuyến nghị gồm `id`, `messages`, `source`, `license`, `language`, `domain`, `quality_flags`, `split`, `content_hash`. Data lineage phải cho phép truy từ example đã render về nguồn và transformation code.

Liên kết: [Unsloth fine-tuning](../../../docs/30_unsloth_finetuning/index.md), [bài fine-tuning](../../../docs/07_fine_tune_pretrained_models/index.md).

## Buổi 1 — Data pipeline / Session 1 — Data pipeline

```python
import hashlib  # Hash canonical record để dedup/audit lineage.
import json  # Canonical JSON serialization.

def canonical_hash(messages):
    # ensure_ascii=False giữ Unicode; sort_keys loại khác biệt do thứ tự key.
    raw = json.dumps(messages, ensure_ascii=False, sort_keys=True).encode()
    # Hash bytes UTF-8 thành fingerprint 64 ký tự hexadecimal.
    return hashlib.sha256(raw).hexdigest()

def validate(r):
    # Trích role theo thứ tự để kiểm tra cấu trúc hội thoại.
    roles = [m["role"] for m in r["messages"]]
    # Sample SFT phải kết thúc bằng assistant target và có ít nhất một user turn.
    assert roles[-1] == "assistant" and "user" in roles
    # Không cho phép train sample thiếu quyền sử dụng hoặc provenance.
    assert r["license"] and r["source"]
```

### Hands-on / Thực hành

1. Ingest ≥3 sources; lưu license/provenance, không kéo dữ liệu không rõ quyền.
2. Normalize Unicode/whitespace có kiểm soát; giữ raw snapshot bất biến.
3. Exact + near dedup; báo retention theo source/language/domain.
4. Audit ngẫu nhiên 100 records với correctness, harmfulness, PII và format.
5. Freeze manifest gồm file hashes, transform commit và split stats.

## Buổi 2 — SFT pilot / Session 2 — SFT pilot

```python
# Effective token batch phản ánh compute tốt hơn số sequence khi độ dài/padding khác nhau.
# micro_batch: sequence/GPU; mean_nonpad_tokens: token thật/sequence;
# grad_accum: số micro-step; world_size: số distributed workers/GPU.
effective_tokens = micro_batch * mean_nonpad_tokens * grad_accum * world_size
```

Render bằng tokenizer/chat template của base model, thêm EOS đúng và mask prompt. Chạy overfit-32-example trước pilot. Log loss theo non-padding tokens, format pass rate, validation tasks, throughput và peak memory.

### Lab / Hands-on lab

- So sánh raw vs quality-filtered data cùng token budget.
- Slice evaluation theo source, language, task type và length.
- Phân tích 50 failures; liên kết từng lỗi tới example gần nhất hoặc coverage gap.
- Viết proposal data v2 với inclusion/exclusion rules đo được.

## Chính xác 5 câu hỏi thảo luận / Exactly 5 discussion questions

1. Thế nào là “chất lượng” với instruction example? / What constitutes instruction-example quality?
2. Near-dedup threshold quá mạnh gây mất gì? / What can overly aggressive near-dedup remove?
3. Vì sao split sau augmentation gây leakage? / Why can splitting after augmentation leak?
4. Khi nào nên giữ multi-turn context trong loss? / When should multi-turn context be supervised?
5. Failure nào nên sửa bằng data thay vì hyperparameter? / Which failures call for data rather than hyperparameter changes?

## Bài tập về nhà / Homework

Nộp dataset version ≥2.000 examples, schema/validator, manifest, license table, dedup report, 100-row audit, rendered/masked samples và SFT pilot base-vs-final. Viết data-v2 proposal dựa trên slice failures, không chỉ tăng số lượng.

## Rubric đánh giá / Assessment rubric

| Tiêu chí / Criterion | Điểm / Points |
|---|---:|
| Provenance/license/schema | 25 |
| Cleaning/dedup/splits | 20 |
| Template/mask/SFT correctness | 25 |
| Evaluation/error-to-data loop | 20 |
| Reproducibility | 10 |

## ⚠️ Hiểu lầm thường gặp / Common misconceptions

- Dữ liệu public không mặc nhiên được phép tái phân phối / Public data is not automatically redistributable.
- Dedup không thay thế quality review / Dedup is not quality control.
- Loss prompt sai có thể dạy model bắt chước user / Incorrect masks can train user imitation.
- Synthetic data cần provenance và audit như dữ liệu khác / Synthetic data still needs audits.
