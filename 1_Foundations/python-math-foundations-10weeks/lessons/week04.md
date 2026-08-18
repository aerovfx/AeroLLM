---
layout: course
title: "Week04"
permalink: /1_Foundations/python-math-foundations-10weeks/lessons/week04.html
---

# Tuần 4 — Luồng điều khiển / Week 4 — Flow control

[← Tuần 3](week03.md) · [← Tổng quan](../INDEX.md) · [Tuần 5 →](week05.md)

## Mục tiêu học tập / Learning objectives

- Dùng vòng lặp `for` để duyệt danh sách và dãy số `range()`. / Iterate lists and `range()` with `for`.
- Dùng câu lệnh `if/elif/else` để rẽ nhánh theo điều kiện. / Branch with `if/elif/else`.
- Viết list comprehension để biến đổi danh sách ngắn gọn. / Write list comprehensions.
- Dùng `enumerate` và `zip` để duyệt có chỉ mục và ghép nhiều dãy. / Use `enumerate` and `zip`.

## Công cụ và dữ liệu / Tools and data

- Python 3.10+. Dữ liệu giả (danh sách điểm, tên). Không cần thư viện ngoài.

## Lý thuyết cô đọng + ví dụ / Concise theory + example

Vòng lặp `for` thực hiện khối lệnh cho từng phần tử của một iterable. `range(n)` sinh dãy `0..n-1`. Câu lệnh `if/elif/else` chỉ chạy nhánh đầu tiên có điều kiện đúng. Thụt lề (indentation) xác định khối lệnh — sai thụt lề gây lỗi `IndentationError`.

```python
for i in range(3):          # Lặp i = 0, 1, 2.
    if i == 0:
        print("bắt đầu")    # Nhánh if chạy khi i == 0.
    else:
        print(i)            # Nhánh else cho các giá trị còn lại.
```

List comprehension là cách viết vòng lặp gọn trên một dòng: `[bieu_thuc for x in day if dieu_kien]`.

```python
squares = [x * x for x in range(5)]   # [0, 1, 4, 9, 16].
```

`enumerate(day)` trả về cặp `(chỉ mục, phần tử)`; `zip(a, b)` ghép từng phần tử tương ứng của hai dãy.

## Lab từng bước / Step-by-step lab

1. In các số từ 1 đến 5 bằng `range(1, 6)`.
2. Viết vòng lặp gán nhãn "đạt"/"không đạt" cho một danh sách điểm (ngưỡng 5).
3. Viết lại bước 2 bằng list comprehension.
4. Dùng `enumerate` để in "vị trí: tên" cho một danh sách tên.
5. Dùng `zip` để ghép danh sách tên và danh sách điểm thành các cặp.
6. Chủ ý bỏ thụt lề sai một dòng và đọc lỗi `IndentationError`.

## Liên kết code mẫu / Sample code links

- [`code/week04/01_loops_and_conditions.py`](../code/week04/01_loops_and_conditions.py) — for/if-else.
- [`code/week04/02_comprehension_enumerate_zip.py`](../code/week04/02_comprehension_enumerate_zip.py) — comprehension/enumerate/zip.
- Xem README: [`code/week04/README.md`](../code/week04/README.md).

## Câu hỏi thảo luận / Discussion questions

1. Khi nào dùng `for` trên phần tử trực tiếp và khi nào dùng `range(len(...))`? / When to iterate directly versus using `range(len(...))`?
2. `elif` khác hai câu `if` liên tiếp ở điểm gì? / How does `elif` differ from two separate `if` statements?
3. Khi nào list comprehension làm code khó đọc hơn? / When does a comprehension hurt readability?
4. Vì sao thụt lề nhất quán quan trọng khi nhiều người cùng viết? / Why does consistent indentation matter for collaboration?

## Bài tập / Exercises

- **Cơ bản:** In bảng cửu chương của một số bằng vòng lặp. / Print a multiplication table using a loop.
- **Nâng cao:** Cho danh sách điểm, dùng comprehension tạo danh sách nhãn đạt/không đạt, rồi dùng `zip` in "tên — điểm — nhãn". / Build pass/fail labels with a comprehension and print with `zip`.
- **Thử thách:** Viết vòng lặp tìm tất cả số nguyên tố dưới 100 chỉ dùng `for`/`if`/`range`, không dùng thư viện. / Find all primes below 100 using only for/if/range.

## Yêu cầu nộp bài / Submission requirements

Nộp script kèm kết quả chạy; giải thích một đoạn bạn chọn vòng lặp thay vì comprehension (hoặc ngược lại).

## Rubric 100 điểm / 100-point rubric

| Hạng mục | Xuất sắc | Đạt | Cần cải thiện | Chưa đạt | Điểm |
|---|---|---|---|---|---|
| Đúng chức năng | Vòng lặp/nhánh đúng, xử lý danh sách rỗng | Đúng luồng chính | Thiếu một phần | Không chạy | 35 |
| Xử lý lỗi/an toàn | Thụt lề chuẩn, tránh vòng lặp vô hạn | Có kiểm soát | Dễ lỗi thụt lề | Vòng lặp vô hạn/treo | 25 |
| Chất lượng code/tài liệu | Chú thích rõ lý do chọn cấu trúc | Dễ đọc | Khó bảo trì | Không giải thích | 20 |
| Phân tích/giải thích | So sánh được for/while/comprehension | Có giải thích | Sơ sài | Không có | 20 |

## Lưu ý an toàn / Safety notes

Tránh vòng lặp vô hạn (đảm bảo điều kiện dừng luôn đạt tới). Không dùng `while True` mà thiếu lối thoát trong lab.

## Nguồn tham khảo / Source

- [Module 23 — Python flow control](../../../docs/23_python_flow_control/index.md)
