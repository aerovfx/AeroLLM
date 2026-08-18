---
layout: course
title: "Week06"
permalink: /1_Foundations/python-math-foundations-10weeks/lessons/week06.html
---

# Tuần 6 — Indexing & slicing / Week 6 — Indexing & slicing

[← Tuần 5](week05.md) · [← Tổng quan](../INDEX.md) · [Tuần 7 →](week07.md)

## Mục tiêu học tập / Learning objectives

- Truy cập phần tử bằng chỉ mục dương và âm (negative indexing). / Access elements with positive and negative indices.
- Cắt lát (slicing) danh sách và chuỗi với `start:stop:step`. / Slice lists and strings with `start:stop:step`.
- Giải thích chỉ mục `start` bao gồm, `stop` loại trừ (half-open). / Explain inclusive start and exclusive stop.
- Áp dụng slicing cho mảng NumPy nhiều chiều. / Apply slicing to multidimensional NumPy arrays.

## Công cụ và dữ liệu / Tools and data

- Python 3.10+, NumPy. Dữ liệu giả (danh sách, chuỗi, mảng 2D).

## Lý thuyết cô đọng + ví dụ / Concise theory + example

Chỉ mục đếm từ 0; chỉ mục âm đếm từ cuối: `seq[-1]` là phần tử cuối. Slicing `seq[start:stop:step]` lấy các phần tử từ `start` đến trước `stop`, bước `step`. Bỏ trống `start`/`stop` nghĩa là lấy từ đầu/đến cuối.

```python
data = [10, 20, 30, 40, 50]
print(data[0])        # 10 — phần tử đầu.
print(data[-1])       # 50 — phần tử cuối.
print(data[1:4])      # [20, 30, 40] — stop=4 loại trừ.
print(data[::2])      # [10, 30, 50] — bước 2.
print(data[::-1])     # [50, 40, 30, 20, 10] — đảo ngược.
```

Chuỗi cũng cắt được (chữ cái): `"python"[1:4]` → `"yth"`. Với mảng NumPy 2D, dùng dấu phẩy để cắt theo trục: `arr[hang, cot]`.

```python
import numpy as np
arr = np.arange(12).reshape(3, 4)   # Ma trận 3 hàng x 4 cột 0..11.
print(arr[0, :])                    # Hàng 0: [0 1 2 3].
print(arr[:, 1])                    # Cột 1: [1 5 9].
```

## Lab từng bước / Step-by-step lab

1. Tạo `data = [10, 20, 30, 40, 50]`, in phần tử đầu, cuối và phần tử thứ ba.
2. Cắt `data[1:4]`, `data[:3]`, `data[3:]`, `data[::-1]` và giải thích từng kết quả.
3. Cắt chuỗi `"học máy"` lấy 2 ký tự đầu và 2 ký tự cuối.
4. Tạo mảng NumPy 3×4, in hàng đầu, cột cuối và một khối 2×2.
5. Dùng slicing để đổi giá trị một khối của mảng (assignment).
6. Thử chỉ mục ngoài phạm vi để quan sát lỗi `IndexError`.

## Liên kết code mẫu / Sample code links

- [`code/week06/01_indexing_slicing.py`](../code/week06/01_indexing_slicing.py) — chỉ mục và slicing danh sách/chuỗi.
- [`code/week06/02_numpy_slicing.py`](../code/week06/02_numpy_slicing.py) — slicing mảng NumPy.
- Xem README: [`code/week06/README.md`](../code/week06/README.md).

## Câu hỏi thảo luận / Discussion questions

1. Vì sao slicing dùng khoảng half-open `[start, stop)`? / Why is slicing half-open `[start, stop)`?
2. `data[::-1]` hoạt động thế nào? / How does `data[::-1]` work?
3. Slicing NumPy trả về bản sao (copy) hay view? Vì sao điều này quan trọng? / Does NumPy slicing return a copy or a view, and why does it matter?
4. Khi nào chỉ mục âm giúp code rõ ràng hơn? / When do negative indices make code clearer?

## Bài tập / Exercises

- **Cơ bản:** Cho chuỗi, in 3 ký tự giữa, ký tự cuối và chuỗi đảo ngược. / Print the middle 3 chars, last char, and reversed string.
- **Nâng cao:** Cho danh sách 10 số, dùng slicing tạo danh sách chỉ chứa phần tử ở vị trí chẵn và danh sách đảo ngược. / Build even-indexed and reversed lists via slicing.
- **Thử thách:** Tạo ma trận 5×5, dùng slicing lấy viền ngoài (border), đường chéo chính và một khối con; giải thích view vs copy. / Extract the border, main diagonal, and a sub-block of a 5×5 matrix; explain view vs copy.

## Yêu cầu nộp bài / Submission requirements

Nộp script kèm kết quả; với mỗi phép slicing ghi một dòng giải thích `start:stop:step` đã dùng.

## Rubric 100 điểm / 100-point rubric

| Hạng mục | Xuất sắc | Đạt | Cần cải thiện | Chưa đạt | Điểm |
|---|---|---|---|---|---|
| Đúng chức năng | Mọi slicing đúng, kể cả step âm | Đúng luồng chính | Thiếu một phần | Không chạy | 35 |
| Xử lý lỗi/an toàn | Nhận diện IndexError, hiểu view/copy | Có kiểm soát | Thiếu guardrail | Gây lỗi ngoài phạm vi | 25 |
| Chất lượng code/tài liệu | Chú thích rõ từng slicing | Dễ đọc | Khó bảo trì | Không giải thích | 20 |
| Phân tích/giải thích | Giải thích half-open và view/copy | Có giải thích | Sơ sài | Không có | 20 |

## Lưu ý an toàn / Safety notes

Slicing chỉ thao tác trên dữ liệu giả trong bộ nhớ. Khi slice NumPy trả về view, việc sửa view đổi cả mảng gốc — luôn kiểm tra để tránh lỗi logic khó phát hiện.

## Nguồn tham khảo / Source

- [Module 03 — Python indexing & slicing](../../../docs/03_python_indexing_and_slicing/index.md)
