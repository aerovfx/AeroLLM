# Tuần 3 — Thiết kế dataset và QA / Week 3 — Dataset design and QA

## Mục tiêu học tập / Learning objectives

- Thiết kế schema instruction–response bám task. / Design a task-aligned instruction-response schema.
- Kiểm tra provenance, consent, license, PII và duplicates. / Audit provenance, consent, licensing, PII, and duplicates.
- Tạo split theo entity/document để ngăn leakage. / Create leakage-resistant splits.
- Định lượng coverage, length, quality và disagreement. / Quantify coverage and quality.

## Lý thuyết sâu / Deep theory

Chất lượng SFT phụ thuộc conditional distribution của examples, không chỉ số hàng. Sampling nên cân bằng intents, languages, difficulty, refusals và edge cases theo deployment mixture. / Example mix should approximate deployment while deliberately covering rare high-risk cases.

Near-duplicate leakage làm evaluation lạc quan. Exact hash bắt bản sao tuyệt đối; normalized hash bỏ biến thể whitespace; MinHash/embedding similarity tìm near duplicates nhưng cần threshold review. Split theo customer/document/thread trước sampling. / Group splitting prevents related records from crossing partitions.

Label QA: guideline + gold set + double annotation trên sample. Với nhãn categorical, Cohen's $\kappa=(p_o-p_e)/(1-p_e)$; agreement thấp báo guideline mơ hồ, không tự động chứng minh annotator kém. / Low agreement often reveals ambiguous policy.

## Buổi 1 — Schema và coverage matrix / Session 1 — Schema and coverage

Tạo data specification: fields, types, nullable rules, max lengths, allowed languages, source ID, license, annotator version, safety tag. Lập matrix `intent × difficulty × language × safety`. / Create a typed specification and coverage matrix.

```python
def validate(r):
    # Instruction phải là chuỗi không rỗng sau khi bỏ whitespace hai đầu.
    assert isinstance(r["instruction"], str) and r["instruction"].strip()
    # Response cũng phải có nội dung vì đây là supervised target của SFT.
    assert isinstance(r["response"], str) and r["response"].strip()
    # Chỉ chấp nhận taxonomy ngôn ngữ đã thống nhất trong data contract.
    assert r["language"] in {"vi", "en", "mixed"}
    # Provenance và license là điều kiện bắt buộc trước khi sample được dùng để train.
    assert "source_id" in r and "license" in r
```

## Buổi 2 — QA pipeline / Session 2 — QA pipeline

1. Schema validation → PII scan → normalization → exact/near dedup → group split. / Run ordered QA stages.
2. Không log raw PII; quarantine records thay vì âm thầm xoá. / Quarantine unsafe records and avoid logging PII.
3. Human-review stratified sample và 100% high-risk cases. / Review stratified and high-risk samples.
4. Xuất data card: sources, transformations, limitations, removals, split hashes. / Produce a data card.

Tham chiếu [Datasets Guide nội bộ](../../../docs/30_unsloth_finetuning/03_dataset_va_chat_template.md). / Use the local dataset guidance.

## Câu hỏi thảo luận / Discussion questions

1. Vì sao nhiều dữ liệu hơn có thể làm model tệ hơn? / Why can more data hurt?
2. Nên oversample edge cases đến mức nào? / How much should edge cases be oversampled?
3. Dedup threshold cao/thấp gây trade-off gì? / What is the dedup threshold trade-off?
4. Synthetic response cần provenance riêng không? / Does synthetic data need separate provenance?
5. Agreement thấp nên sửa guideline hay loại annotator? / What should low agreement trigger?

## Bài tập về nhà / Homework

Tạo tối thiểu 200 records hoặc audit dataset có sẵn; nộp schema, validator, coverage table, duplicate/PII report, group split manifest và data card. Không nộp dữ liệu nhạy cảm thật. / Build or audit a safe dataset with a full QA and provenance package.

## Rubric đánh giá / Assessment rubric

| Hạng mục / Criterion | Điểm |
|---|---:|
| Schema/task coverage | 25 |
| Provenance/license/privacy | 25 |
| Dedup/split correctness | 20 |
| QA metrics và review / QA | 20 |
| Data card clarity | 10 |

## ⚠️ Ngộ nhận thường gặp / Common misconceptions

- JSON hợp lệ đồng nghĩa mẫu tốt. / Valid syntax is not semantic quality.
- Random row split luôn đủ. / Group leakage defeats row splits.
- PII regex bắt được mọi dữ liệu nhạy cảm. / Automated scans need review.
- Dữ liệu synthetic không có license/safety concern. / Synthetic data still needs governance.
