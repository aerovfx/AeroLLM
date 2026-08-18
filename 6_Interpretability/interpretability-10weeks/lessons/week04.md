---
layout: course
title: "Week04"
permalink: /6_Interpretability/interpretability-10weeks/lessons/week04.html
---

# Tuần 4 — Neurons và dimensions / Week 4 — Neurons and dimensions

[Mục lục khoá](../INDEX.md) · [Tài liệu nguồn](../../../docs/12_investigating_neurons_dimensions/index.md) · [← Tuần 3](week03.md) · [Tuần 5 →](week05.md)

## Mục tiêu học tập / Learning objectives

- Giải thích activation maximization: tối ưu đầu vào để làm một neuron "bật" mạnh nhất. / Explain activation maximization as optimizing input to maximize a neuron.
- Dùng hook (khái niệm) để trích kích hoạt tại một vị trí cụ thể giữa forward pass. / Use hooks to extract activations at a specific point mid-forward.
- Đo "tính chọn lọc" của neuron bằng hồi quy logistic và kiểm định t-test, phân biệt hai công cụ. / Measure neuron selectivity with logistic regression and a t-test, and contrast them.
- Nêu khó khăn của từ đa token (multi-token words) khi gán "ý nghĩa" cho một neuron. / State the difficulty of multi-token words when labeling a neuron.

## Công cụ và dữ liệu / Tools and data

- Python 3 + NumPy; một mạng nhỏ 2 lớp giả lập MLP có neuron "biết" một đặc trưng cấy sẵn.
- [`../code/week04/01_activation_maximization.py`](../code/week04/01_activation_maximization.py) và [`../code/week04/02_neuron_selectivity.py`](../code/week04/02_neuron_selectivity.py).

## Lý thuyết / Theory

Một neuron (hay một chiều của kích hoạt) có thể "thích" một đặc trưng nào đó. Hai cách hỏi:

1. **Activation maximization**: giữ trọng số cố định, tối ưu *đầu vào* $x$ bằng gradient ascent để cực đại hoá kích hoạt $a_i(x)$ của neuron $i$. Kết quả là "hình ảnh/kích thích mà neuron thích nhất". Với LLM, đầu vào là embedding liên tục, nên ta thường kết hợp với "data sampling" (tìm mẫu thật kích hoạt mạnh nhất) vì tối ưu trực tiếp dễ rơi vào nhiễu.

2. **Selectivity (probe)**: thu thập kích hoạt $a_i$ trên nhiều mẫu có nhãn (ví dụ "danh từ riêng" vs "khác"), rồi hỏi "neuron này có phản ứng khác biệt giữa hai nhóm không?". Hai công cụ thống kê:
   - **Logistic regression**: học $p(y\mid a_i)$, cho ta đường phân loại và khả năng dự đoán nhãn từ neuron.
   - **t-test**: kiểm định giả thuyết "trung bình $a_i$ hai nhóm bằng nhau", cho p-value.

Chúng trả lời câu hỏi khác nhau: logistic đo *năng lực phân tách*, t-test đo *khác biệt trung bình có ý nghĩa thống kê*. Với từ đa token (ví dụ "playing" = "play"+"ing"), kích hoạt của một neuron trải trên nhiều token, nên việc gán một nhãn duy nhất trở nên mơ hồ.

## Lab từng bước / Step-by-step lab

1. Chạy [`01_activation_maximization.py`](../code/week04/01_activation_maximization.py), quan sát đầu vào tối ưu hội tụ về đặc trưng neuron thích. / Watch optimized input converge toward the neuron's preferred feature.
2. Chạy [`02_neuron_selectivity.py`](../code/week04/02_neuron_selectivity.py), so sánh kết luận từ logistic regression và t-test trên cùng dữ liệu. / Compare logistic regression vs t-test conclusions.
3. Thử "hook" tưởng tượng: vẽ sơ đồ vị trí trích kích hoạt giữa forward pass (trước/sau GELU). / Sketch where a hook sits relative to GELU.
4. Ghi lại trường hợp cả hai công cụ "đồng ý" và trường hợp "bất đồng". / Record where the two tools agree and disagree.

## Liên kết code / Code links

- [`../code/week04/01_activation_maximization.py`](../code/week04/01_activation_maximization.py) — gradient ascent cực đại hoá neuron.
- [`../code/week04/02_neuron_selectivity.py`](../code/week04/02_neuron_selectivity.py) — logistic regression vs t-test.

## Câu hỏi thảo luận / Discussion questions

1. Vì sao activation maximization trực tiếp trên LLM hay ra nhiễu? / Why does direct activation maximization on LLMs often produce noise?
2. Logistic regression và t-test khác nhau ở giả định và kết luận nào? / How do logistic regression and t-test differ in assumptions and conclusions?
3. Khi nào một neuron "chọn lọc" nhưng vẫn không phải là mạch quan trọng? / When is a neuron selective yet not causally important?
4. Multi-token words gây khó gì cho việc gán nhãn neuron? / What problem do multi-token words cause for labeling?

## Bài tập về nhà / Homework

- **Cơ bản**: chạy hai script, báo cáo "đặc trưng" neuron tìm được và p-value/accuracy.
- **Nâng cao**: thêm nhiễu vào dữ liệu, xem t-test và logistic mất ý nghĩa khi nào; giải thích.
- **Thử thách**: viết data sampling đơn giản (quét 1000 vector giả, lấy top-k kích hoạt) và so với kết quả gradient ascent.

## Yêu cầu nộp / Submission

- Bảng neuron + đặc trưng + kết quả hai phép thử + nhận xét, nộp theo đường dẫn thầy chỉ định.

## Rubric (100 điểm) / Assessment rubric

| Tiêu chí | Điểm |
|---|---:|
| Đúng chức năng: tối ưu hội tụ, hai phép thử tính đúng | 35 |
| An toàn & xử lý lỗi: learning rate ổn định, seed, xử lý p-value | 25 |
| Chất lượng code/tài liệu: chú thích, cấu trúc hàm rõ | 20 |
| Phân tích: đối chiếu hai công cụ, nêu giới hạn multi-token | 20 |

## Lưu ý an toàn / Safety notes

- Chỉ tối ưu trên mạng giả local; không chạy gradient ascent lên model thật chưa được phép.
- p-value thấp không đồng nghĩa "quan trọng nhân quả"; đừng nhầm tương quan với nguyên nhân.
- Ghi learning rate và số bước để tái lập; cảnh báo hội tụ về nhiễu.
