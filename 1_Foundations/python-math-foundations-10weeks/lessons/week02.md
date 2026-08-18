---
layout: course
title: "Week02"
permalink: /1_Foundations/python-math-foundations-10weeks/lessons/week02.html
---

# Tuần 2 — Kiểu dữ liệu Python / Week 2 — Python data types

[← Tuần 1](week01.md) · [← Tổng quan](../INDEX.md) · [Tuần 3 →](week03.md)

## Mục tiêu học tập / Learning objectives

- Phân biệt các kiểu dữ liệu cơ bản: `int`, `float`, `str`, `bool` và dùng `type()` để kiểm tra. / Distinguish int, float, str, bool and inspect them with `type()`.
- Thực hiện phép toán số học và so sánh; hiểu thứ tự ưu tiên. / Perform arithmetic and comparisons; understand precedence.
- Khai báo biến và giải thích quy tắc đặt tên. / Declare variables and explain naming rules.
- Dùng `list` và `dict` để chứa dữ liệu có cấu trúc; truy cập phần tử bằng chỉ mục và khóa. / Use list and dict to hold structured data.

## Công cụ và dữ liệu / Tools and data

- Python 3.10+ hoặc Colab. Dữ liệu giả do bạn tự khai báo (điểm số, tên, trạng thái). Không cần thư viện ngoài.

## Lý thuyết cô đọng + ví dụ / Concise theory + example

Biến là tên gán cho một giá trị trong bộ nhớ. Python gõ động (dynamic typing): cùng một biến có thể nhận giá trị kiểu khác nhau, nhưng mỗi giá trị vẫn có một kiểu cụ thể. `int` là số nguyên, `float` là số thực, `str` là chuỗi ký tự, `bool` là `True`/`False`. `list` là dãy có thứ tự, `dict` là ánh xạ khóa→giá trị.

```python
age = 21                 # int: số nguyên.
height = 1.75            # float: số thực.
name = "An"              # str: chuỗi ký tự.
is_student = True        # bool: đúng/sai.
scores = [8, 9, 7]       # list: dãy có thứ tự.
info = {"name": "An", "age": 21}  # dict: khóa -> giá trị.

print(type(age), type(height), type(name), type(is_student))
print(scores[0], info["name"])  # Truy cập phần tử list và dict.
```

Lưu ý: phép chia `/` luôn trả về `float`; phép chia lấy nguyên `//` và lấy dư `%` trả về `int` khi cả hai toán hạng là `int`.

## Lab từng bước / Step-by-step lab

1. Khai báo một biến mỗi kiểu cơ bản, in `type()` của từng biến.
2. Tính `(17 // 5)` và `(17 % 5)`, giải thích kết quả.
3. Tạo `list` gồm 4 điểm số, in phần tử đầu và phần tử cuối.
4. Tạo `dict` mô tả một sinh viên (tên, tuổi, điểm), in giá trị theo khóa.
5. Thử gán biến `x = 5` rồi `x = "năm"`, in `type(x)` để thấy gõ động.
6. Chủ ý gây một lỗi `TypeError` (ví dụ `"a" + 1`) rồi đọc thông báo lỗi.

## Liên kết code mẫu / Sample code links

- [`code/week02/01_data_types.py`](../code/week02/01_data_types.py) — các kiểu dữ liệu và `type()`.
- [`code/week02/02_containers.py`](../code/week02/02_containers.py) — list/dict và truy cập phần tử.
- Xem README: [`code/week02/README.md`](../code/week02/README.md).

## Câu hỏi thảo luận / Discussion questions

1. Khi nào dùng `list` và khi nào dùng `dict`? / When do you choose a list versus a dict?
2. Vì sao `1/2` ra `0.5` nhưng `1//2` ra `0`? / Why does `1/2` give `0.5` while `1//2` gives `0`?
3. Gõ động mang lại lợi ích gì và rủi ro gì? / What are the benefits and risks of dynamic typing?
4. Vì sao nên đặt tên biến có nghĩa thay vì `a`, `b`, `x1`? / Why prefer meaningful names over `a`, `b`, `x1`?

## Bài tập / Exercises

- **Cơ bản:** Khai báo biến cho tên, tuổi, chiều cao, điểm trung bình; in từng giá trị kèm `type()`. / Declare variables for name, age, height, average score and print each with its type.
- **Nâng cao:** Xây `dict` "lớp học" chứa danh sách sinh viên, mỗi sinh viên là một `dict`; in tên và điểm của từng người. / Build a "class" dict of student dicts and print each name and score.
- **Thử thách:** Viết đoạn code đếm số lần mỗi giá trị xuất hiện trong một `list` (dùng `dict`), không dùng thư viện. / Count occurrences of each value in a list using a dict, no libraries.

## Yêu cầu nộp bài / Submission requirements

Nộp script (hoặc notebook) kèm kết quả chạy và một đoạn giải thích 5–10 dòng về lựa chọn kiểu dữ liệu. Không gắn dữ liệu thật của người khác.

## Rubric 100 điểm / 100-point rubric

| Hạng mục | Xuất sắc | Đạt | Cần cải thiện | Chưa đạt | Điểm |
|---|---|---|---|---|---|
| Đúng chức năng | Mọi kiểu dữ liệu dùng đúng, edge case được xử lý | Đúng luồng chính | Thiếu một phần | Không chạy | 35 |
| Xử lý lỗi/an toàn | Nhận diện và giải thích TypeError, chia cho 0 | Có kiểm soát chính | Thiếu guardrail | Gây lỗi không kiểm soát | 25 |
| Chất lượng code/tài liệu | Tên biến rõ, chú thích đúng chỗ | Dễ đọc | Khó bảo trì | Không giải thích | 20 |
| Phân tích/giải thích | Lý giải đúng chọn kiểu dữ liệu | Có giải thích | Sơ sài | Không có | 20 |

## Lưu ý an toàn / Safety notes

Dữ liệu dùng trong bài là dữ liệu giả do bạn tạo. Không dùng thông tin cá nhân thật (tên, điểm, số định danh) của người khác trong bài nộp.

## Nguồn tham khảo / Source

- [Module 21 — Python data types](../../../docs/21_python_data_types/index.md)
