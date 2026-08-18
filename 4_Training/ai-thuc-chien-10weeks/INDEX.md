---
layout: course
title: "Index"
permalink: /4_Training/ai-thuc-chien-10weeks/INDEX.html
---

# AI Thực Chiến — nhánh training nâng cao (10 tuần)

Nhánh ứng dụng của AeroLLM, phù hợp sau khi hoàn thành Giai đoạn 4 (pre-training). Nội dung tập trung vào dữ liệu, huấn luyện phân tán, post-training, đánh giá và đóng gói mô hình.

## Cấu trúc

- [Lịch học](schedule.md)
- `lessons/week01.md` … `week10.md`: bài học theo tuần.
- [Dự án cuối khóa](projects/final_project.md)
- [Code & môi trường](code/README.md)
- `references/`: tài liệu cuộc thi (Round 2–4) và hướng dẫn model training chi tiết.

## Chuyên đề hệ thống nâng cao

- [DeepSpec — huấn luyện draft model cho speculative decoding](../../docs/31_deepspec_training/index.md): học sau distributed training và evaluation; yêu cầu capacity planning nghiêm ngặt (pipeline mặc định giả định 8 GPU và target cache rất lớn).

## Quy tắc thực hành

Chỉ chạy thí nghiệm trong môi trường do bạn kiểm soát. Ưu tiên tập dữ liệu nhỏ, checkpoint thường xuyên, ghi log rõ ràng và chuẩn bị phương án rollback trước mỗi lần huấn luyện.
