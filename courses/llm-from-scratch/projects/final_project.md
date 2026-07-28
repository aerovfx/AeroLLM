# Đồ án — Huấn luyện GPT nhỏ / Capstone — Train a Small GPT

[← Tổng quan](../INDEX.md) · [Lịch học](../schedule.md)

## Đề bài / Brief

Xây hoặc hoàn thiện một GPT nhỏ, huấn luyện trên corpus có quyền sử dụng, so sánh ít nhất hai cấu hình và cung cấp demo sinh văn bản. Không chấm theo model lớn; chấm theo tính đúng, khả năng tái lập và chất lượng phân tích.

## Deliverables

- source code/patch và test cho tokenizer, attention, block hoặc training loop;
- dataset card, config và seed;
- baseline + ít nhất một ablation có kiểm soát;
- learning curves, validation loss, tốc độ và mẫu sinh;
- model card, intended/out-of-scope use và failure analysis;
- README có lệnh chuẩn bị dữ liệu, train, evaluate và sample.

## Rubric 100 điểm

| Hạng mục | Điểm |
|---|---:|
| Data, tokenizer và reproducibility | 15 |
| Kiến trúc đúng và có tests | 25 |
| Training/evaluation có baseline | 20 |
| Ablation và phân tích lỗi | 15 |
| Demo, model card và safety | 15 |
| Trình bày/code quality | 10 |

## Điều kiện kỹ thuật / Technical gates

Forward/loss hữu hạn; causal test đạt; checkpoint nạp lại được; test split không rò rỉ; không commit credential/data/checkpoint lớn; mọi tuyên bố đều gắn với metric hoặc quan sát.
