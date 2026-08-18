---
layout: course
title: "Week10"
permalink: /1_Foundations/python-math-foundations-10weeks/lessons/week10.html
---

# Tuần 10 — Bản chất mạng nơ-ron + capstone mini / Week 10 — Essence of neural networks + mini capstone

[← Tuần 9](week09.md) · [← Tổng quan](../INDEX.md) · [Đồ án](../projects/final_project.md)

## Mục tiêu học tập / Learning objectives

- Mô tả perceptron: tổng có trọng số + bias + hàm kích hoạt phi tuyến. / Describe the perceptron: weighted sum + bias + nonlinear activation.
- Giải thích vì sao cần phi tuyến (nonlinearity). / Explain why nonlinearity is necessary.
- Thực hiện lan truyền xuôi (forward pass) và tính mất mát (loss). / Perform a forward pass and compute the loss.
- Thực hiện lan truyền ngược (backpropagation) bằng autograd của PyTorch. / Perform backpropagation via PyTorch autograd.
- Gói gọn kiến thức 10 tuần vào một capstone mini. / Consolidate the 10 weeks into a mini capstone.

## Công cụ và dữ liệu / Tools and data

- Python 3.10+, PyTorch. Dữ liệu giả (bài toán hồi quy/classification nhỏ do bạn tạo).

## Lý thuyết cô đọng + ví dụ / Concise theory + example

Perceptron tính $z = x\cdot w + b$ rồi áp dụng hàm kích hoạt phi tuyến $\hat y=\sigma(z)$. Nếu bỏ phi tuyến, chồng nhiều tầng tuyến tính vẫn chỉ là một phép tuyến tính — không học được ranh giới cong. ReLU $\sigma(z)=\max(0,z)$ là hàm kích hoạt phổ biến.

Lan truyền xuôi: từ đầu vào tính dự đoán rồi tính mất mát, ví dụ MSE $\mathcal L=\frac1N\sum(\hat y - y)^2$. Lan truyền ngược: tính đạo hàm của loss theo tham số bằng autograd rồi cập nhật tham số bằng gradient descent.

```python
import torch

# Dữ liệu giả: y = 3x + 1 (có chút nhiễu).
x = torch.tensor([[1.0], [2.0], [3.0], [4.0]])
y = torch.tensor([[4.0], [7.0], [10.0], [13.0]])

w = torch.tensor([[0.0]], requires_grad=True)  # Tham số cần học.
b = torch.tensor([0.0], requires_grad=True)    # Bias cần học.
eta = 0.01                                     # Learning rate.

for epoch in range(200):
    y_hat = x @ w + b                         # Forward pass (tuyến tính).
    loss = ((y_hat - y) ** 2).mean()          # MSE loss.
    loss.backward()                           # Backward: tính đạo hàm.
    with torch.no_grad():                     # Cập nhật không cần grad.
        w -= eta * w.grad
        b -= eta * b.grad
    w.grad.zero_(); b.grad.zero_()            # Xoá gradient cho bước sau.
print("w =", round(w.item(), 3), "b =", round(b.item(), 3))  # ~3 và ~1.
```

## Lab từng bước / Step-by-step lab

1. Cài đặt perceptron thủ công bằng NumPy: `z = dot(x, w) + b`, `relu(z)`.
2. Giải thích vì sao bỏ ReLU khiến mô hình không học được quan hệ phi tuyến.
3. Chạy đoạn hồi quy tuyến tính PyTorch ở trên, quan sát `w` tiến về 3, `b` về 1.
4. Thêm ReLU vào mô hình và thử với dữ liệu phi tuyến (ví dụ $y=x^2$).
5. In loss mỗi 50 epoch để thấy loss giảm dần.
6. Bắt đầu capstone mini theo [`projects/final_project.md`](../projects/final_project.md).

## Liên kết code mẫu / Sample code links

- [`code/week10/01_perceptron.py`](../code/week10/01_perceptron.py) — perceptron thủ công.
- [`code/week10/02_linear_regression_pytorch.py`](../code/week10/02_linear_regression_pytorch.py) — forward/backward bằng autograd.
- Xem README: [`code/week10/README.md`](../code/week10/README.md).

## Câu hỏi thảo luận / Discussion questions

1. Vai trò của bias trong perceptron là gì? / What is the role of the bias term?
2. Vì sao cần hàm kích hoạt phi tuyến giữa các tầng? / Why do we need nonlinear activations between layers?
3. `loss.backward()` làm gì và gradient được lưu ở đâu? / What does `loss.backward()` do and where are gradients stored?
4. Vì sao phải `zero_()` gradient trước mỗi bước? / Why zero the gradients before each step?

## Bài tập / Exercises

- **Cơ bản:** Cài đặt perceptron một đầu vào với ReLU; tính `z` và `relu(z)` cho vài giá trị. / Implement a single-input perceptron with ReLU and evaluate it.
- **Nâng cao:** Huấn luyện hồi quy tuyến tính PyTorch cho $y=2x-1$ và báo cáo `w`, `b` hội tụ. / Train a PyTorch linear regression for $y=2x-1$ and report converged `w`, `b`.
- **Thử thách:** Thêm một tầng ẩn ReLU để xấp xỉ $y=x^2$ trên dữ liệu giả; so sánh loss với mô hình tuyến tính. / Add one hidden ReLU layer to approximate $y=x^2$; compare loss to the linear model.

## Yêu cầu nộp bài / Submission requirements

Nộp script capstone mini kèm kết quả hội tụ (đồ thị loss) và một đoạn mô tả forward/backward. Capstone đầy đủ theo [`projects/final_project.md`](../projects/final_project.md).

## Rubric 100 điểm / 100-point rubric

| Hạng mục | Xuất sắc | Đạt | Cần cải thiện | Chưa đạt | Điểm |
|---|---|---|---|---|---|
| Đúng chức năng | Forward/backward đúng, hội tụ | Đúng luồng chính | Thiếu một phần | Không chạy | 35 |
| Xử lý lỗi/an toàn | zero grad đúng, tránh rò grad/NaN | Có kiểm soát | Thiếu guardrail | Grad không zero gây sai | 25 |
| Chất lượng code/tài liệu | Chú thích rõ từng bước | Dễ đọc | Khó bảo trì | Không giải thích | 20 |
| Phân tích/giải thích | Giải thích phi tuyến, autograd, hội tụ | Có giải thích | Sơ sài | Không có | 20 |

## Lưu ý an toàn / Safety notes

Chạy trên CPU với dữ liệu giả nhỏ là đủ. Không huấn luyện trên dữ liệu thật/có bản quyền. Ghi seed để tái lập; kiểm tra giá trị loss hữu hạn trước khi kết luận hội tụ.

## Nguồn tham khảo / Source

- [Module 29 — Essence of deep learning](../../../docs/29_essence_deep_learning/index.md)
