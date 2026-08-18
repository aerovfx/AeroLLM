---
layout: course
title: "Week05"
permalink: /1_Foundations/python-math-foundations-10weeks/lessons/week05.html
---

# Tuần 5 — Chuỗi & văn bản + trực quan dữ liệu / Week 5 — Strings & text + data visualization

[← Tuần 4](week04.md) · [← Tổng quan](../INDEX.md) · [Tuần 6 →](week06.md)

## Mục tiêu học tập / Learning objectives

- Dùng f-string để nội suy giá trị vào chuỗi. / Use f-strings for string interpolation.
- Đọc và xử lý văn bản từ file local (đếm từ, tách dòng, chuẩn hoá). / Read and process local text files.
- Vẽ biểu đồ đường/chấm bằng Matplotlib với nhãn trục và tiêu đề. / Plot lines/dots with Matplotlib and labels.
- Tạo nhiều biểu đồ con (subplot) trong một hình. / Create multiple subplots in one figure.

## Công cụ và dữ liệu / Tools and data

- Python 3.10+, Matplotlib (`pip install matplotlib`). Dữ liệu giả hoặc file text local do bạn tự tạo (ví dụ `data.txt` vài dòng). Không tải văn bản từ web trong tuần này.

## Lý thuyết cô đọng + ví dụ / Concise theory + example

f-string đặt biểu thức trong `{}` để chèn vào chuỗi: `f"Tên: {name}"`. Xử lý văn bản gồm đọc file (`open`, `read`/`readlines`), tách từ (`split`), chuyển chữ thường (`lower`), bỏ khoảng trắng (`strip`). Vẽ biểu đồ dùng `matplotlib.pyplot`: `plot(x, y)` vẽ đường, `scatter` vẽ chấm, `title/xlabel/ylabel` đặt nhãn, `subplots` tạo lưới biểu đồ.

```python
name, diem = "An", 8.5
print(f"{name} đạt {diem} điểm")   # f-string nội suy name và diem.

text = "  Xin chào  "
print(text.strip().lower().split())  # ['xin', 'chào'] sau khi làm sạch.
```

```python
import matplotlib.pyplot as plt
x, y = [1, 2, 3], [2, 4, 6]
fig, ax = plt.subplots()        # Tạo hình và một trục.
ax.plot(x, y, marker="o")       # Vẽ đường với chấm đánh dấu.
ax.set_title("y = 2x")          # Tiêu đề biểu đồ.
plt.show()                      # Hiển thị (hoặc savefig để lưu file).
```

## Lab từng bước / Step-by-step lab

1. Dùng f-string in một câu chứa tên và điểm trung bình.
2. Tạo file `data.txt` gồm 4–5 dòng văn bản; đọc và đếm số từ.
3. Chuẩn hoá: chuyển thường, bỏ dấu câu đơn giản, đếm tần suất từ.
4. Vẽ biểu đồ `y = 2x` cho `x = 1..5` với tiêu đề và nhãn trục.
5. Tạo lưới 1×2 subplot: một biểu đồ đường, một biểu đồ chấm.
6. Lưu biểu đồ bằng `savefig("chart.png")` và mở xem.

## Liên kết code mẫu / Sample code links

- [`code/week05/01_strings_text.py`](../code/week05/01_strings_text.py) — f-string và xử lý text.
- [`code/week05/02_plotting.py`](../code/week05/02_plotting.py) — vẽ biểu đồ và subplot.
- Xem README: [`code/week05/README.md`](../code/week05/README.md).

## Câu hỏi thảo luận / Discussion questions

1. Khi nào nên dùng `savefig` thay vì `show`? / When to use `savefig` instead of `show`?
2. Vì sao nên đọc file bằng context manager (`with open(...)`) thay vì `open` thường? / Why use a `with open(...)` context manager?
3. Trực quan hoá giúp phát hiện điều gì mà bảng số không cho thấy? / What can visualization reveal that a table of numbers cannot?
4. Những loại dữ liệu nào không nên vẽ biểu đồ vì dễ gây hiểu lầm? / Which data can be misleading when plotted?

## Bài tập / Exercises

- **Cơ bản:** Dùng f-string in bảng thông tin 3 sinh viên; vẽ biểu đồ điểm của họ. / Print a 3-student table with f-strings and plot their scores.
- **Nâng cao:** Đọc file text, đếm tần suất 5 từ phổ biến nhất và vẽ biểu đồ cột (bar chart). / Read a text file, count the 5 most common words, and plot a bar chart.
- **Thử thách:** Vẽ 2 biểu đồ con: một đường của hàm bậc hai và một histogram của 1000 số ngẫu nhiên (NumPy). / Plot a quadratic line and a histogram of 1000 random numbers in subplots.

## Yêu cầu nộp bài / Submission requirements

Nộp script + file text nguồn (dữ liệu giả) + ảnh biểu đồ. Giải thích ngắn ý nghĩa biểu đồ. Không dùng văn bản có bản quyền.

## Rubric 100 điểm / 100-point rubric

| Hạng mục | Xuất sắc | Đạt | Cần cải thiện | Chưa đạt | Điểm |
|---|---|---|---|---|---|
| Đúng chức năng | Text và biểu đồ đúng, nhãn đầy đủ | Đúng luồng chính | Thiếu nhãn/trục | Không chạy | 35 |
| Xử lý lỗi/an toàn | `with open` an toàn, xử lý file thiếu | Có kiểm soát | Thiếu guardrail | Rò tài nguyên file | 25 |
| Chất lượng code/tài liệu | Chú thích rõ, biểu đồ dễ đọc | Dễ đọc | Khó bảo trì | Không giải thích | 20 |
| Phân tích/giải thích | Đọc được ý nghĩa biểu đồ | Có giải thích | Sơ sài | Không có | 20 |

## Lưu ý an toàn / Safety notes

Chỉ đọc file text local do bạn tạo; không đọc file hệ thống hoặc dữ liệu cá nhân của người khác. Đóng file đúng cách để tránh rò tài nguyên.

## Nguồn tham khảo / Source

- [Module 25 — Python strings & texts](../../../docs/25_python_strings_texts/index.md)
- [Module 24 — Python data visualization](../../../docs/24_python_data_visualization/index.md)
