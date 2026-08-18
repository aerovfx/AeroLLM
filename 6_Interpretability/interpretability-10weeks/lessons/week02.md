---
layout: course
title: "Week02"
permalink: /6_Interpretability/interpretability-10weeks/lessons/week02.html
---

# Tuần 2 — Identifying circuits / Week 2 — Identifying circuits

[Mục lục khoá](../INDEX.md) · [Tài liệu nguồn](../../../docs/10_identifying_circuits/index.md) · [← Tuần 1](week01.md) · [Tuần 3 →](week03.md)

## Mục tiêu học tập / Learning objectives

- Định nghĩa "circuit" là một tập nhỏ các thành phần (neuron/head) phối hợp thực hiện một chức năng. / Define a circuit as a small set of components performing one function.
- Giải thích sparse probing: hồi quy logistic + phạt L1 để ép hệ số về 0, tìm tập neuron tối thiểu. / Explain sparse probing as logistic regression with L1 penalty.
- Mô tả sparse autoencoder (SAE) như cách khôi phục feature thưa từ biểu diễn dày đặc. / Describe an SAE as recovering sparse features from dense activations.
- Chạy được sparse probe và SAE toy trên dữ liệu giả, đọc "mạch" tìm được. / Run a sparse probe and a toy SAE and read out the discovered circuit.

## Công cụ và dữ liệu / Tools and data

- Python 3 + NumPy; dữ liệu giả mô phỏng kích hoạt MLP (vài nghìn neuron, phần lớn nhiễu).
- [`../code/week02/01_sparse_probe.py`](../code/week02/01_sparse_probe.py) và [`../code/week02/02_sae_toy.py`](../code/week02/02_sae_toy.py).

## Lý thuyết / Theory

Một mô hình học sâu không lưu trữ một khái niệm ở một chỗ; nó tổ chức thành các **mạch** (circuits): tập nhỏ thành phần, mỗi thành phần làm một việc nhỏ, ghép lại thành chức năng lớn hơn. Muốn "tìm mạch", ta cần một công cụ ép thưa (sparsity): giữ lại ít neuron, loại phần còn lại.

**Sparse probing** dùng hồi quy logistic với hàm phạt L1:

$$\mathcal{L} = \underbrace{-\tfrac1n\sum_i\big[y_i\log p_i + (1-y_i)\log(1-p_i)\big]}_{\text{BCE}} + \lambda\sum_k|\beta_k|$$

Phạt L1 kéo nhiều $\beta_k$ về đúng 0; hệ số $\lambda$ (hay $C=1/\lambda$) điều khiển độ thưa. Kết quả: chỉ vài neuron "sống sót" mà vẫn phân loại chính xác — đó chính là ứng viên mạch. Trên GPT-2 Small, một sparse probe cho cặp "the/an" có thể đạt ~99% độ thưa, giữ lại khoảng chục neuron.

**Sparse autoencoder (SAE)** là một lớp tuyến tính học mã hoá $z=\text{ReLU}(W_{enc}\,h+b)$ rồi tái tạo $\hat h = W_{dec}\,z$, với phạt thưa lên $z$. Nó tách biểu diễn dày đặc thành các **feature** hiếm khi cùng bật — gần với "đơn vị ngữ nghĩa" hơn là neuron thô. Lưu ý giới hạn: trên dữ liệu nhỏ, L1 dễ bị *statistical suppression* — tín hiệu thật bị nhiễu lấn át và bị ép về 0 nhầm.

## Lab từng bước / Step-by-step lab

1. Sinh kích hoạt giả: một số ít neuron mang tín hiệu phân loại, phần còn lại là nhiễu. / Generate fake activations where few neurons carry signal.
2. Chạy [`01_sparse_probe.py`](../code/week02/01_sparse_probe.py), tăng/giảm $\lambda$ và quan sát độ thưa đổi thế nào. / Tune λ and watch sparsity change.
3. Chạy [`02_sae_toy.py`](../code/week02/02_sae_toy.py), so sánh feature học được với feature "thật" đã cấy vào dữ liệu. / Compare learned SAE features to the planted ground-truth features.
4. Lập bảng: (λ, accuracy, số neuron sống, nhận xét). / Build a table of λ vs accuracy vs surviving neurons.

## Liên kết code / Code links

- [`../code/week02/01_sparse_probe.py`](../code/week02/01_sparse_probe.py) — sparse probing (logistic + L1).
- [`../code/week02/02_sae_toy.py`](../code/week02/02_sae_toy.py) — sparse autoencoder tối giản.

## Câu hỏi thảo luận / Discussion questions

1. Tại sao accuracy cao nhưng mạch lại cực nhỏ lại là phát hiện đáng giá? / Why is a tiny circuit with high accuracy valuable?
2. $\lambda$ quá lớn gây ra lỗi gì, $\lambda$ quá nhỏ gây ra lỗi gì? / What errors do too-large and too-small λ cause?
3. Sparse probe khác SAE ở mục tiêu như thế nào? / How do sparse probing and SAE differ in goal?
4. "Statistical suppression" là gì và vì sao nguy hiểm khi dùng tập dữ liệu nhỏ? / What is statistical suppression and why is it risky on small data?

## Bài tập về nhà / Homework

- **Cơ bản**: chạy hai script, ghi lại mạch tìm được (chỉ số neuron / feature) và độ chính xác.
- **Nâng cao**: quét 5 giá trị $\lambda$, vẽ (bằng tay hoặc bảng) đường accuracy vs số neuron sống, tìm điểm gãy.
- **Thử thách**: cấy 2 feature tương quan nhau vào dữ liệu và xem sparse probe có tách được chúng không; giải thích.

## Yêu cầu nộp / Submission

- Bảng kết quả + danh sách mạch + nhận xét giới hạn, nộp theo đường dẫn thầy chỉ định.

## Rubric (100 điểm) / Assessment rubric

| Tiêu chí | Điểm |
|---|---:|
| Đúng chức năng: probe/SAE chạy, mạch tìm đúng feature đã cấy | 35 |
| An toàn & xử lý lỗi: seed, xử lý hội tụ, không overfit dữ liệu nhỏ | 25 |
| Chất lượng code/tài liệu: chú thích, đặt tên, cấu trúc rõ | 20 |
| Phân tích: đọc đúng độ thưa, nêu statistical suppression, bằng chứng | 20 |

## Lưu ý an toàn / Safety notes

- Chỉ chạy trên kích hoạt giả local; không tự ý trích xuất kích hoạt từ model lớn chưa được cấp quyền.
- Cẩn thận với kết luận từ dữ liệu nhỏ: độ thưa cao có thể là suppression, không phải mạch thật.
- Ghi seed và số epoch để tái lập; kiểm tra hội tụ trước khi kết luận.
