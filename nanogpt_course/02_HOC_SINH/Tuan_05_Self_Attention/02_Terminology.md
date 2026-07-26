# Tuần 5: Self-Attention — Terminology

| Thuật ngữ Tiếng Việt | Thuật ngữ Tiếng Anh | Phiên âm (IPA) | Định nghĩa & Ý nghĩa ngắn gọn |
| :--- | :--- | :--- | :--- |
| **Cơ chế tự chú ý** | Self-Attention | /sɛlf-əˈtɛn.ʃən/ | Cơ chế toán học cho phép các token trong chuỗi tương tác và gán mức độ quan trọng cho nhau dựa trên ngữ cảnh. |
| **Truy vấn** | Query (Q) | /ˈkwɪr.i/ | Vector đại diện cho thông tin mà token hiện tại đang tìm kiếm từ các token khác. |
| **Khóa** | Key (K) | /kiː/ | Vector đại diện cho nhãn dán thông tin mà một token cung cấp để so khớp với Query. |
| **Giá trị** | Value (V) | /ˈvæl.juː/ | Vector đại diện cho nội dung thông tin thực tế của token được gom lại sau khi tính trọng số chú ý. |
| **Tích vô hướng** | Dot Product | /dɑːt ˈprɑː.dʌkt/ | Phép nhân ma trận giữa Q và K để đo lường mức độ tương đồng (độ khớp) giữa các token. |
| **Chuẩn hóa Softmax** | Softmax Function | /ˈsɑːft.mæks ˈfʌŋk.ʃən/ | Hàm toán học biến đổi điểm số tương đồng thô (logits) thành phân phối xác suất có tổng bằng 1. |
| **Thang đo chia căn** | Scaled Dot-Product | /skeɪld dɑːt-ˈprɑː.dʌkt/ | Chia điểm số chú ý cho căn bậc hai của số chiều $\sqrt{d_k}$ để tránh làm tràn số khi tính Softmax. |
