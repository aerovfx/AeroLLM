---
layout: course
title: "Week01"
permalink: /1_Foundations/python-math-foundations-10weeks/lessons/week01.html
---

# Tuần 1 — Google Colab & môi trường Python / Week 1 — Google Colab & the Python environment

[← Tổng quan](../INDEX.md) · [Lịch học](../schedule.md) · [Tuần 2 →](week02.md)

## Mục tiêu học tập / Learning objectives

- Mở, chạy và lưu một notebook trên Google Colab; phân biệt ô code (code cell) và ô văn bản (text/Markdown cell). / Open, run, and save a Colab notebook; distinguish code cells from text/Markdown cells.
- Mô tả runtime (bộ nhớ, GPU/TPU) và chọn đúng runtime cho bài tập. / Describe the runtime and pick the right one.
- Chạy được script Python độc lập (`*.py`) ngoài Colab. / Run a standalone Python script.
- Kiểm tra phiên bản Python và cài đặt thư viện một cách an toàn. / Check the Python version and install libraries safely.

## Công cụ và dữ liệu / Tools and data

- Google Colab (tài khoản Google miễn phí) hoặc Python 3.10+ cài local.
- Trình duyệt và soạn thảo văn bản (VS Code, Notepad++…).
- Không dùng dữ liệu bên ngoài trong tuần này; chỉ cần các ô text/code tự viết.

## Lý thuyết cô đọng + ví dụ / Concise theory + example

Notebook là một tài liệu xen kẽ ô văn bản và ô code; Colab chạy từng ô trên một máy ảo tạm thời gọi là **runtime**. Ô code in kết quả ra ngay dưới ô. Một script `.py` thì chạy toàn bộ file từ trên xuống dưới bằng lệnh `python ten_file.py`.

Ví dụ ô code đầu tiên:

```python
# Ô code: in một dòng chào và phiên bản Python.
import sys  # Module chuẩn cung cấp thông tin phiên bản Python.
print("Xin chào từ Colab!")  # In chuỗi chào ra màn hình.
print(sys.version)           # In chuỗi mô tả phiên bản Python đang chạy.
```

Ví dụ ô Markdown: `# Tiêu đề`, `**in đậm**`, `- mục danh sách`, `` `code` ``. Ô văn bản không thực thi, dùng để ghi chú và trình bày.

## Lab từng bước / Step-by-step lab

1. Tạo notebook mới: `File → New notebook`.
2. Thêm một ô văn bản mô tả mục tiêu của bạn (ô `+ Text`).
3. Thêm ô code: `print("hello")` rồi bấm nút chạy (play). Kiểm tra kết quả xuất hiện ngay dưới ô.
4. Thêm ô code `import sys; print(sys.version)`, ghi lại phiên bản Python.
5. Chọn runtime: `Runtime → Change runtime type`; xem tuỳ chọn CPU/GPU/TPU (tuần này để CPU là đủ).
6. Tải notebook về: `File → Download → .ipynb`, mở thử trong trình soạn thảo.
7. Nếu dùng local: lưu đoạn code ở trên thành `hello.py` rồi chạy `python hello.py`.

## Liên kết code mẫu / Sample code links

- [`code/week01/01_hello_python.py`](../code/week01/01_hello_python.py) — script chào và in phiên bản.
- [`code/week01/02_environment_check.py`](../code/week01/02_environment_check.py) — kiểm tra môi trường Python.
- Xem README và lệnh chạy: [`code/week01/README.md`](../code/week01/README.md).

## Câu hỏi thảo luận / Discussion questions

1. Khác biệt giữa ô code và ô Markdown là gì? Khi nào nên dùng loại nào? / What is the difference between a code cell and a Markdown cell, and when should you use each?
2. Vì sao runtime Colab "biến mất" sau một thời gian không dùng? Dữ liệu lưu ở đâu mới bền? / Why does a Colab runtime reset, and where is data persistent?
3. Khi nào bạn cần bật GPU thay vì CPU? / When do you need a GPU runtime?
4. Script `.py` khác notebook ở điểm nào về cách chạy và chia sẻ? / How does a `.py` script differ from a notebook in execution and sharing?

## Bài tập / Exercises

- **Cơ bản:** Tạo notebook có ít nhất 1 ô text và 2 ô code, chụp ảnh kết quả chạy. / Make a notebook with one text cell and two code cells; screenshot the result.
- **Nâng cao:** Viết script `hello.py` in tên bạn và phiên bản Python; chạy cả trên Colab (`%run hello.py`) lẫn local. / Write `hello.py` that prints your name and the Python version; run it both in Colab and locally.
- **Thử thách:** Giải thích ý nghĩa từng dòng trong `02_environment_check.py`, và viết thêm một ô kiểm tra số CPU/GPU khả dụng. / Explain each line of `02_environment_check.py` and add a cell that reports available CPU/GPU.

## Yêu cầu nộp bài / Submission requirements

Nộp link notebook (hoặc file `.ipynb` + `.py`), ảnh chụp kết quả chạy, và một đoạn 5–10 dòng mô tả runtime đã chọn và lý do. Không gắn dữ liệu cá nhân hay token vào bài.

## Rubric 100 điểm / 100-point rubric

| Hạng mục | Xuất sắc | Đạt | Cần cải thiện | Chưa đạt | Điểm |
|---|---|---|---|---|---|
| Đúng chức năng | Chạy đúng cả notebook lẫn script, đủ ô theo yêu cầu | Chạy được luồng chính | Thiếu một phần yêu cầu | Không chạy được | 35 |
| Xử lý lỗi/an toàn | Ghi rõ phiên bản, môi trường; không secret | Môi trường được nêu | Thiếu mô tả môi trường | Đưa secret/token vào bài | 25 |
| Chất lượng code/tài liệu | Ô văn bản rõ, code có chú thích ngắn gọn | Dễ đọc | Khó theo dõi | Không giải thích | 20 |
| Phân tích/giải thích | Lý giải đúng lựa chọn runtime và từng dòng | Có giải thích | Giải thích sơ sài | Không giải thích | 20 |

## Lưu ý an toàn / Safety notes

Chỉ dùng tài khoản Colab của chính bạn và chạy local trên máy bạn kiểm soát. Không đưa mật khẩu, API key hay token vào notebook; không tải dữ liệu nhạy cảm lên máy chưa được phép.

## Nguồn tham khảo / Source

- [Module 20 — Google Colab notebooks](../../../docs/20_python_colab_notebooks/index.md)
