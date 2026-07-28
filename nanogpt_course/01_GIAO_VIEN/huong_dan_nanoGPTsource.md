# Hướng dẫn giáo viên — bài tập nanoGPTsource

[Chỉ mục giáo viên](index.md) · [Hệ thống bài tập](../06_BAI_TAP_MA_NGUON/index.md)

## Vai trò của mã nguồn

`nanoGPTsource/` là bản nanoGPT có giấy phép MIT, dùng để học đọc mã, kiểm chứng shape, chạy ablation nhỏ và nối khái niệm với một training pipeline thật. README upstream ghi dự án đã cũ/deprecated, nên giáo viên cần phân biệt rõ mục tiêu sư phạm với khuyến nghị công nghệ production.

## Phân tầng lớp học

- Mọi học sinh làm mức A bằng đọc code/tensor nhỏ.
- Học sinh có máy phù hợp làm mức B; có thể dùng checkpoint/log do giáo viên cung cấp nếu không có GPU.
- Mức C là tự chọn, chấm theo thiết kế thí nghiệm chứ không theo model lớn.

Không cộng điểm chỉ vì dùng nhiều GPU hoặc train lâu hơn.

## Chuẩn bị trước buổi học

1. Pin một commit của `nanoGPTsource` và giữ nguyên suốt khoá.
2. Chạy trước cấu hình CPU/MPS/CUDA nhỏ trên đúng loại máy của lớp.
3. Chuẩn bị `train.bin`, `val.bin`, `meta.pkl` và một checkpoint nhỏ để tránh cả lớp tải cùng lúc.
4. Đặt quota cho output; đưa checkpoint/data binaries vào `.gitignore`.
5. Chuẩn bị phương án “đọc code + log có sẵn” khi Colab/GPU lỗi.

## Rubric bài tuần — 10 điểm

| Hạng mục | Điểm |
|---|---:|
| Dự đoán và hiểu code/shape | 2 |
| Code/test chạy được | 3 |
| Baseline và kiểm soát biến | 2 |
| Giải thích kết quả/giới hạn | 2 |
| Tái lập, an toàn tài nguyên/dữ liệu | 1 |

## Chống chép đáp án

- Yêu cầu học sinh giải thích một shape hoặc dòng code ngẫu nhiên.
- Mỗi nhóm dùng một seed/prompt hoặc một cặp hyperparameter khác nhau.
- Chấm patch và test, không chấm số dòng code.
- Yêu cầu kết luận cả khi kết quả bác bỏ giả thuyết.

## Bài không giao đại trà

Không yêu cầu học sinh tải OpenWebText, reproduce GPT-2 bằng 8 A100, chạy GPT-2 XL hoặc DDP nhiều node. Các config này phù hợp cho capacity-planning exercise và thảo luận scaling.
