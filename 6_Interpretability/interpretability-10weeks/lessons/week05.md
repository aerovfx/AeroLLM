---
layout: course
title: "Week05"
permalink: /6_Interpretability/interpretability-10weeks/lessons/week05.html
---

# Tuần 5 — Layers / Week 5 — Layers

[Mục lục khoá](../INDEX.md) · [Tài liệu nguồn](../../../docs/13_investigating_layers/index.md) · [← Tuần 4](week04.md) · [Tuần 6 →](week06.md)

## Mục tiêu học tập / Learning objectives

- Đo "số chiều hiệu quả" (effective dimensionality) của biểu diễn theo tầng bằng phổ giá trị riêng PCA. / Measure effective dimensionality per layer via PCA's eigenvalue spectrum.
- Dùng logit lens: đọc trực tiếp logit từ hidden state tầng trung gian qua ma trận unembedding. / Apply the logit lens to decode intermediate hidden states.
- Mô tả mutual information như phép đo phụ thuộc phi tuyến giữa biến, phân biệt với covariance. / Describe mutual information vs covariance.
- Vẽ "laminar profile": một đại lượng khảo sát dọc theo độ sâu mô hình. / Plot a laminar profile of a quantity across depth.

## Công cụ và dữ liệu / Tools and data

- Python 3 + NumPy; một dãy "tầng" giả lập biểu diễn token biến đổi dần, kèm ma trận unembedding.
- [`../code/week05/01_effective_dimensionality.py`](../code/week05/01_effective_dimensionality.py) và [`../code/week05/02_logit_lens.py`](../code/week05/02_logit_lens.py).

## Lý thuyết / Theory

Thông tin không phân bố đều theo độ sâu. Ta cần công cụ đo *dọc theo các tầng*.

**Effective dimensionality**: PCA tìm các hướng phương sai lớn nhất. Số chiều hiệu quả có thể định nghĩa là số thành phần cần để giải thích $p\%$ phương sai, hoặc entropy của phổ đã chuẩn hoá. Nếu biểu diễn "nằm gọn" trong ít chiều, số chiều hiệu quả thấp — gợi ý cấu trúc nén.

**Logit lens**: ở mỗi tầng, thay vì chờ đến cuối, ta nhân thẳng hidden state $h^{(l)}$ với ma trận unembedding $W_U$ để xem "model đang nghĩ token gì" tại tầng $l$:

$$logits^{(l)} = W_U\,h^{(l)}$$

Vẽ token có logit cao nhất theo từng tầng cho thấy dự đoán hình thành dần ra sao — một dạng "phim tư duy" của model.

**Mutual information** $I(X;Y)$ đo lượng thông tin biến này mang về biến kia, bắt được cả phụ thuộc phi tuyến mà covariance (tuyến tính) bỏ sót. Ước lượng MI trên biến liên tục nhiều chiều rất khó và nhạy với phương pháp binning/estimator — luôn ghi rõ cách ước lượng.

## Lab từng bước / Step-by-step lab

1. Chạy [`01_effective_dimensionality.py`](../code/week05/01_effective_dimensionality.py), quan sát số chiều hiệu quả tăng/giảm theo tầng. / Watch effective dimensionality change across layers.
2. Chạy [`02_logit_lens.py`](../code/week05/02_logit_lens.py), theo dõi token dự đoán "hiện dần" qua các tầng. / Trace the predicted token emerging across layers.
3. So sánh covariance và một ước lượng MI thô trên dữ liệu có phụ thuộc phi tuyến (script gợi ý trong bài tập). / Compare covariance with a rough MI estimate on nonlinear data.
4. Vẽ laminar profile của một đại lượng và chú thích chỗ "chuyển pha". / Plot a laminar profile and annotate phase changes.

## Liên kết code / Code links

- [`../code/week05/01_effective_dimensionality.py`](../code/week05/01_effective_dimensionality.py) — PCA + effective dimensionality.
- [`../code/week05/02_logit_lens.py`](../code/week05/02_logit_lens.py) — logit lens theo tầng.

## Câu hỏi thảo luận / Discussion questions

1. Số chiều hiệu quả cao hay thấp thì "dễ diễn giải" hơn? Vì sao? / Is high or low effective dimensionality easier to interpret?
2. Logit lens dựa trên giả định gì về $W_U$ và hidden state? Khi nào nó sai lệch? / What assumption underlies the logit lens?
3. Tại sao covariance bỏ sót phụ thuộc phi tuyến còn MI thì không? / Why does covariance miss nonlinear dependence but MI doesn't?
4. "Chuyển pha" theo tầng (như trong activation patching) gợi ý gì về phân công nhiệm vụ? / What does a layer-wise phase transition suggest about role division?

## Bài tập về nhà / Homework

- **Cơ bản**: chạy hai script, báo cáo số chiều hiệu quả mỗi tầng và chuỗi token logit lens.
- **Nâng cao**: thêm một ước lượng MI đơn giản (binning + histogram) cho hai biến có quan hệ phi tuyến, so với Pearson correlation.
- **Thử thách**: đổi cấu trúc tầng giả (thêm "tầng nén") và dự đoán trước — rồi kiểm chứng — số chiều hiệu quả thay đổi thế nào.

## Yêu cầu nộp / Submission

- Laminar profile + bảng + nhận xét về phân công theo tầng, nộp theo đường dẫn thầy chỉ định.

## Rubric (100 điểm) / Assessment rubric

| Tiêu chí | Điểm |
|---|---:|
| Đúng chức năng: PCA/logit lens đúng, profile hợp lệ | 35 |
| An toàn & xử lý lỗi: chuẩn hoá, xử lý ma trận suy biến, seed | 25 |
| Chất lượng code/tài liệu: chú thích, hàm tách bạch | 20 |
| Phân tích: đọc đúng profile, nêu giới hạn PCA/MI | 20 |

## Lưu ý an toàn / Safety notes

- Chỉ dùng biểu diễn giả local; logit lens trên model thật cần môi trường được cấp phép.
- Variance ≠ relevance: phương sai lớn không bảo đảm mang ý nghĩa; cảnh báo overinterpreting PCA.
- Ghi rõ cách ước lượng MI (binning/estimator) vì kết quả phụ thuộc mạnh vào nó.
