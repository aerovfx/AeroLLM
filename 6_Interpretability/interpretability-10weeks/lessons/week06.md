---
layout: course
title: "Week06"
permalink: /6_Interpretability/interpretability-10weeks/lessons/week06.html
---

# Tuần 6 — Modify activations / Week 6 — Modify activations

[Mục lục khoá](../INDEX.md) · [Tài liệu nguồn](../../../docs/14_modify_activations/index.md) · [← Tuần 5](week05.md) · [Tuần 7 →](week07.md)

## Mục tiêu học tập / Learning objectives

- Chuyển từ quan sát (observational) sang nhân quả (causal): can thiệp để kiểm chứng giả thuyết. / Move from observational to causal interpretation via intervention.
- Phân biệt các chế độ sửa kích hoạt: zero-out, thay bằng mean, thay bằng median, bơm nhiễu, thay bằng giá trị từ ngữ cảnh khác (patching). / Distinguish activation-editing modes: zero, mean, median, noise, cross-context patching.
- Giải thích ba khó khăn của can thiệp nhân quả: vô số lựa chọn, tính bù trừ của mạng, thiếu ground truth. / Explain the three challenges: limitless choices, network compensation, no ground truth.
- Chạy được một can thiệp có baseline và đo logit difference. / Run an intervention with a clean baseline and measure logit difference.

## Công cụ và dữ liệu / Tools and data

- Python 3 + NumPy; mô hình giả có một "mạch" cấy sẵn để biết trước đáp án can thiệp.
- [`../code/week06/01_activation_editing.py`](../code/week06/01_activation_editing.py) và [`../code/week06/02_counterfactual_patching.py`](../code/week06/02_counterfactual_patching.py).

## Lý thuyết / Theory

Quan sát cho biết một neuron *tương quan* với một hành vi; can thiệp cho biết nó *gây ra* hành vi đó. Đây là điểm chuyển từ "đọc" sang "viết".

Các chế độ sửa kích hoạt $h$ tại một vị trí (position, layer):

- **Zero-out**: $h \leftarrow 0$ — mạnh, dễ gây sốc.
- **Mean**: $h \leftarrow \bar h$ (trung bình trên tập) — "trung hoà" nhưng giữ thang đo.
- **Median**: $h \leftarrow \text{median}$ — bền hơn trước outlier.
- **Noise**: $h \leftarrow h + \epsilon$ — đo độ nhạy nhiễu.
- **Patching**: $h \leftarrow h'$ lấy từ một ngữ cảnh khác — "cấy" thông tin từ câu nguồn sang câu đích.

Ba khó khăn cốt lõi:

1. **Limitless choices**: có vô số vị trí và cách sửa; cần giả thuyết dẫn đường, không thử mù.
2. **Compensation**: LayerNorm/dropout khiến mạng tự "gánh tạ" và định tuyến lại tín hiệu; can thiệp có thể không đổi output.
3. **No ground truth**: không có đáp án chuẩn để biết thay đổi là do mạch hỏng hay do bơm nhiễu out-of-distribution.

Vì vậy luôn đo bằng **logit difference** $\Delta = \log p(\text{target}) - \log p(\text{contrast})$, so với baseline sạch, và quét nhiều mức cường độ (scale) thay vì một phép nhị phân.

## Lab từng bước / Step-by-step lab

1. Chạy [`01_activation_editing.py`](../code/week06/01_activation_editing.py), so sánh zero/mean/median/noise lên cùng một vị trí. / Compare editing modes at one site.
2. Chạy [`02_counterfactual_patching.py`](../code/week06/02_counterfactual_patching.py), vá giá trị từ câu nguồn vào câu đích và quan sát dự đoán "lật". / Patch source value into target and watch the prediction flip.
3. Quét cường độ scale $0, 0.25, \dots, 1$ và vẽ logit difference theo scale. / Sweep scale and plot logit difference.
4. Ghi nhận xét: vị trí nào "nhạy", vị trí nào "được bù trừ". / Note which sites are sensitive vs compensated.

## Liên kết code / Code links

- [`../code/week06/01_activation_editing.py`](../code/week06/01_activation_editing.py) — các chế độ sửa kích hoạt.
- [`../code/week06/02_counterfactual_patching.py`](../code/week06/02_counterfactual_patching.py) — patching phản thực.

## Câu hỏi thảo luận / Discussion questions

1. Vì sao zero-out thường cho kết quả "không thay đổi gì"? / Why does zero-out often change nothing?
2. Khi nào nên dùng median thay vì mean? / When to use median instead of mean?
3. "Compensation" khiến kết luận nhân quả khó thế nào? / How does compensation complicate causal conclusions?
4. Làm sao phân biệt "mạch hỏng" với "nhiễu out-of-distribution"? / How to distinguish a broken circuit from OOD noise?

## Bài tập về nhà / Homework

- **Cơ bản**: chạy hai script, lập bảng chế độ × logit difference.
- **Nâng cao**: quét scale cho 2 vị trí khác nhau, so sánh độ dốc (nhạy cảm).
- **Thử thách**: thiết kế một giả thuyết nhân quả cụ thể ("neuron X gây ra phân biệt A/B") rồi dùng patching để bác bỏ hoặc ủng hộ nó.

## Yêu cầu nộp / Submission

- Bảng can thiệp + đồ thị scale + giả thuyết nhân quả và kết luận, nộp theo đường dẫn thầy chỉ định.

## Rubric (100 điểm) / Assessment rubric

| Tiêu chí | Điểm |
|---|---:|
| Đúng chức năng: can thiệp đúng vị trí, logit difference đúng | 35 |
| An toàn & xử lý lỗi: baseline sạch, xử lý scale, seed | 25 |
| Chất lượng code/tài liệu: chú thích, cấu trúc rõ | 20 |
| Phân tích: giả thuyết rõ, nêu compensation/ground truth | 20 |

## Lưu ý an toàn / Safety notes

- Chỉ can thiệp mô hình giả local; không sửa mô hình đang phục vụ thật.
- Một lần chạy không đủ kết luận: quét nhiều mức cường độ, so baseline.
- Ghi rõ giả thuyết trước khi chạy để tránh "fishing" (thử tới khi có kết quả ưng ý).
