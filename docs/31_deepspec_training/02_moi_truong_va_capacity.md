# Bài 2 — Môi trường, repo và capacity planning

[← Bài 1](01_speculative_decoding.md) · [Chỉ mục](index.md) · [Bài 3 →](03_data_va_target_cache.md)

## Mục tiêu

- kiểm tra mã nguồn, license và revision trước khi chạy;
- lập ngân sách GPU, RAM, disk và thời gian;
- chọn audit/evaluation hoặc training thu nhỏ.

## Lấy mã nguồn có thể tái lập

```bash
git clone https://github.com/deepseek-ai/DeepSpec.git
cd DeepSpec
git rev-parse HEAD
python -m pip install -r requirements.txt
```

Lưu commit SHA vào báo cáo. Không đưa repo bên ngoài vào khoá học này như code do dự án sở hữu; giữ attribution và đọc `LICENSE`/`NOTICE`.

## Resource manifest

Trước mọi job ghi rõ:

```text
target_model + revision:
algorithm/config_path:
dataset rows/tokens:
cached target layers:
sequence length:
GPU model/count/VRAM:
RAM:
disk free / estimated cache:
checkpoint directory:
time budget:
```

Repo mặc định dùng 8 GPU; có thể giảm `CUDA_VISIBLE_DEVICES` nhưng điều đó không đảm bảo cấu hình vừa VRAM hoặc hoàn tất trong budget. Storage cache tăng theo số mẫu, sequence length, hidden dimension và số layer target được lưu.

## Quy tắc go/no-go

- **No-go:** chưa ước lượng cache; output nằm trong `$HOME` không đủ chỗ; không có quota; chưa pin target revision.
- **Evaluation-only:** không đủ storage/training GPU nhưng có thể dùng released checkpoint.
- **Reduced training:** subset nhỏ, ít target layers, output path có quota và cleanup plan.
- **Full reproduction:** chỉ khi hạ tầng gần với setup công bố và mục tiêu là tái hiện nghiên cứu.

## Checkpoint

- [ ] Commit SHA và license được lưu.
- [ ] Dung lượng cache ước tính nhỏ hơn quota với biên an toàn.
- [ ] Checkpoint/output dùng đường dẫn tường minh, không phụ thuộc mặc định mơ hồ.

Nguồn: [DeepSpec README — Environment/Training](https://github.com/deepseek-ai/DeepSpec), [Data preparation](https://github.com/deepseek-ai/DeepSpec/blob/main/scripts/data/README.md).
