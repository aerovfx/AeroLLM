---
layout: course
title: "Week08"
permalink: /1_Foundations/python-math-foundations-10weeks/lessons/week08.html
---

# Tuần 8 — Toán cho deep learning / Week 8 — Math for deep learning

[← Tuần 7](week07.md) · [← Tổng quan](../INDEX.md) · [Tuần 9 →](week09.md)

## Mục tiêu học tập / Learning objectives

- Tính chuyển vị, tổ hợp tuyến tính và tích vô hướng (dot product). / Compute transpose, linear combination, and dot product.
- Nhân ma trận và kiểm tra quy tắc kích thước. / Multiply matrices and check the size rule.
- Cài đặt softmax và giải thích tại sao nó cho phân phối xác suất. / Implement softmax and explain why it yields a probability distribution.
- Tính entropy/cross-entropy và nêu liên hệ với hàm mất mát. / Compute entropy/cross-entropy and relate it to a loss function.
- Mô tả đạo hàm như độ dốc và dùng quy tắc chuỗi (chain rule). / Describe the derivative as a slope and use the chain rule.

## Công cụ và dữ liệu / Tools and data

- Python 3.10+, NumPy. Dữ liệu giả là các vector/ma trận số.

## Lý thuyết cô đọng + ví dụ / Concise theory + example

Tích vô hướng của hai vector cùng độ dài: $x\cdot y=\sum_i x_i y_i$. Tổ hợp tuyến tính: $w_1 x_1 + w_2 x_2 + b$. Nhân ma trận $A_{m\times k}B_{k\times n}$ chỉ hợp lệ khi số cột của $A$ bằng số hàng của $B$, kết quả là ma trận $m\times n$.

```python
import numpy as np
x = np.array([1.0, 2.0])
w = np.array([0.5, -0.5])
print(np.dot(x, w))          # Tích vô hướng = 1*0.5 + 2*(-0.5) = -0.5.

A = np.array([[1, 2], [3, 4]])   # 2x2.
B = np.array([[5, 6], [7, 8]])   # 2x2.
print(A @ B)                     # Nhân ma trận (toán tử @).
```

Softmax biến vector thành phân phối xác suất (tổng bằng 1): $\mathrm{softmax}(z)_i = \frac{e^{z_i}}{\sum_j e^{z_j}}$. Trừ đi giá trị lớn nhất trước khi lấy mũ để tránh tràn số (numerical stability).

```python
def softmax(z):
    z = z - np.max(z)          # Ổn định số: tránh e^z quá lớn.
    e = np.exp(z)
    return e / e.sum()

print(softmax(np.array([2.0, 1.0, 0.0])))  # Tổng = 1.
```

Entropy đo độ bất định của phân phối: $H(p)=-\sum_i p_i\log p_i$. Cross-entropy $H(p,q)=-\sum_i p_i\log q_i$ đo độ "lệch" khi dùng $q$ thay cho $p$, là nền tảng của hàm mất mát phân loại.

## Lab từng bước / Step-by-step lab

1. Tính tích vô hướng hai vector bằng vòng lặp rồi bằng `np.dot`, so sánh.
2. Tính tổ hợp tuyến tính $w_1 x_1 + w_2 x_2 + b$ cho vài bộ trọng số.
3. Nhân hai ma trận 2×3 và 3×2; thử nhân sai kích thước và đọc lỗi.
4. Cài đặt softmax có trừ max; kiểm tra tổng bằng 1.
5. Tính entropy của phân phối đều và phân phối "chắc chắn", so sánh.
6. Tính cross-entropy giữa nhãn one-hot và xác suất dự đoán.

## Liên kết code mẫu / Sample code links

- [`code/week08/01_vector_matrix.py`](../code/week08/01_vector_matrix.py) — dot product, tổ hợp tuyến tính, nhân ma trận.
- [`code/week08/02_softmax_entropy.py`](../code/week08/02_softmax_entropy.py) — softmax, entropy, cross-entropy.
- Xem README: [`code/week08/README.md`](../code/week08/README.md).

## Câu hỏi thảo luận / Discussion questions

1. Vì sao softmax cần trừ max trước khi lấy mũ? / Why subtract the max before exponentiating in softmax?
2. Khi nào cross-entropy bằng 0? / When is cross-entropy zero?
3. Đạo hàm cho ta biết gì về hướng cập nhật tham số? / What does the derivative tell us about the update direction?
4. Vì sao nhân ma trận là phép toán "xương sống" của mạng nơ-ron? / Why is matrix multiplication the backbone of neural networks?

## Bài tập / Exercises

- **Cơ bản:** Tính tích vô hướng và nhân hai ma trận; kiểm tra kích thước kết quả. / Compute a dot product and a matrix product; verify the result size.
- **Nâng cao:** Cài đặt softmax ổn định số và kiểm chứng tổng bằng 1 với nhiều vector. / Implement numerically stable softmax and verify the sum is 1 for several vectors.
- **Thử thách:** Tính cross-entropy cho một bài phân loại 3 lớp; vẽ đồ thị giá trị loss theo độ tự tin của dự đoán. / Compute cross-entropy for a 3-class problem and plot loss versus prediction confidence.

## Yêu cầu nộp bài / Submission requirements

Nộp script kèm kết quả; giải thích từng công thức bằng lời và nêu một lỗi kích thước ma trận bạn gặp.

## Rubric 100 điểm / 100-point rubric

| Hạng mục | Xuất sắc | Đạt | Cần cải thiện | Chưa đạt | Điểm |
|---|---|---|---|---|---|
| Đúng chức năng | Công thức đúng, softmax ổn định số | Đúng luồng chính | Thiếu một phần | Không chạy | 35 |
| Xử lý lỗi/an toàn | Trừ max, kiểm tra kích thước, tránh log(0) | Có kiểm soát | Thiếu guardrail | Tràn số/NaN | 25 |
| Chất lượng code/tài liệu | Chú thích rõ công thức | Dễ đọc | Khó bảo trì | Không giải thích | 20 |
| Phân tích/giải thích | Liên hệ đúng loss, giải thích numerical stability | Có giải thích | Sơ sài | Không có | 20 |

## Lưu ý an toàn / Safety notes

Các phép toán chỉ trên dữ liệu giả trong bộ nhớ. Tránh `log(0)` bằng cách thêm epsilon nhỏ; tránh mũ số quá lớn gây tràn (overflow) làm hỏng kết quả.

## Nguồn tham khảo / Source

- [Module 27 — Math for deep learning](../../../docs/27_math_deep_learning/index.md)
