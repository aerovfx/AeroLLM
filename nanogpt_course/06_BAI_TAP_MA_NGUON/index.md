# Hệ thống bài tập thực hành với nanoGPTsource

[Trang khoá học](../README.md) · [Mã nguồn tham chiếu](../../nanoGPTsource/README.md) · [Hướng dẫn dự án](../03_THUC_HANH_DU_AN/index.md)

Hệ thống này biến mã nguồn trong `nanoGPTsource/` thành bài tập tăng dần cho khoá nanoGPT 10 tuần. Học sinh không cần đọc toàn bộ repository ngay từ đầu: mỗi tuần chỉ mở những file và hàm liên quan.

## Nguyên tắc sử dụng

- `nanoGPTsource/` là **mã tham chiếu**, không phải đáp án để chép nguyên file.
- Mọi thay đổi của học sinh thực hiện trong một bản sao/nhánh riêng; không sửa nguồn gốc dùng chung.
- Chạy cấu hình nhỏ trước. Không chạy OpenWebText hoặc GPT-2 reproduction nếu chưa được giáo viên duyệt tài nguyên.
- Ghi baseline trước khi sửa và chỉ thay một biến trong mỗi thí nghiệm.
- README upstream ghi nanoGPT đã cũ/deprecated; khoá học dùng nó vì mã ngắn, rõ và có giá trị sư phạm, không coi đây là stack production hiện đại.

## Chỉ mục

- [Bản đồ mã nguồn theo 10 tuần](bai_tap_theo_tuan.md)
- [Quy trình làm và nộp bài](quy_trinh_thuc_hanh.md)
- [Phiếu báo cáo thí nghiệm](phieu_bao_cao.md)
- [Hướng dẫn giáo viên và gợi ý chấm](../01_GIAO_VIEN/huong_dan_nanoGPTsource.md)

## Ba mức độ

| Mức | Ký hiệu | Yêu cầu |
|---|---|---|
| Khởi động | A | đọc code, dự đoán output, chạy test nhỏ |
| Thực hành | B | hoàn thiện/chỉnh một phần code và đo kết quả |
| Thử thách | C | thiết kế ablation, benchmark hoặc mở rộng |

Mỗi tuần hoàn thành A và B; mức C dành cho nhóm tiến nhanh. Các bài chạy training phải nộp log/config thay vì chỉ nộp ảnh chụp output.

## Bản đồ repository

| Nguồn | Vai trò trong bài tập |
|---|---|
| [`model.py`](../../nanoGPTsource/model.py) | attention, MLP, block, GPT, optimizer và generation |
| [`train.py`](../../nanoGPTsource/train.py) | batching, loss, learning-rate schedule, checkpoint, DDP |
| [`sample.py`](../../nanoGPTsource/sample.py) | inference, temperature và top-k |
| [`config/`](../../nanoGPTsource/config/) | cấu hình train/eval/fine-tune có thể override |
| [`data/shakespeare_char/prepare.py`](../../nanoGPTsource/data/shakespeare_char/prepare.py) | tokenizer ký tự và train/validation binaries |
| [`data/shakespeare/prepare.py`](../../nanoGPTsource/data/shakespeare/prepare.py) | GPT-2 BPE trên Tiny Shakespeare |
| [`bench.py`](../../nanoGPTsource/bench.py) | benchmark training step |
| [`transformer_sizing.ipynb`](../../nanoGPTsource/transformer_sizing.ipynb) | tham số và kích thước Transformer |
| [`scaling_laws.ipynb`](../../nanoGPTsource/scaling_laws.ipynb) | bài mở rộng về scaling laws |

Nguồn được lưu kèm giấy phép [MIT](../../nanoGPTsource/LICENSE), bản quyền Andrej Karpathy.
