# Tuần 7: Transformer Block & Architecture — Terminology

| Thuật ngữ Tiếng Việt | Thuật ngữ Tiếng Anh | Phiên âm (IPA) | Định nghĩa & Ý nghĩa ngắn gọn |
| :--- | :--- | :--- | :--- |
| **Kết nối dòng dư** | Residual Connection | /rɪˈzɪd.ju.əl kəˈnɛk.ʃən/ | Phép toán cộng trực tiếp đầu vào ban đầu vào đầu ra của một lớp ($x + f(x)$) để bảo toàn luồng tín hiệu. |
| **Chuẩn hóa lớp** | Layer Normalization | /ˈleɪ.ɚ ˌnɔːr.mə.laɪˈzeɪ.ʃən/ | Kỹ thuật điều chỉnh các giá trị số học của một lớp về trạng thái có trung bình bằng 0 và phương sai bằng 1. |
| **Độ dốc biến mất** | Vanishing Gradient | /ˈvæn.ɪ.ʃɪŋ ˈɡreɪ.di.ənt/ | Hiện tượng đạo hàm bị suy giảm về 0 khi truyền qua quá nhiều lớp sâu, khiến mô hình ngừng học. |
| **Chia sẻ trọng số** | Weight Tying | /weɪt taɪ.ɪŋ/ | Mẹo kỹ thuật dùng chung ma trận trọng số giữa lớp nhúng từ đầu vào (Embedding) và lớp chiếu đầu ra (Unembedding). |
