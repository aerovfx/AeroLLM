---
layout: course
title: "Week01"
permalink: /6_Interpretability/interpretability-10weeks/lessons/week01.html
---

# Tuần 1 — Nhập môn interpretability & phương pháp / Week 1 — Introduction to interpretability and methods

[Mục lục khoá](../INDEX.md) · [Lịch 20 buổi](../schedule.md) · [Tài liệu nguồn](../../../docs/15_interpretability/index.md) · [Tuần 2 →](week02.md)

## Mục tiêu học tập / Learning objectives

- Phát biểu định nghĩa mechanistic interpretability là "dịch ngược hộp đen" (reverse engineering), phân biệt observational với causal. / Define mechanistic interpretability as reverse-engineering and distinguish observational from causal approaches.
- Mô tả residual stream như dòng trạng thái được cập nhật bởi attention và MLP ở mỗi block. / Describe the residual stream as a state updated by attention and MLP per block.
- Giải thích ba rào cản: biểu diễn phân tán (distributed representations), hành vi trỗi dậy (emergence), thiếu ground truth. / Explain the three barriers: distributed representations, emergence, and lack of ground truth.
- Chạy được baseline và linear probe trên mô hình giả, đọc số liệu thô như một nhà phân tích. / Run a baseline and a linear probe on a toy model and read raw numbers analytically.

## Công cụ và dữ liệu / Tools and data

- Python 3 + NumPy (đã có sẵn trong repo); không cần tải mô hình thật.
- Mô hình giả: ma trận embedding ngẫu nhiên có seed + vài "block" cập nhật giả lập residual stream.
- [`../code/week01/01_residual_stream.py`](../code/week01/01_residual_stream.py) và [`../code/week01/02_linear_probe_baseline.py`](../code/week01/02_linear_probe_baseline.py).

## Lý thuyết / Theory

Mechanistic interpretability muốn trả lời *cách* mô hình tính toán, chứ không chỉ *kết quả* nó trả về. Thay vì đọc input/output, ta soi vào các kích hoạt (activations) và trọng số (weights) bên trong.

Mô hình hồi quy tuyến tính $y=\beta_0+\beta_1 x$ dễ diễn giải vì $\beta_1$ mang nghĩa trực tiếp ("học thêm một giờ tăng bao nhiêu điểm"). LLM cũng chỉ là phép nhân ma trận và cộng vector, nhưng ở hàng nghìn chiều và xếp chồng phi tuyến. Mỗi token là một vector $h$ đi qua residual stream:

$$h_{out} = \text{LayerNorm}\big(h_{in} + \text{Attention}(h_{in}) + \text{MLP}(h_{in})\big)$$

Ba rào cản cốt lõi:

1. **Distributed representations**: một khái niệm (như "Paris") không nằm gọn ở một neuron, mà rải trên nhiều chiều phối hợp nhau.
2. **Emergence / reductionism**: hiểu từng neuron không bảo đảm hiểu được hành vi tổng thể trỗi dậy từ tương tác.
3. **Lack of ground truth**: không có "đáp án đúng" để biết diễn giải của ta khớp với cách model *thực sự* nghĩ hay chỉ là ảo giác thống kê.

Phương pháp chia hai nhánh bổ trợ: **observational** (đọc kích hoạt, probing, giảm chiều) và **causal** (can thiệp, ablation, patching). Tuần 1 chỉ cần vững nhánh quan sát; từ tuần 6 ta mới "cầm dao".

## Lab từng bước / Step-by-step lab

1. Tạo embedding $E\in\mathbb{R}^{V\times d}$ với seed cố định; mã hoá một câu nhỏ thành chỉ số token. / Build a seeded embedding and encode a small sentence.
2. Chạy [`01_residual_stream.py`](../code/week01/01_residual_stream.py), quan sát vector token dịch chuyển qua từng block và khoảng cách so với vị trí đầu. / Watch the token vector move block by block.
3. Chạy [`02_linear_probe_baseline.py`](../code/week01/02_linear_probe_baseline.py), so sánh một mô hình tuyến tính (diễn giải được) với một mô hình phi tuyến (hộp đen). / Compare a linear (interpretable) model with a nonlinear (black-box) one.
4. Ghi lại một "model card quan sát": seed, chiều $d$, số block, metric đo, và một nhận xét định tính. / Record an observational model card.

## Liên kết code / Code links

- [`../code/week01/01_residual_stream.py`](../code/week01/01_residual_stream.py) — mô phỏng residual stream.
- [`../code/week01/02_linear_probe_baseline.py`](../code/week01/02_linear_probe_baseline.py) — linear probe và baseline.

## Câu hỏi thảo luận / Discussion questions

1. Vì sao một neuron đơn lẻ thường *không* là một "khái niệm"? / Why is a single neuron usually not a concept?
2. Khi nào observational đủ, khi nào phải cần causal? / When is observation enough and when is intervention required?
3. "Mô hình dự đoán đúng" khác "mô hình dễ hiểu" thế nào? / How does "predicts correctly" differ from "easy to understand"?
4. Thiếu ground truth ảnh hưởng gì tới việc công bố một diễn giải? / How does the lack of ground truth affect claiming an interpretation?

## Bài tập về nhà / Homework

- **Cơ bản**: chạy hai script, chép lại output, giải thích mỗi số liệu nghĩa là gì.
- **Nâng cao**: đổi seed và số block, quan sát khoảng cách residual thay đổi thế nào; ghi nhận xét.
- **Thử thách**: tự viết một "probe" nhỏ (hồi quy logistic thuần NumPy) phân loại hai nhóm vector giả, và đánh giá độ tin cậy khi chỉ có vài chục mẫu.

## Yêu cầu nộp / Submission

- 1 file `.md` hoặc notebook gồm: output đã chạy, model card, và câu trả lời bài tập. Nộp theo đường dẫn thầy chỉ định.

## Rubric (100 điểm) / Assessment rubric

| Tiêu chí | Điểm |
|---|---:|
| Đúng chức năng: script chạy, số liệu đúng, baseline hợp lệ | 35 |
| An toàn & xử lý lỗi: seed tái lập, không tải model thật, ghi rõ phạm vi | 25 |
| Chất lượng code/tài liệu: chú thích Việt, đặt tên rõ, dễ đọc | 20 |
| Phân tích: diễn giải số liệu, nêu giới hạn, bằng chứng chạy | 20 |

## Lưu ý an toàn / Safety notes

- Chỉ chạy trên dữ liệu/mô hình giả local. Không cần và không nên tải model lớn thật ở tuần này.
- Giữ seed cố định để tái lập; không đọc kết quả một lần rồi kết luận.
- Diễn giải là giả thuyết hỗ trợ, không phải chứng minh cuối cùng — ghi rõ giới hạn.
