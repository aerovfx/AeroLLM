# Tuần 4: Causal Masking — Terminology

| Thuật ngữ Tiếng Việt | Thuật ngữ Tiếng Anh | Phiên âm (IPA) | Định nghĩa & Ý nghĩa ngắn gọn |
| :--- | :--- | :--- | :--- |
| **Mặt nạ nhân quả** | Causal Masking | /ˈkɑː.zəl ˈmæsk.ɪŋ/ | Cơ chế che đi thông tin từ tương lai để đảm bảo mô hình chỉ dự đoán dựa trên quá khứ. |
| **Ma trận tam giác dưới** | Lower Triangular Matrix | /ˈloʊ.ɚ traɪˈæŋ.ɡjə.lɚ ˈmeɪ.trɪks/ | Ma trận có tất cả các phần tử nằm phía trên đường chéo chính bằng 0. |
| **Phép lấp mặt nạ** | masked_fill | /mæskt fɪl/ | Phép toán thay thế các phần tử được chỉ định bởi mặt nạ bằng một giá trị cố định (như $-\infty$). |
| **Âm vô cùng** | Negative Infinity | /ˈnɛɡ.ə.t̬ɪv ɪnˈfɪn.ə.t̬i/ | Giá trị cực nhỏ ($-\infty$) dùng để biến đổi xác suất thành 0 sau khi qua hàm Softmax. |
