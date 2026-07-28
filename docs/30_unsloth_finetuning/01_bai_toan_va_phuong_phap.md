# Bài 1 — Bài toán fine-tuning và chọn phương pháp

[← Chỉ mục](index.md) · [Bài 2 →](02_moi_truong_va_chon_model.md)

## Mục tiêu

- phân biệt SFT, LoRA, QLoRA, full fine-tuning, continued pre-training, preference optimization và RL;
- quyết định khi nào nên fine-tune, dùng RAG hoặc chỉ cải thiện prompt;
- thiết lập baseline và tiêu chí thành công trước training.

## Khung quyết định

| Nhu cầu | Điểm bắt đầu hợp lý |
|---|---|
| Đổi format, giọng điệu, cách tuân thủ instruction | SFT với QLoRA |
| Truy xuất thông tin thường xuyên thay đổi, cần dẫn nguồn | RAG |
| Học văn phong/nhiệm vụ từ cặp input-output | SFT |
| Thích nghi trên raw corpus chuyên ngành | Continued pre-training, rồi SFT |
| Tối ưu sở thích giữa hai câu trả lời | DPO/preference optimization |
| Tối ưu hành vi có reward kiểm chứng được | RL/GRPO |
| Baseline đã tốt nhưng prompt chưa rõ | Sửa prompt/evaluation trước |

LoRA giữ trọng số base model và học các ma trận hạng thấp. QLoRA còn lượng tử hoá base model xuống 4-bit để giảm bộ nhớ. Với người mới, hướng dẫn Unsloth khuyến nghị bắt đầu bằng QLoRA và một instruct model nhỏ; full fine-tuning chỉ nên xét khi đã chứng minh LoRA không đáp ứng.

## Lab: viết project brief

Tạo một trang mô tả:

1. **Người dùng và tác vụ:** ai hỏi gì, model phải trả lời ra sao?
2. **Không làm:** phạm vi, nội dung cần từ chối, dữ liệu nhạy cảm.
3. **Baseline:** 20–50 prompt đại diện, chạy bằng base model với cùng chat template dự kiến dùng sau training.
4. **Metric:** ít nhất một metric tác vụ và một guardrail.
5. **Ngưỡng đạt:** ví dụ tăng exact-format pass rate từ 55% lên 85% mà safety pass rate không giảm.

## Checkpoint

- [ ] Có tập test bị giữ kín khỏi training.
- [ ] Có kết quả baseline lưu được.
- [ ] Giải thích được vì sao chọn fine-tuning thay vì RAG/prompting.
- [ ] Chọn SFT + QLoRA làm thử nghiệm đầu tiên hoặc ghi rõ lý do chọn phương pháp khác.

Nguồn: [Unsloth Fine-tuning Guide — phần 1–2](https://unsloth.ai/docs/get-started/fine-tuning-guide).
