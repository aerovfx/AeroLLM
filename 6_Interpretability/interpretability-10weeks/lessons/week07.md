---
layout: course
title: "Week07"
permalink: /6_Interpretability/interpretability-10weeks/lessons/week07.html
---

# Tuần 7 — Editing hidden states / Week 7 — Editing hidden states

[Mục lục khoá](../INDEX.md) · [Tài liệu nguồn](../../../docs/15_editing_hidden_states/index.md) · [← Tuần 6](week06.md) · [Tuần 8 →](week08.md)

## Mục tiêu học tập / Learning objectives

- Định nghĩa activation patching: ghi đè hidden state tại (vị trí, tầng) bằng giá trị "sạch" từ ngữ cảnh khác. / Define activation patching as overwriting a hidden state with another context's value.
- Mô tả tác vụ IOI (Indirect Object Identification) và metric logit difference giữa hai ứng viên. / Describe the IOI task and its logit-difference metric.
- Giải thích hiện tượng "chuyển pha theo tầng": tầng sớm kháng nhiễu, tầng giữa-cuối nhạy cảm. / Explain the layer-wise phase transition in patching.
- Chạy được patching và skip-a-layer trên mô hình giả, đọc bản đồ ảnh hưởng. / Run patching and skip-a-layer and read the influence map.

## Công cụ và dữ liệu / Tools and data

- Python 3 + NumPy; cặp câu donor/recipient giả cho tác vụ IOI với mô hình giả biết trước đáp án.
- [`../code/week07/01_activation_patching_ioi.py`](../code/week07/01_activation_patching_ioi.py) và [`../code/week07/02_skip_layer.py`](../code/week07/02_skip_layer.py).

## Lý thuyết / Theory

**Activation patching** là công cụ định vị "thông tin ở đâu, lúc nào". Cho hai câu chỉ khác ở một token (donor và recipient), ta chạy forward câu đích nhưng tại một vị trí/tầng cụ thể, ghi đè hidden state bằng giá trị lấy từ câu nguồn. Nếu dự đoán cuối cùng "lật" sang đáp án của câu nguồn, thì vị trí đó thực sự mang thông tin quyết định.

Tác vụ **IOI** là chuẩn để đo: "Bob and Barbara went to the beach. Bob gave the umbrella to ___". Đáp án đúng ngữ pháp là Barbara (tân ngữ gián tiếp). Metric là chênh lệch logit giữa hai ứng viên:

$$\Delta = \log p(\text{Barbara}) - \log p(\text{Bob})$$

Kết quả kinh điển (trên GPT-2 XL): patching ở tầng sớm gần như vô hại (mô hình vẫn trả lời theo câu đích), còn từ tầng giữa trở đi xảy ra **phase transition** — mô hình đột ngột tin theo thông tin được vá. Điều này cho thấy quan hệ ngữ pháp/thực thể được tích hợp ở nửa sau mạng.

**Skip a layer** là một can thiệp thô hơn: bỏ hẳn một block (nối residual thẳng). Nó đo "tầng này có quan trọng không" ở mức thô, và cũng bộc lộ tính dư thừa của mạng.

## Lab từng bước / Step-by-step lab

1. Chạy [`01_activation_patching_ioi.py`](../code/week07/01_activation_patching_ioi.py), quan sát logit difference theo từng tầng được vá. / Watch logit difference across patched layers.
2. Xác định tầng bắt đầu "chuyển pha" trong mô hình giả. / Identify the phase-transition layer.
3. Chạy [`02_skip_layer.py`](../code/week07/02_skip_layer.py), so sánh tác động bỏ tầng sớm vs tầng cuối. / Compare skipping early vs late layers.
4. Vẽ bản đồ ảnh hưởng (heatmap vị trí × tầng) nếu đủ thời gian. / Draw an influence heatmap if time permits.

## Liên kết code / Code links

- [`../code/week07/01_activation_patching_ioi.py`](../code/week07/01_activation_patching_ioi.py) — patching + IOI metric.
- [`../code/week07/02_skip_layer.py`](../code/week07/02_skip_layer.py) — bỏ qua một tầng.

## Câu hỏi thảo luận / Discussion questions

1. Vì sao tầng sớm "phớt lờ" giá trị được vá? / Why do early layers ignore patched values?
2. Phase transition nói gì về nơi tích hợp quan hệ thực thể? / What does the phase transition say about where entity relations are integrated?
3. Patching khác ablation (zero-out) ở chỗ nào về mặt thông tin? / How does patching differ from ablation informationally?
4. Skip-a-layer đo được gì mà patching không đo? / What does skip-a-layer measure that patching doesn't?

## Bài tập về nhà / Homework

- **Cơ bản**: chạy hai script, báo cáo tầng chuyển pha và tác động skip từng tầng.
- **Nâng cao**: vá tại nhiều vị trí token khác nhau (chủ ngữ vs tân ngữ) và so mức ảnh hưởng.
- **Thử thách**: dựng heatmap vị trí × tầng cho một metric, và dùng nó để khoanh vùng "mạch IOI" trong mô hình giả.

## Yêu cầu nộp / Submission

- Bảng logit difference theo tầng + bản đồ ảnh hưởng + nhận xét, nộp theo đường dẫn thầy chỉ định.

## Rubric (100 điểm) / Assessment rubric

| Tiêu chí | Điểm |
|---|---:|
| Đúng chức năng: patching/skip đúng, metric IOI đúng | 35 |
| An toàn & xử lý lỗi: donor/recipient tách bạch, baseline, seed | 25 |
| Chất lượng code/tài liệu: chú thích, cấu trúc rõ | 20 |
| Phân tích: xác định chuyển pha, nêu tính dư thừa | 20 |

## Lưu ý an toàn / Safety notes

- Chỉ patching mô hình giả local; không dùng để "sửa" hành vi model thật khi chưa được phép.
- Chuyển pha quan sát trên một mô hình không phải quy luật phổ quát; ghi rõ điều kiện.
- Giữ cặp donor/recipient chỉ khác đúng một biến để kết luận nhân quả sạch.
