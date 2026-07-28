# Module 31 — Huấn luyện Speculative Decoding với DeepSpec

[Trang chủ](../../README.md) · [Lộ trình](../../COURSE.md) · [Module Unsloth](../30_unsloth_finetuning/index.md)

Chuyên đề nâng cao về huấn luyện và đánh giá **draft model** cho speculative decoding bằng [deepseek-ai/DeepSpec](https://github.com/deepseek-ai/DeepSpec). DeepSpec cung cấp toàn bộ pipeline chuẩn bị dữ liệu, target cache, training và evaluation cho DSpark, DFlash và Eagle3.

## Vị trí trong lộ trình

Học sau pre-training, fine-tuning và evaluation. Module này tối ưu **inference**, không thay thế SFT/QLoRA:

```text
Target LLM đã huấn luyện
        ↓ sinh dữ liệu + hidden-state cache
Huấn luyện draft model
        ↓ đề xuất token
Target LLM xác minh
        ↓
Đo acceptance, latency và throughput
```

## Cảnh báo tài nguyên

Repo chính thức mặc định cho một node 8 GPU. Target cache mặc định với `Qwen/Qwen3-4B` được tác giả cảnh báo có thể chiếm khoảng **38 TB**. Không chạy `prepare_data.sh` mặc định trên laptop, Colab hoặc ổ đĩa dùng chung. Hãy kiểm tra dung lượng, giảm dataset/layer cache, hoặc dùng checkpoint phát hành sẵn.

## Hai lộ trình thực hành

| Nhánh | Phù hợp | Phạm vi |
|---|---|---|
| Audit + Evaluation | Phần lớn người học | đọc config, dùng checkpoint có sẵn, chạy evaluation thu nhỏ |
| Training thu nhỏ | Lab nhiều GPU và storage | tạo subset, cache ít layer, train draft checkpoint |

## Chỉ mục

| Buổi | Nội dung | Đầu ra |
|---:|---|---|
| 1 | [Speculative decoding và kiến trúc DeepSpec](01_speculative_decoding.md) | Sơ đồ và baseline plan |
| 2 | [Môi trường, repo và capacity planning](02_moi_truong_va_capacity.md) | Resource manifest |
| 3 | [Data preparation và target cache](03_data_va_target_cache.md) | Data/cache manifest |
| 4 | [Huấn luyện draft model](04_huan_luyen_draft_model.md) | Run config hoặc dry-run audit |
| 5 | [Đánh giá và đồ án](05_danh_gia_va_do_an.md) | Báo cáo acceptance–quality–cost |

## Nguồn chuẩn

- [DeepSpec repository](https://github.com/deepseek-ai/DeepSpec)
- [Data preparation README](https://github.com/deepseek-ai/DeepSpec/blob/main/scripts/data/README.md)
- [DSpark paper](https://arxiv.org/abs/2607.05147)
- [Released checkpoints](https://github.com/deepseek-ai/DeepSpec#released-checkpoints)

DeepSpec dùng giấy phép MIT nhưng có mã thích nghi từ dự án bên thứ ba; xem `NOTICE` trong repo trước khi phân phối derivative.
