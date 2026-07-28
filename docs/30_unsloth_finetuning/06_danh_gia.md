# Bài 6 — Đánh giá và chẩn đoán lỗi

[← Bài 5](05_sft_va_hyperparameters.md) · [Chỉ mục](index.md) · [Bài 7 →](07_luu_va_trien_khai.md)

## Mục tiêu

- so sánh base và fine-tuned model công bằng;
- kết hợp metric tự động, rubric con người và safety tests;
- phân loại lỗi để quyết định sửa data, training hay inference.

## Thiết kế evaluation

Giữ cố định model prompt, chat template, decoding parameters và test set. So sánh ít nhất:

1. **Base model** trước training.
2. **Fine-tuned adapter** trên cùng base model.
3. Tuỳ chọn: prompt-engineered baseline hoặc model khác cùng ngân sách.

### Ba lớp metric

- **Task:** accuracy/F1, exact format, unit tests, ROUGE hoặc rubric chuyên ngành.
- **Quality:** đúng, liên quan, đầy đủ, nhất quán; chấm mù nếu dùng người.
- **Guardrail:** hallucination, từ chối sai, PII, toxicity, prompt injection, memorization.

Đánh giá thủ công bằng chat hữu ích cho khám phá nhưng không đủ để kết luận. Automated judge cũng có bias; phải lưu rubric, judge model/version và kiểm tra một mẫu bằng người.

## Error analysis

Gán mỗi lỗi vào một nhóm:

- thiếu/nhầm kiến thức;
- sai instruction hoặc format;
- suy luận sai;
- hallucination;
- output bị cắt hoặc lặp;
- safety/refusal;
- lỗi template/tokenization;
- dữ liệu test mơ hồ.

Sau đó chọn can thiệp nhỏ nhất: sửa prompt → sửa/augment data → đổi hyperparameter → đổi model/method.

## Checkpoint

- [ ] Test set chưa từng vào training hoặc synthetic generation context.
- [ ] Có bảng before/after và confidence/độ biến thiên nếu phù hợp.
- [ ] Có ít nhất 20 case review định tính.
- [ ] Có regression và safety tests.

Nguồn: [Unsloth Fine-tuning Guide — Evaluation](https://unsloth.ai/docs/get-started/fine-tuning-guide), [Datasets Guide](https://unsloth.ai/docs/get-started/fine-tuning-llms-guide/datasets-guide).
