---
layout: course
title: "Week01"
permalink: /5_Applications/llm-applications-10weeks/lessons/week01.html
---

# Tuần 1 — Đánh giá mô hình: mục tiêu, metric cơ bản và bẫy / Week 1 — Model evaluation: goals, core metrics and pitfalls

[Mục lục khoá](../INDEX.md) · [Lịch](../schedule.md) · [Tuần 2 →](week02.md)

## Mục tiêu học tập / Learning objectives

- Phân biệt ba mục tiêu đánh giá: đo **khả năng** (capability), đo **chất lượng đầu ra** (quality) và đo **an toàn** (safety). / Distinguish measuring capability, output quality, and safety.
- Tính và diễn giải accuracy, precision, recall, F1, exact match; nhận biết bẫy class imbalance. / Compute accuracy/precision/recall/F1/EM and identify class-imbalance traps.
- Tính log-likelihood và perplexity; nhận biết vì sao perplexity phụ thuộc tokenization. / Compute log-likelihood and perplexity; explain tokenizer dependence.
- Phát biểu một "evaluation contract": dữ liệu, split, seed, metric, đơn vị token, hardware. / State an evaluation contract.

## Công cụ / dữ liệu

- Python 3 chuẩn (`math`, `statistics`, `random`), không cần thư viện ngoài.
- Dữ liệu giả: tập nhãn phân loại và chuỗi token nhỏ.
- Nguồn lý thuyết: [`../../../docs/09_quantitative_evaluations/index.md`](../../../docs/09_quantitative_evaluations/index.md) (perplexity, numerical issues in softmax).

## Lý thuyết + ví dụ / Theory + examples

Với chuỗi token $x_{1:T}$, cross-entropy là trung bình âm log xác suất:

$$\mathcal L = -\frac1T\sum_{t=1}^T \log p_\theta(x_t\mid x_{<t}), \qquad \mathrm{PPL}=\exp(\mathcal L).$$

Perplexity là "số lựa chọn hiệu dụng" tại mỗi bước, không phải độ chính xác. Nó chỉ so sánh công bằng khi **tokenizer, split và preprocessing giống nhau**. / Perplexity is an effective branching factor; comparisons require identical tokenizer, split, and preprocessing.

Ba bẫy metric phổ biến:

1. **Class imbalance**: accuracy = 95% có thể chỉ là "đoán lớp đa số". Dùng precision/recall/F1 và báo baseline đa số. / Accuracy can hide a majority-class guess; report the majority baseline.
2. **Đơn vị token khác nhau**: cùng một văn bản, BPE khác nhau cho perplexity khác nhau. / Different token units invalidate direct comparison.
3. **Chỉ một metric duy nhất**: một điểm số không mô tả hành vi. Luôn đi kèm nhiều metric và mẫu lỗi. / A single number never describes behavior.

Ví dụ softmax ổn định số (tránh tràn `exp` khi logit lớn):

```python
import math
def softmax_stable(logits):
    m = max(logits)                 # Trừ max để tránh exp tràn số.
    e = [math.exp(z - m) for z in logits]
    s = sum(e)
    return [x / s for x in e]       # Tổng phân phối luôn bằng 1.
```

## Lab từng bước / Step-by-step lab

1. Tạo 100 nhãn giả lệch nặng (90 nhãn 0, 10 nhãn 1); so sánh accuracy của "đoán toàn 0" với F1.
2. Viết hàm tính precision/recall/F1 từ confusion matrix; kiểm tra các trường hợp biên (chia cho 0).
3. Tính NLL/perplexity cho một chuỗi xác suất nhỏ; xác nhận `exp(log)` ổn định.
4. Viết "evaluation contract" 5 dòng cho một bài toán bạn chọn.

## Liên kết code / Code links

- [`../code/week01/01_metrics.py`](../code/week01/01_metrics.py) — confusion matrix, precision/recall/F1, bẫy imbalance.
- [`../code/week01/02_calibration.py`](../code/week01/02_calibration.py) — softmax ổn định, log-prob, perplexity.

## Câu hỏi thảo luận / Discussion questions

1. Khi nào accuracy cao nhưng mô hình vẫn vô dụng? Cho ví dụ. / When is high accuracy still useless?
2. Vì sao không so sánh perplexity giữa hai tokenizer khác nhau? / Why can't perplexity cross tokenizers?
3. "Đo khả năng" khác "đo an toàn" thế nào trong một ứng dụng chatbot? / How do capability and safety evaluations differ?
4. Bạn cần log gì để tái lập một con số metric? / What must be logged to reproduce a metric?

## Bài tập / Homework

- **Cơ bản**: Tính accuracy/precision/recall/F1 và baseline đa số cho một tập nhãn giả lệch; giải thích số nào đáng tin nhất.
- **Nâng cao**: Cài hàm softmax ổn định và perplexity; viết test xác nhận tổng phân phối = 1 và perplexity hữu hạn với token chưa thấy.
- **Thử thách**: Dựng một "evaluation contract" hoàn chỉnh cho đánh giá một chatbot (dữ liệu, split, seed, metric chính/phụ, đơn vị token, giới hạn).

## Yêu cầu nộp / Submission

- 1 file Python + 1 file báo cáo ngắn (markdown) gồm: bảng metric, baseline, 3 mẫu lỗi, contract.
- Ghi rõ seed và dữ liệu dùng; không cần API hay mô hình thật.

## Rubric (100 điểm)

| Tiêu chí | Điểm |
|---|---:|
| Đúng chức năng: công thức metric chính xác, xử lý biên, chạy được | 35 |
| An toàn & xử lý lỗi: validate đầu vào, tránh chia 0, không log secret | 25 |
| Chất lượng code/tài liệu: chú thích đúng chỗ, dễ đọc | 20 |
| Phân tích & bằng chứng: baseline, mẫu lỗi, giải thích metric | 20 |

## ⚠️ Lưu ý an toàn / Safety notes

- Chỉ chạy trên dữ liệu giả/local.
- Không dùng perplexity như "điểm thông minh"; nó chỉ đo khớp phân phối.
- Khi đánh giá mô hình thật, chỉ dùng mô hình bạn sở hữu/được ủy quyền và ghi rõ nguồn dữ liệu.
