# Tuần 9: Suy Luận & Lấy Mẫu — Terminology

| Thuật ngữ Tiếng Việt | Thuật ngữ Tiếng Anh | Phiên âm (IPA) | Định nghĩa & Ý nghĩa ngắn gọn |
| :--- | :--- | :--- | :--- |
| **Suy luận / Sinh chữ** | Inference | /ˈɪn.fɚ.əns/ | Quá trình chạy mô hình đã được huấn luyện xong để tạo ra dữ liệu mới (không cập nhật tham số). |
| **Thang nhiệt độ** | Temperature | /ˈtɛm.prə.tʃɚ/ | Siêu tham số dùng để chia tỷ lệ logits trước khi tính Softmax, kiểm soát mức độ ngẫu nhiên của câu trả lời. |
| **Lấy mẫu xác suất** | Multinomial Sampling | /ˌmʌl.tiˈnoʊ.mi.əl ˈsæm.plɪŋ/ | Phương pháp bốc thăm ngẫu nhiên một token dựa trên phân phối xác suất đã được chuẩn hóa bởi Softmax. |
| **Thuật toán Top-K** | Top-K Sampling | /tɑːp-keɪ ˈsæm.plɪŋ/ | Kỹ thuật lọc bỏ các từ có xác suất thấp, chỉ giữ lại top $K$ từ có điểm số cao nhất để bốc thăm. |
