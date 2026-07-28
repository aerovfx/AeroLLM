# Kimi K3: kiến trúc frontier và hệ thống agent / Frontier Architecture & Agent Systems

[Danh mục khoá ngắn](../README.md) · [Chỉ mục 40 tuần](../WEEK_INDEX.md) · [Lịch 20 buổi](schedule.md) · [Phân tích technical report](TECHNICAL_REPORT.md) · [Hướng dẫn repository](REPOSITORY_GUIDE.md) · [Đồ án](projects/final_project.md)

[Code lab](code/README.md) · [Yêu cầu máy tính](../COMPUTER_REQUIREMENTS.md) · [Nguồn chính thức](references/README.md)

## Tổng quan / Overview

Khoá 10 tuần dùng Kimi K3 như một case study để học cách một mô hình frontier kết hợp kiến trúc, dữ liệu, post-training, agent environment và serving. Mục tiêu là **hiểu và tái tạo ý tưởng ở quy mô nhỏ**, không phải tái huấn luyện mô hình 2.8T tham số.

> Trạng thái nguồn: technical report chính thức 47 trang, bản tải ngày 28/07/2026. Các con số benchmark là kết quả do nhóm Kimi công bố, trừ các bảng được report ghi rõ là đánh giá bên thứ ba.

## Điều kiện đầu vào / Prerequisites

- Python, PyTorch và Transformer cơ bản; đã hiểu attention, residual connection và supervised fine-tuning.
- Có thể đọc công thức đại số tuyến tính và biểu đồ benchmark.
- Không cần GPU để làm các lab kiến trúc toy; GPU/API chỉ là nhánh mở rộng.

## Chuẩn đầu ra / Learning outcomes

Sau khoá học, học viên có thể:

1. giải thích KDA–Gated MLA, AttnRes và Stable LatentMoE theo ba trục token–depth–channel;
2. cài đặt toy recurrence, block residual routing và Quantile Balancing có kiểm thử;
3. thiết kế dữ liệu multimodal/long-context và curriculum 8K → 64K → 256K → 1M ở mức kế hoạch;
4. phân tích chuỗi SFT → RL theo domain/effort → multi-teacher distillation → QAT;
5. xây agent task có sandbox, verifier, budget và đánh giá chống reward hacking;
6. đọc benchmark với đúng harness, reasoning effort, tool augmentation và giới hạn so sánh.
7. audit license, model config, `trust_remote_code` và preserved-thinking history trước deployment.

## Bản đồ 10 tuần / Course map

| Tuần | Chủ đề | Bài học | Lab chính |
|---:|---|---|---|
| 1 | Đọc report và audit claim | [Week 01](lessons/week01.md) | `model_scale_estimator.py` |
| 2 | Hybrid KDA–Gated MLA | [Week 02](lessons/week02.md) | `toy_kda.py` |
| 3 | Attention Residuals | [Week 03](lessons/week03.md) | `toy_attnres.py` |
| 4 | Stable LatentMoE | [Week 04](lessons/week04.md) | `quantile_balancing.py` |
| 5 | Native multimodal và pre-training | [Week 05](lessons/week05.md) | data-mixture design |
| 6 | Long context và systems co-design | [Week 06](lessons/week06.md) | context/caching worksheet |
| 7 | SFT, RL và reasoning effort | [Week 07](lessons/week07.md) | budget controller |
| 8 | Agent environments và verifier | [Week 08](lessons/week08.md) | `agent_verifier.py` |
| 9 | QAT, serving và evaluation | [Week 09](lessons/week09.md) | benchmark audit |
| 10 | Capstone reproduction-style | [Week 10](lessons/week10.md) | demo + technical report |

## Đánh giá / Assessment

Reading notes 10%, architecture labs 25%, data/systems design 20%, benchmark audit 15%, capstone 30%. Điều kiện đạt: ≥70/100; code chạy được trên CPU; mọi claim về Kimi K3 có nguồn; không trình bày mô phỏng toy như reproduction của model gốc.
