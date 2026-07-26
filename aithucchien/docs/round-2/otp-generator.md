# Công cụ Tạo mã OTP

Công cụ này tạo Mật khẩu một lần dựa trên thời gian (TOTP) từ một secret key, tương thích với Google Authenticator, Microsoft Authenticator, và các ứng dụng 2FA tiêu chuẩn khác.

## Hướng dẫn sử dụng​

1. **Nhập Secret Key của bạn**: Dán secret key đã được mã hóa Base32 của bạn vào ô nhập liệu bên dưới.
2. **Nhận mã OTP**: Công cụ sẽ tự động tạo mã OTP 6 chữ số hiện tại.
3. **Tự động làm mới**: Mã sẽ tự động làm mới sau mỗi 30 giây, giống như ứng dụng xác thực của bạn.

Secret Key (Base32):💡 Thử với secret key mẫu: JBSWY3DPEHPK3PXP------Copy

## Lưu ý Bảo mật​

- **Chỉ xử lý phía Client**: Mọi tính toán đều được thực hiện trực tiếp trong trình duyệt của bạn. Secret key của bạn không bao giờ được gửi đến bất kỳ máy chủ nào.
- **Không chia sẻ Key**: Secret key là thông tin nhạy cảm. Không chia sẻ công khai. Công cụ này dành cho mục đích phát triển và kiểm thử.
