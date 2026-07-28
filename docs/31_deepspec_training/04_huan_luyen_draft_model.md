# Bài 4 — Huấn luyện draft model

[← Bài 3](03_data_va_target_cache.md) · [Chỉ mục](index.md) · [Bài 5 →](05_danh_gia_va_do_an.md)

## Mục tiêu

- đọc config DSpark/DFlash/Eagle3;
- chạy training có kiểm soát hoặc thực hiện dry-run audit;
- quản lý checkpoint và khả năng resume.

## Luồng thực thi

Theo repo chính thức, `scripts/train/train.sh` gọi `train.py`, tạo một worker trên mỗi GPU visible. Thuật toán và target model được chọn qua `config_path`; các trường riêng có thể override bằng `--opts`. Checkpoint mặc định đi vào `~/checkpoints/<project_name>/<exp_name>/step_*`.

Trước khi chạy, tạo bản ghi config resolved gồm:

- algorithm và target/draft architecture;
- target cache path, layer IDs và dtype;
- batch/sequence/optimizer/scheduler;
- số GPU, seed và distributed settings;
- checkpoint cadence, output path và resume policy.

## Lab training thu nhỏ

1. Chọn config gần nhất với target model.
2. Đọc toàn bộ config và shell header; không chỉ đổi tên model.
3. Override output/cache bằng đường dẫn có quota.
4. Chạy smoke test vài step trên một cache shard.
5. Xác nhận loss hữu hạn, gradient/parameters cập nhật và checkpoint nạp lại được.
6. Chạy budget nhỏ; theo dõi loss, samples/s, GPU utilization, peak VRAM và disk growth.
7. Giữ một checkpoint baseline, không chỉ checkpoint loss thấp nhất.

### Nhánh audit không GPU

Nếu không đủ tài nguyên, chọn một released checkpoint và truy ngược: checkpoint → config → target model → dataset mode → layer cache. Sản phẩm là bảng audit các giả định và một kế hoạch lệnh, không tuyên bố đã tái hiện training.

## Checkpoint

- [ ] Config resolved và commit SHA được lưu.
- [ ] Smoke test/resume thành công trước full job.
- [ ] Target cache khớp target model/config.
- [ ] Không so sánh hai thuật toán khi training budget/setup khác nhau mà không ghi rõ.

Nguồn: [DeepSpec README — Training](https://github.com/deepseek-ai/DeepSpec#training), [config directory](https://github.com/deepseek-ai/DeepSpec/tree/main/config).
