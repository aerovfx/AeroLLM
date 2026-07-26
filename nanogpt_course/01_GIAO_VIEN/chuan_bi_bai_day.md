# CÔNG TÁC CHUẨN BỊ BÀI DẠY (GIÁO VIÊN)
> **Học phần:** Tự xây dựng nanoGPT cho học sinh THPT  
> **Mục tiêu:** Đảm bảo hệ thống máy tính phòng lab hoặc thiết bị cá nhân của học sinh hoạt động tốt trước buổi học viết code.

---

## 💻 Yêu cầu phần cứng & Thiết bị phòng Lab
Khóa học này được thiết kế tối ưu để có thể thực hành trên hai cấu hình phần cứng:

### Cấu hình 1: Chạy trên Google Colab (Khuyến khích)
*   **Thiết bị:** Máy tính xách tay hoặc PC có kết nối Internet (không yêu cầu GPU rời của máy).
*   **Tài khoản:** Học sinh cần chuẩn bị sẵn một tài khoản Google (Gmail) cá nhân để truy cập Google Colab.
*   **Lợi ích:** Dùng GPU T4 miễn phí trên đám mây của Google, thời gian huấn luyện mô hình mẫu chỉ mất 3-5 phút.

### Cấu hình 2: Chạy trực tiếp trên máy tính phòng Lab (Offline)
*   **Yêu cầu hệ điều hành:** Windows 10/11, macOS, hoặc Ubuntu.
*   **Cấu hình tối thiểu:** CPU Core i5 (hoặc tương đương), RAM 8GB.
*   **Thời gian huấn luyện:** Chạy trên CPU sẽ lâu hơn (mất khoảng 10-15 phút để hoàn thành 3000 bước huấn luyện trên Tiny Shakespeare).

---

## 🛠️ Hướng dẫn thiết lập môi trường phần mềm (Cấu hình Offline)

Nếu không dùng Google Colab, giáo viên cần cài đặt sẵn các phần mềm sau trên máy học sinh trước khi khóa học bắt đầu:

1.  **Cài đặt Python:** Tải và cài đặt Python phiên bản 3.9 hoặc mới hơn từ trang chủ [python.org](https://www.python.org/).
2.  **Cài đặt thư viện PyTorch:** 
    *   Mở Terminal (macOS/Linux) hoặc Command Prompt (Windows).
    *   Chạy lệnh cài đặt PyTorch:
        ```bash
        pip install torch
        ```
    *   *Lưu ý cho máy có GPU Nvidia:* Tải phiên bản PyTorch hỗ trợ CUDA từ trang chủ [pytorch.org](https://pytorch.org/) để tối ưu hóa thời gian chạy.
3.  **Tải sẵn tập dữ liệu mẫu (Tiny Shakespeare):**
    *   Lưu tệp dữ liệu thô thành tệp `input.txt` trong thư mục làm việc của học sinh.
    *   Đường dẫn tải nhanh tệp:
        ```bash
        curl -o input.txt https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt
        ```

---

## 💡 Hướng dẫn xử lý sự cố trong lớp (Troubleshooting)

| Sự cố thường gặp | Nguyên nhân | Giải pháp |
| :--- | :--- | :--- |
| Lỗi `ModuleNotFoundError: No module named 'torch'` | Máy tính chưa được cài đặt thư viện PyTorch. | Chạy lệnh `pip install torch` để cài đặt thư viện. |
| Google Colab báo lỗi: `Cannot connect to GPU backend` | Đã dùng quá hạn mức GPU miễn phí trong ngày của Colab. | Hướng dẫn học sinh chuyển Runtime sang CPU (Chạy chậm hơn nhưng không bị giới hạn) hoặc đăng nhập bằng tài khoản Gmail phụ. |
| AI sinh chữ bị lỗi phông tiếng Việt có dấu | File dữ liệu đầu vào `input.txt` không được lưu dưới định dạng **UTF-8**. | Hướng dẫn học sinh mở tệp `input.txt` bằng Notepad/VS Code và bấm **Save with Encoding -> UTF-8**. |
