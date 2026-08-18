---
layout: course
title: "Week09"
permalink: /1_Foundations/python-math-foundations-10weeks/lessons/week09.html
---

# Tuần 9 — Gradient descent / Week 9 — Gradient descent

[← Tuần 8](week08.md) · [← Tổng quan](../INDEX.md) · [Tuần 10 →](week10.md)

## Mục tiêu học tập / Learning objectives

- Phát biểu ý tưởng gradient descent: cập nhật tham số ngược hướng đạo hàm. / State the gradient descent update rule.
- Cài đặt GD một chiều (1D) và quan sát hội tụ. / Implement 1D gradient descent and observe convergence.
- Cài đặt GD hai chiều (2D) trên hàm hai biến. / Implement 2D gradient descent on a two-variable function.
- So sánh learning rate cố định và động; nhận diện learning rate quá lớn/nhỏ. / Compare fixed vs. dynamic learning rates; identify too-large/too-small rates.
- Thảo luận local minima và vì sao chúng ít gây hại trong chiều cao. / Discuss local minima and why they matter less in high dimensions.

## Công cụ và dữ liệu / Tools and data

- Python 3.10+, NumPy, Matplotlib (để vẽ đường hội tụ). Dữ liệu giả là các hàm toán do bạn định nghĩa.

## Lý thuyết cô đọng + ví dụ / Concise theory + example

Gradient descent tìm cực tiểu của hàm $f$ bằng cách lặp: $x \leftarrow x - \eta\, f'(x)$. Đạo hàm $f'(x)$ chỉ hướng dốc lên, nên ta đi ngược lại. Learning rate $\eta$ quyết định độ dài bước.

Với $f(x)=(x-0.5)^2$, đạo hàm $f'(x)=2(x-0.5)$, cực tiểu tại $x=0.5$.

```python
def f(x):  return (x - 0.5) ** 2          # Hàm cần cực tiểu hoá.
def df(x): return 2 * (x - 0.5)           # Đạo hàm giải tích.

x = 2.0                                   # Điểm khởi tạo xa cực tiểu.
eta = 0.1                                 # Learning rate.
for i in range(30):                       # Lặp 30 epoch.
    x = x - eta * df(x)                   # Bước cập nhật GD.
print(round(x, 5))                        # Tiến về 0.5.
```

Learning rate quá lớn làm tham số nhảy quá đà (phân kỳ); quá nhỏ làm hội tụ chậm. Dynamic learning rate giảm dần theo epoch giúp bước lớn lúc đầu, nhỏ khi gần đích.

## Lab từng bước / Step-by-step lab

1. Cài đặt $f$ và $df$ như trên, chạy GD với `eta=0.1`, in `x` mỗi 5 epoch.
2. Thử `eta=1.0` và quan sát dao động không hội tụ; thử `eta=1.5` và quan sát phân kỳ (giá trị bùng nổ).
3. Thử `eta=0.001` và quan sát hội tụ chậm.
4. Lưu lịch sử `x` vào list, vẽ đồ thị hội tụ bằng Matplotlib.
5. Cài đặt GD 2D cho $f(x,y)=x^2+y^2$, cập nhật cả $x$ và $y$.
6. Thêm dynamic learning rate (giảm dần theo epoch, ví dụ $\eta_t = \eta_0/(1+t/10)$) và so sánh tốc độ hội tụ.

## Liên kết code mẫu / Sample code links

- [`code/week09/01_gradient_descent_1d.py`](../code/week09/01_gradient_descent_1d.py) — GD 1D và so sánh LR.
- [`code/week09/02_gradient_descent_2d.py`](../code/week09/02_gradient_descent_2d.py) — GD 2D và dynamic LR.
- Xem README: [`code/week09/README.md`](../code/week09/README.md).

## Câu hỏi thảo luận / Discussion questions

1. Dấu trừ trong công thức cập nhật có ý nghĩa gì? / What does the minus sign mean in the update rule?
2. Vì sao learning rate quá lớn gây phân kỳ? / Why does a too-large learning rate diverge?
3. Local minima khác global minimum thế nào? / How do local minima differ from the global minimum?
4. Vì sao dynamic learning rate thường giúp hội tụ tốt hơn? / Why does a dynamic learning rate usually help?

## Bài tập / Exercises

- **Cơ bản:** Chạy GD 1D cho $f(x)=(x-3)^2$ và in số epoch cần để `x` gần 3. / Run 1D GD for $f(x)=(x-3)^2$ and print epochs to reach near 3.
- **Nâng cao:** Vẽ đồ thị giá trị hàm theo epoch cho 3 learning rate khác nhau trên cùng một hình. / Plot the loss curve for three learning rates on one figure.
- **Thử thách:** Cài đặt GD 2D cho hàm có local minimum (ví dụ $f(x,y)=\sin x + y^2$) và khảo sát ảnh hưởng của điểm khởi tạo. / Implement 2D GD for a function with a local minimum and study initialization.

## Yêu cầu nộp bài / Submission requirements

Nộp script kèm đồ thị hội tụ; ghi rõ learning rate, số epoch và nhận xét về tốc độ hội tụ/phân kỳ.

## Rubric 100 điểm / 100-point rubric

| Hạng mục | Xuất sắc | Đạt | Cần cải thiện | Chưa đạt | Điểm |
|---|---|---|---|---|---|
| Đúng chức năng | GD 1D/2D đúng, đồ thị hội tụ rõ | Đúng luồng chính | Thiếu một phần | Không chạy | 35 |
| Xử lý lỗi/an toàn | Phát hiện phân kỳ, giới hạn epoch | Có kiểm soát | Thiếu guardrail | Phân kỳ không kiểm soát | 25 |
| Chất lượng code/tài liệu | Chú thích rõ đạo hàm và bước cập nhật | Dễ đọc | Khó bảo trì | Không giải thích | 20 |
| Phân tích/giải thích | So sánh LR cố định/động, nhận diện local minima | Có giải thích | Sơ sài | Không có | 20 |

## Lưu ý an toàn / Safety notes

Thí nghiệm chỉ trên hàm toán giả. Đặt giới hạn số epoch và phát hiện giá trị không hữu hạn (`NaN`/`inf`) để dừng sớm, tránh vòng lặp chạy vô hạn khi phân kỳ.

## Nguồn tham khảo / Source

- [Module 28 — Gradient descent](../../../docs/28_gradient_descent/index.md)
