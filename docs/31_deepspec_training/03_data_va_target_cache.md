# Bài 3 — Data preparation và target cache

[← Bài 2](02_moi_truong_va_capacity.md) · [Chỉ mục](index.md) · [Bài 4 →](04_huan_luyen_draft_model.md)

## Mục tiêu

- hiểu ba bước tạo dữ liệu DeepSpec;
- ngăn data leakage và sampling mismatch;
- tạo cache thu nhỏ có manifest và checksum.

## Pipeline chính thức

1. Download prompt data và tách held-out user turns.
2. Dùng target model tái sinh assistant answers qua endpoint OpenAI-compatible.
3. Chạy target model để precompute hidden-state cache dùng khi train draft.

Sampling khi tái sinh phải phù hợp target model: temperature, top-p, top-k, min-p, thinking mode và max tokens đều ảnh hưởng phân phối mà draft sẽ học. Không trộn cache từ target revision hoặc chế độ sinh khác mà không ghi provenance.

## Lab an toàn: subset trước

1. Audit schema và license của dataset.
2. Tạo train/test split trước generation; kiểm tra duplicate.
3. Chỉ lấy subset nhỏ để xác nhận pipeline.
4. Khởi chạy inference server bằng engine tương thích `/v1`.
5. Sinh answers, lưu cả error file và tỷ lệ lỗi.
6. Dừng server nếu bước cache dùng cùng GPU.
7. Chỉ cache một số target layers theo config thử nghiệm.
8. Ghi manifest: target SHA, tokenizer, sampling, row count, token stats, layer IDs, dtype, bytes và checksum.

Không chạy wrapper mặc định trước khi đọc từng lệnh. Với Qwen3-4B mặc định, tài liệu repo cảnh báo cache đầy đủ xấp xỉ 38 TB.

## Kiểm định

- So sánh số input/output rows và lý do row thất bại.
- Mở ngẫu nhiên prompt/answer sau generation.
- Xác nhận test prompts không vào cache training.
- Nạp thử một shard cache trước khi tạo toàn bộ.
- Đo bytes/token trên subset rồi ngoại suy có biên an toàn.

## Checkpoint

- [ ] Split và provenance tái lập được.
- [ ] Sampling khớp target deployment dự kiến.
- [ ] Cache manifest có layer IDs và checksum.
- [ ] Có cleanup/retention policy cho artifact rất lớn.

Nguồn: [DeepSpec Data Preparation README](https://github.com/deepseek-ai/DeepSpec/blob/main/scripts/data/README.md).
