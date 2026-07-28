# Bài 3 — Dataset và chat template

[← Bài 2](02_moi_truong_va_chon_model.md) · [Chỉ mục](index.md) · [Bài 4 →](04_lora_qlora.md)

## Mục tiêu

- chọn đúng format raw corpus, instruct, conversation hoặc preference;
- chuẩn hoá role và áp chat template nhất quán;
- chia train/validation/test mà không rò rỉ dữ liệu.

## Data contract

Trước khi viết code, định nghĩa:

| Trường | Câu hỏi bắt buộc |
|---|---|
| Mục đích | Hành vi nào cần học? |
| Input | Người dùng cung cấp gì? |
| Output | Văn bản, JSON, code hay nhãn? |
| Role | `system`, `user`, `assistant` có hợp lệ không? |
| Nguồn/quyền | Có quyền dùng để train và phân phối không? |
| Chất lượng | Cách phát hiện trùng, sai, PII, prompt injection? |

## Format chính

- **Raw corpus:** continued pre-training.
- **Instruction:** instruction/input/output cho SFT một lượt.
- **Conversation/ChatML:** danh sách message nhiều lượt với `role` và `content`.
- **ShareGPT:** thường dùng `from` và `value`; chỉ chuẩn hoá khi source thực sự ở format này.
- **Preference:** prompt cùng chosen/rejected response cho DPO hoặc phương pháp tương tự.

Chat template biến cấu trúc message thành chuỗi token đúng với model. Sai template có thể khiến loss vẫn giảm nhưng inference hỏng vì model học các token phân cách khác lúc phục vụ.

## Lab kiểm định dữ liệu

1. Viết schema và kiểm tra mọi row.
2. Loại row rỗng, role sai, assistant answer thiếu và bản ghi trùng/near-duplicate.
3. Kiểm tra 50 mẫu ngẫu nhiên bằng người.
4. Tách theo nguồn/chủ đề/người dùng trước khi augment để tránh leakage.
5. Áp chat template và in 3 chuỗi sau format.
6. Đo phân bố token; quyết định truncate, filter hay tăng context.
7. Lập dataset card: nguồn, license, số row, split, ngôn ngữ, giới hạn và thay đổi làm sạch.

Tài liệu Unsloth gợi ý tối thiểu khoảng 100 mẫu để có tín hiệu ban đầu và trên 1.000 mẫu cho kết quả tốt hơn, nhưng chất lượng và độ phủ quan trọng hơn việc tăng số lượng mù quáng.

## Checkpoint

- [ ] Không có overlap giữa train và test.
- [ ] 100% row qua schema validation.
- [ ] Đã xem chuỗi sau chat template, không chỉ xem JSON gốc.
- [ ] Có dataset card và danh sách failure modes.

Nguồn: [Datasets Guide](https://unsloth.ai/docs/get-started/fine-tuning-llms-guide/datasets-guide), [Chat Templates](https://unsloth.ai/docs/basics/chat-templates).
