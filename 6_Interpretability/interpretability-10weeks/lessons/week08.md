---
layout: course
title: "Week08"
permalink: /6_Interpretability/interpretability-10weeks/lessons/week08.html
---

# Tuần 8 — Interfering with attention / Week 8 — Interfering with attention

[Mục lục khoá](../INDEX.md) · [Tài liệu nguồn](../../../docs/16_interfering_with_attention/index.md) · [← Tuần 7](week07.md) · [Tuần 9 →](week09.md)

## Mục tiêu học tập / Learning objectives

- Giải thích vì sao phải can thiệp *trước* c_proj để cô lập một attention head (trước khi các head bị trộn). / Explain why we intervene before c_proj to isolate one head.
- Thực hiện head ablation (zero-out một head) và đo logit difference trên một câu tri thức. / Perform head ablation and measure logit difference on a fact sentence.
- Mô tả head patching trong IOI: vá đầu ra của một head từ ngữ cảnh khác. / Describe head patching in IOI.
- Đọc được "mạch attention" phân tán: nhiều head góp phần nhỏ, mất một head hiếm khi sụp đổ. / Read distributed attention circuits and their redundancy.

## Công cụ và dữ liệu / Tools and data

- Python 3 + NumPy; mô hình giả với nhiều head, trong đó một head "biết" quan hệ thủ đô/quốc gia.
- [`../code/week08/01_head_ablation.py`](../code/week08/01_head_ablation.py) và [`../code/week08/02_head_patching_ioi.py`](../code/week08/02_head_patching_ioi.py).

## Lý thuyết / Theory

Trong GPT-2, nhiều attention head được nối (concatenate) rồi nhân với ma trận trộn $W_O$ ở tầng `c_proj`. Sau `c_proj`, thông tin các head đã hoà lẫn vào residual stream, không thể tách riêng. Vì vậy, để can thiệp một head, ta phải đặt hook ở **trước** `c_proj`, khi dữ liệu còn ở dạng các khối head riêng biệt — có thể reshape, zero-out hoặc vá từng head.

**Head ablation**: gán 0 cho đầu ra một head. Trên câu "Berlin is the capital of...", ablation thường làm giảm nhẹ logit token đúng ("Germany") nhưng *tăng* logit token cùng nhóm ngữ nghĩa nhưng sai ("France"). Điều thú vị: top-1 vẫn đúng trong hầu hết trường hợp — mạng có tính dư thừa cao, mất một head hiếm khi sụp đổ. Đây là lý do phải đo bằng **logit difference liên tục**, không chỉ đúng/sai.

**Head patching** nâng cấp ablation: thay vì zero-out, ta vá đầu ra head từ một ngữ cảnh khác để xem head đó "mang" thông tin gì — chính xác hơn về mặt nhân quả, đặc biệt trong IOI.

## Lab từng bước / Step-by-step lab

1. Chạy [`01_head_ablation.py`](../code/week08/01_head_ablation.py), so logit difference khi lần lượt tắt từng head. / Compare logit difference per ablated head.
2. Quan sát hiện tượng "token đúng giảm, token nhiễu tăng". / Observe correct-token drop and distractor rise.
3. Chạy [`02_head_patching_ioi.py`](../code/week08/02_head_patching_ioi.py), tìm head mà patching làm "lật" dự đoán IOI. / Find the head whose patching flips the IOI prediction.
4. Lập bảng: head, Δ logit (ablation), Δ logit (patching), nhận xét vai trò. / Tabulate heads and their roles.

## Liên kết code / Code links

- [`../code/week08/01_head_ablation.py`](../code/week08/01_head_ablation.py) — head ablation.
- [`../code/week08/02_head_patching_ioi.py`](../code/week08/02_head_patching_ioi.py) — head patching trong IOI.

## Câu hỏi thảo luận / Discussion questions

1. Vì sao phải hook trước c_proj mà không phải sau? / Why hook before c_proj and not after?
2. "Top-1 vẫn đúng" có nghĩa ablation vô ích không? / Does a correct top-1 mean ablation is useless?
3. Ablation và patching trả lời câu hỏi nhân quả khác nhau thế nào? / How do ablation and patching answer different causal questions?
4. Tính dư thừa của attention gây khó gì cho việc tìm "head quan trọng"? / How does attention redundancy complicate finding important heads?

## Bài tập về nhà / Homework

- **Cơ bản**: chạy hai script, liệt kê head nào nhạy nhất và vai trò phỏng đoán.
- **Nâng cao**: thay zero-out bằng mean-ablation (trừ trung bình head) và so kết quả.
- **Thử thách**: dùng patching để vẽ sơ đồ "head nào chuyển thông tin từ token nào" trong câu IOI giả.

## Yêu cầu nộp / Submission

- Bảng head + logit difference (cả ablation lẫn patching) + sơ đồ mạch phỏng đoán, nộp theo đường dẫn thầy chỉ định.

## Rubric (100 điểm) / Assessment rubric

| Tiêu chí | Điểm |
|---|---:|
| Đúng chức năng: tách head đúng, logit difference đúng | 35 |
| An toàn & xử lý lỗi: reshape head đúng shape, baseline, seed | 25 |
| Chất lượng code/tài liệu: chú thích, hàm rõ | 20 |
| Phân tích: đọc mạch phân tán, nêu tính dư thừa | 20 |

## Lưu ý an toàn / Safety notes

- Chỉ can thiệp mô hình giả local; không sửa model thật đang phục vụ.
- Đo logit difference liên tục, đừng chỉ nhìn top-1 đúng/sai.
- Ghi rõ vị trí hook (trước/sau c_proj) vì nó đổi hoàn toàn ý nghĩa kết quả.
