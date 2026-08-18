---
layout: course
title: "Week03"
permalink: /1_Foundations/python-math-foundations-10weeks/lessons/week03.html
---

# Tuần 3 — Hàm / Week 3 — Functions

[← Tuần 2](week02.md) · [← Tổng quan](../INDEX.md) · [Tuần 4 →](week04.md)

## Mục tiêu học tập / Learning objectives

- Khai báo hàm bằng `def`, phân biệt tham số (parameter) và đối số (argument). / Declare functions with `def`; distinguish parameters and arguments.
- Dùng `return` để trả kết quả và hiểu phạm vi biến (scope). / Use `return` and understand scope.
- Đọc trợ giúp hàm bằng `help()` và docstring. / Read function help with `help()` and docstrings.
- Dùng NumPy để tạo số ngẫu nhiên có seed (tái lập được). / Use NumPy random with a seed for reproducibility.

## Công cụ và dữ liệu / Tools and data

- Python 3.10+, thư viện NumPy (`pip install numpy` hoặc `numpy>=1.25` trong `requirements.txt`). Dữ liệu giả do hàm sinh ra.

## Lý thuyết cô đọng + ví dụ / Concise theory + example

Hàm đóng gói một khối lệnh có tên, nhận đầu vào qua tham số và trả đầu ra qua `return`. Docstring (chuỗi ở đầu hàm) mô tả mục đích và được hiển thị khi gọi `help()`. Biến khai báo trong hàm là biến cục bộ (local), không thấy từ bên ngoài.

```python
def tinh_diem_trung_binh(diem):           # Tham số: diem (list).
    """Trả về điểm trung bình của một danh sách điểm."""  # Docstring.
    if not diem:                          # Bảo vệ danh sách rỗng.
        return 0.0
    return sum(diem) / len(diem)          # Trả kết quả trung bình.

print(tinh_diem_trung_binh([8, 9, 7]))   # Đối số là [8, 9, 7].
help(tinh_diem_trung_binh)                # In docstring.
```

NumPy random có `default_rng(seed)`: cùng seed cho cùng dãy số, giúp thí nghiệm tái lập được.

```python
import numpy as np
rng = np.random.default_rng(42)  # seed 42 -> dãy tái lập được.
print(rng.normal(size=5))        # 5 số ngẫu nhiên phân phối chuẩn.
```

## Lab từng bước / Step-by-step lab

1. Viết hàm `double(x)` trả về `x * 2`, gọi với vài giá trị.
2. Thêm docstring, gọi `help(double)`.
3. Viết hàm trả về giá trị lớn nhất của `list` không dùng `max()`.
4. Thử truy cập một biến cục bộ từ ngoài hàm để quan sát lỗi `NameError`.
5. Dùng NumPy `default_rng(42)` sinh 5 số; chạy lại để xác nhận kết quả giống nhau.
6. Đổi seed khác và quan sát dãy số thay đổi.

## Liên kết code mẫu / Sample code links

- [`code/week03/01_functions.py`](../code/week03/01_functions.py) — định nghĩa và gọi hàm.
- [`code/week03/02_numpy_random.py`](../code/week03/02_numpy_random.py) — số ngẫu nhiên có seed.
- Xem README: [`code/week03/README.md`](../code/week03/README.md).

## Câu hỏi thảo luận / Discussion questions

1. Vì sao nên tách logic thành hàm thay vì viết một khối dài? / Why split logic into functions instead of one long block?
2. Tham số và đối số khác nhau thế nào? / How do parameters differ from arguments?
3. `return` khác `print` ở điểm gì? / How does `return` differ from `print`?
4. Vì sao seed quan trọng với thí nghiệm khoa học? / Why does a seed matter for scientific experiments?

## Bài tập / Exercises

- **Cơ bản:** Viết hàm `chu_vi_hcn(dai, rong)` và `dien_tich_hcn(dai, rong)`; in kết quả cho vài bộ số. / Write rectangle perimeter and area functions and print results.
- **Nâng cao:** Viết hàm `tinh_diem_trung_binh` có xử lý danh sách rỗng và phần tử không phải số (bỏ qua hoặc báo lỗi rõ). / Write a mean function that handles an empty list and non-numeric items.
- **Thử thách:** Viết hàm `sinh_du_lieu(seed, n)` tạo dữ liệu giả bằng NumPy rồi tính trung bình/độ lệch chuẩn, chứng minh tính tái lập. / Write a fake-data generator with seed, compute mean/std, and prove reproducibility.

## Yêu cầu nộp bài / Submission requirements

Nộp script kèm kết quả chạy; mỗi hàm cần có docstring. Giải thích ngắn về một lỗi bạn đã gặp và cách sửa.

## Rubric 100 điểm / 100-point rubric

| Hạng mục | Xuất sắc | Đạt | Cần cải thiện | Chưa đạt | Điểm |
|---|---|---|---|---|---|
| Đúng chức năng | Hàm đúng, xử lý biên (rỗng, phần tử lạ) | Đúng luồng chính | Thiếu một phần | Không chạy | 35 |
| Xử lý lỗi/an toàn | Có docstring, bảo vệ đầu vào | Có kiểm soát chính | Thiếu guardrail | Hàm gây crash không rõ | 25 |
| Chất lượng code/tài liệu | Tên hàm/param rõ, chú thích đúng | Dễ đọc | Khó bảo trì | Không giải thích | 20 |
| Phân tích/giải thích | Giải thích return vs print, scope, seed | Có giải thích | Sơ sài | Không có | 20 |

## Lưu ý an toàn / Safety notes

Không đặt mật khẩu/token làm giá trị mặc định trong tham số. Số ngẫu nhiên chỉ dùng cho dữ liệu giả, không dùng cho bảo mật (dùng `secrets` cho mục đích bảo mật thực).

## Nguồn tham khảo / Source

- [Module 22 — Python functions](../../../docs/22_python_functions/index.md)
