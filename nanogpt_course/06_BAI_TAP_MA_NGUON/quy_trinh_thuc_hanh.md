# Quy trình làm và nộp bài mã nguồn

[← Chỉ mục](index.md) · [Bài tập theo tuần](bai_tap_theo_tuan.md) · [Phiếu báo cáo](phieu_bao_cao.md)

## 1. Chuẩn bị bản làm việc

Không chỉnh trực tiếp bản `nanoGPTsource/` dùng chung. Sao chép vào thư mục cá nhân hoặc tạo nhánh Git. Lưu commit/revision nguồn trong báo cáo.

Các dependency cơ bản được liệt kê trong [README nguồn](../../nanoGPTsource/README.md). Không commit token W&B hoặc credential dịch vụ.

## 2. Chạy smoke test nhỏ

Trước training dài, xác nhận:

- Python import được `torch`, `numpy`, `transformers`, `datasets`, `tiktoken`, `wandb`, `tqdm` khi bài cần;
- dữ liệu Shakespeare character đã tạo `train.bin`, `val.bin` và `meta.pkl`;
- thiết bị là `cpu`, `mps` hoặc `cuda` đúng với máy;
- `compile=False` nếu nền tảng không hỗ trợ `torch.compile`;
- output/checkpoint ghi vào thư mục cá nhân.

Lệnh CPU/Mac khởi đầu phải dùng model nhỏ, ít iteration và context ngắn. Không dùng cấu hình `train_gpt2.py` trong lớp học thông thường: config này nhắm tới 8 GPU A100 và training rất dài.

## 3. Chu trình thí nghiệm

```text
Dự đoán → Ghi baseline → Chỉ đổi 1 biến → Chạy → So sánh → Giải thích
```

Mỗi run cần lưu:

```text
run_id, commit, device, seed
dataset, config và mọi CLI override
parameter count, block_size, batch_size
learning rate, iterations, train/val loss
wall time, checkpoint, sample output
```

## 4. Quy tắc đọc code

1. Đọc docstring/comment và shape đầu vào/đầu ra.
2. Viết dự đoán trước khi chạy.
3. Dùng tensor nhỏ hoặc một batch nhỏ để kiểm chứng.
4. Không xoá assertion/test chỉ để code chạy.
5. Khi gặp lỗi, nộp minimal reproduction và traceback liên quan.

## 5. Quy tắc tài nguyên và dữ liệu

- Không download OpenWebText trên máy/phòng lab nếu chưa được duyệt dung lượng và băng thông.
- Không chạy GPT-2 XL hoặc reproduction nhiều GPU như một bài tập bắt buộc.
- Không đẩy `train.bin`, `val.bin`, checkpoint lớn hoặc credential lên Git.
- Kiểm tra quyền sử dụng dữ liệu tự chọn; loại PII và nội dung không phù hợp.
- Dừng run khi loss thành NaN, disk gần đầy hoặc nhiệt độ/phần cứng bất thường.

## 6. Nộp bài

Mỗi nhóm nộp patch/code đã thay đổi, [phiếu báo cáo](phieu_bao_cao.md), log rút gọn và một đoạn giải thích 150–300 từ. Ảnh chụp màn hình không thay thế code, config hoặc metric.
