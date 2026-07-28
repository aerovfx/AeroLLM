# Bài 8 — Đồ án cuối khoá

[← Bài 7](07_luu_va_trien_khai.md) · [Chỉ mục](index.md)

## Đề bài

Fine-tune một instruct model nhỏ bằng Unsloth + QLoRA cho một tác vụ có thể đánh giá được. Ví dụ: trả lời hỗ trợ theo taxonomy, chuyển text thành JSON, phân loại có giải thích, viết theo style có rubric hoặc trợ lý miền hẹp.

Không chọn bài toán chỉ có thể chứng minh bằng vài ảnh chụp chat. Đồ án phải có test set và baseline.

## Deliverables

```text
project/
├── README.md              # cách tái lập và kết quả chính
├── model-card.md          # base model, data, method, limits
├── dataset-card.md        # nguồn, license, schema, split, QA
├── train.ipynb            # notebook sạch, chạy từ đầu đến cuối
├── eval/                  # test cases, rubric, results
└── inference/             # lệnh hoặc notebook chạy artifact
```

## Rubric 100 điểm

| Hạng mục | Điểm |
|---|---:|
| Bài toán, baseline và tiêu chí thành công | 15 |
| Chất lượng, quyền sử dụng và kiểm định dữ liệu | 20 |
| Cấu hình QLoRA/SFT và khả năng tái lập | 20 |
| Đánh giá before/after, error analysis | 25 |
| Export, inference và model card | 10 |
| Safety, giới hạn và trình bày | 10 |

## Điều kiện đạt

- tổng điểm từ 70/100;
- notebook chạy được hoặc có log/artifact đủ để kiểm chứng;
- không có data leakage đã biết;
- không công khai credential hoặc dữ liệu không có quyền sử dụng;
- kết luận bám theo số liệu, kể cả khi fine-tuning không thắng baseline.

## Bài mở rộng

- so sánh QLoRA 4-bit với LoRA 16-bit cùng budget;
- ablation rank hoặc lượng dữ liệu;
- so sánh fine-tuning với RAG;
- export GGUF ở hai mức quantization và đo quality/latency/size;
- DPO/GRPO chỉ sau khi SFT baseline và reward/evaluation đáng tin cậy.

Nguồn chuẩn để cập nhật notebook và API: [Unsloth Fine-tuning LLMs Guide](https://unsloth.ai/docs/get-started/fine-tuning-guide).
