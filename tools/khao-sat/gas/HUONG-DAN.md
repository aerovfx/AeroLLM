# Kết nối AeroLLM với Google Sheets

Backend là tùy chọn. Khi chưa cấu hình, khảo sát và điểm được lưu trong `localStorage` của trình duyệt.

## Triển khai

1. Truy cập [Google Apps Script](https://script.google.com/) bằng tài khoản sở hữu dữ liệu.
2. Tạo dự án mới và sao chép nội dung `Code.gs` vào trình soạn thảo.
3. Trong khối `CONFIG`, điền `OWNER_EMAIL`, `TEACHER_EMAIL` và kiểm tra ba URL AeroLLM.
4. Chạy hàm `taoToanBo()` một lần và cấp các quyền cần thiết. Script sẽ tạo thư mục, bảng tính và biểu mẫu trong Drive của bạn.
5. Chọn **Triển khai → Lần triển khai mới → Ứng dụng web**:
   - Thực thi với tư cách: **Tôi**.
   - Người có quyền truy cập: chọn phạm vi phù hợp với lớp học.
6. Sao chép URL kết thúc bằng `/exec`.
7. Mở `tools/khao-sat/ket-noi.html`, dán URL, bấm **Kiểm tra kết nối**, sau đó **Lưu**.

## Nguyên tắc riêng tư

- Dùng tài khoản Google thuộc tổ chức hoặc cá nhân chịu trách nhiệm quản lý lớp.
- Không đưa credential, token hay dữ liệu nhạy cảm vào repository.
- Chỉ thu thập dữ liệu cần thiết và thông báo rõ mục đích cho học viên.
- Thiết lập quyền chia sẻ bảng tính ở mức tối thiểu.
- Xuất bản sao lưu định kỳ và xóa dữ liệu khi hết thời hạn lưu giữ.

## Chia sẻ cấu hình

Trang Kết nối có thể tạo URL chứa tham số `?api=`. Chỉ gửi URL này cho người được phép sử dụng backend. Nếu cần thu hồi, hãy tạo deployment Apps Script mới và ngừng deployment cũ.
