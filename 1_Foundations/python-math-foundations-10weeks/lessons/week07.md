---
layout: course
title: "Week07"
permalink: /1_Foundations/python-math-foundations-10weeks/lessons/week07.html
---

# Tuần 7 — PyTorch căn bản / Week 7 — PyTorch basics

[← Tuần 6](week06.md) · [← Tổng quan](../INDEX.md) · [Tuần 8 →](week08.md)

## Mục tiêu học tập / Learning objectives

- Khai báo lớp (class) và đối tượng, phân biệt thuộc tính và phương thức. / Declare classes and objects; distinguish attributes and methods.
- Tạo tensor PyTorch, đọc dtype, shape và số chiều (ndim). / Create tensors and read dtype, shape, and ndim.
- Đổi hình (reshape) và lấy phần tử tensor. / Reshape tensors and index into them.
- Sinh tensor ngẫu nhiên có seed để tái lập. / Generate random tensors with a seed.

## Công cụ và dữ liệu / Tools and data

- Python 3.10+, PyTorch (`pip install torch`, hoặc `torch>=2.0.1` trong `requirements.txt`). Dữ liệu giả là các tensor do bạn tạo.

## Lý thuyết cô đọng + ví dụ / Concise theory + example

Lớp (class) là khuôn mẫu định nghĩa thuộc tính và hành vi; đối tượng (object) là một thực thể cụ thể từ khuôn mẫu đó. Phương thức `__init__` khởi tạo đối tượng, `self` trỏ tới chính đối tượng.

```python
class Student:
    def __init__(self, name, score):   # Khởi tạo thuộc tính.
        self.name = name                # Thuộc tính name.
        self.score = score              # Thuộc tính score.

s = Student("An", 8.5)                  # Tạo một đối tượng.
print(s.name, s.score)                  # Truy cập thuộc tính.
```

Tensor là mảng nhiều chiều, là đơn vị dữ liệu cơ bản của PyTorch. `torch.tensor(...)` tạo tensor, `.shape` cho kích thước, `.dtype` cho kiểu số, `reshape` đổi hình, `default_rng`/`rand` sinh số ngẫu nhiên.

```python
import torch
t = torch.tensor([[1, 2, 3], [4, 5, 6]])  # Tensor 2x3.
print(t.shape, t.dtype)                    # torch.Size([2, 3]) torch.int64.
print(t.reshape(3, 2))                     # Đổi hình thành 3x2.

g = torch.Generator().manual_seed(42)      # Seed tái lập được.
r = torch.rand(3, generator=g)             # 3 số ngẫu nhiên [0, 1).
```

## Lab từng bước / Step-by-step lab

1. Viết lớp `Student` có thuộc tính `name` và `score`, tạo 2 đối tượng rồi in.
2. Tạo tensor `[[1,2,3],[4,5,6]]`, in `shape` và `dtype`.
3. `reshape(3, 2)` và `reshape(-1)` (trải phẳng); giải thích `-1`.
4. Tạo tensor `float` bằng `torch.tensor(..., dtype=torch.float32)`.
5. Dùng `torch.Generator().manual_seed(42)` để sinh 3 số, chạy lại xác nhận giống.
6. Truy cập phần tử `t[0, 1]` và hàng `t[1]` (liên hệ slicing tuần 6).

## Liên kết code mẫu / Sample code links

- [`code/week07/01_classes_objects.py`](../code/week07/01_classes_objects.py) — class và đối tượng.
- [`code/week07/02_tensor_basics.py`](../code/week07/02_tensor_basics.py) — tensor, shape, reshape, random.
- Xem README: [`code/week07/README.md`](../code/week07/README.md).

## Câu hỏi thảo luận / Discussion questions

1. Class khác dict ở điểm gì khi mô tả một đối tượng có hành vi? / How does a class differ from a dict for objects with behavior?
2. Vì sao tensor cần dtype cụ thể và đổi dtype có thể mất thông tin? / Why does dtype matter and how can casting lose information?
3. `reshape` khác `view` ở chỗ nào về bộ nhớ? / How do `reshape` and `view` differ regarding memory?
4. Vì sao mọi thí nghiệm học máy nên ghi lại seed? / Why record the seed in every ML experiment?

## Bài tập / Exercises

- **Cơ bản:** Tạo tensor 3×2 và in shape/dtype; đổi thành 2×3 rồi trải phẳng. / Create a 3×2 tensor, print shape/dtype, reshape to 2×3 then flatten.
- **Nâng cao:** Viết lớp `Dataset` giả chứa `features` (tensor) và `labels` (tensor), có phương thức trả số mẫu. / Write a fake `Dataset` class holding feature and label tensors with a length method.
- **Thử thách:** Sinh tensor 1000 số ngẫu nhiên có seed, tính trung bình/độ lệch chuẩn bằng PyTorch và so với giá trị kỳ vọng. / Generate 1000 seeded random values, compute mean/std with PyTorch, and compare to expectation.

## Yêu cầu nộp bài / Submission requirements

Nộp script kèm kết quả; ghi rõ phiên bản torch và seed đã dùng. Giải thích một lỗi shape bạn gặp khi reshape.

## Rubric 100 điểm / 100-point rubric

| Hạng mục | Xuất sắc | Đạt | Cần cải thiện | Chưa đạt | Điểm |
|---|---|---|---|---|---|
| Đúng chức năng | Tensor/shape/dtype đúng, seed tái lập | Đúng luồng chính | Thiếu một phần | Không chạy | 35 |
| Xử lý lỗi/an toàn | Nhận diện lỗi shape, đổi dtype có chủ ý | Có kiểm soát | Thiếu guardrail | Gây lỗi shape không rõ | 25 |
| Chất lượng code/tài liệu | Class rõ, chú thích đúng chỗ | Dễ đọc | Khó bảo trì | Không giải thích | 20 |
| Phân tích/giải thích | Giải thích reshape/view và seed | Có giải thích | Sơ sài | Không có | 20 |

## Lưu ý an toàn / Safety notes

Chạy tensor trên CPU là đủ cho tuần này; không cần GPU. Không đưa trọng số model thật hoặc dữ liệu có bản quyền vào bài. Lưu ý seed chỉ đảm bảo tái lập, không phải biện pháp bảo mật.

## Nguồn tham khảo / Source

- [Module 26 — Python & PyTorch](../../../docs/26_python_pytorch/index.md)
