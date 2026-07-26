# KẾ HOẠCH GIẢNG DẠY (GIÁO VIÊN)
> **Học phần:** Tự xây dựng nanoGPT cho học sinh THPT  
> **Thời lượng:** 10 tuần (mỗi tuần 1 buổi 90 - 120 phút)

---

## 📅 Lịch trình giảng dạy 10 tuần chi tiết

### 📅 Tuần 1: Giới thiệu AI & Mô hình ngôn ngữ lớn (LLM)
*   **Mục tiêu:** Giúp học sinh hiểu AI không phải là "phép thuật", nó hoạt động dựa trên quy luật đoán từ.
*   **Hoạt động lớp:** Chơi trò chơi đoán từ tiếp theo trong câu dở dang.
*   **Điểm nhấn giảng dạy:** Giải thích mô hình ngôn ngữ tự hồi quy (Autoregressive model).

### 📅 Tuần 2: Tokenization - Biến chữ viết thành số nguyên
*   **Mục tiêu:** Hiểu cách máy tính "đọc" ngôn ngữ qua các mã số.
*   **Hoạt động lớp:** Học sinh tự tạo từ điển ký tự `stoi` (string to int) và `itos` (int to string) bằng Python.
*   **Điểm nhấn giảng dạy:** So sánh mã hóa ký tự (char-level) đơn giản và mã hóa cụm từ (BPE) của OpenAI.

### 📅 Tuần 3: Embedding & Position - Bản đồ ý nghĩa từ vựng
*   **Mục tiêu:** Nắm được khái niệm không gian vector nhiều chiều và lý do cần Position Embedding.
*   **Hoạt động lớp:** Ẩn dụ "sơ đồ lớp học" để học sinh tìm ra các từ có tọa độ gần nhau.
*   **Điểm nhấn giảng dạy:** Cơ chế hoạt động của `nn.Embedding`.

### 📅 Tuần 4: Attention P1 - Cơ chế trung bình hóa và Mặt nạ nhân quả (Causal Mask)
*   **Mục tiêu:** Học cách gom thông tin từ quá khứ và che thông tin tương lai.
*   **Hoạt động lớp:** Thực hành viết phép nhân ma trận tam giác dưới (`tril`) trên bảng tính Excel hoặc Google Sheets.
*   **Điểm nhấn giảng dạy:** Tại sao mô hình không được "nhìn trộm" tương lai khi học.

### 📅 Tuần 5: Attention P2 - Thuật toán Query, Key, Value
*   **Mục tiêu:** Nắm vững công thức cốt lõi của Self-Attention.
*   **Hoạt động lớp:** Ẩn dụ "thẻ tra cứu thư viện" để giải thích mối quan hệ giữa Query, Key và Value.
*   **Điểm nhấn giảng dạy:** Vai trò của hàm Softmax trong việc quy đổi điểm tương đồng thành tỷ lệ xác suất (tổng bằng 1).

### 📅 Tuần 6: Multi-Head Attention & Lớp MLP (Feed-Forward)
*   **Mục tiêu:** Hiểu cách chạy song song nhiều góc nhìn (Heads) và lớp xử lý thông tin độc lập của từng từ.
*   **Hoạt động lớp:** Đọc code lớp `MultiHead` và `MLP` trong file mẫu.
*   **Điểm nhấn giảng dạy:** Tầm quan trọng của hàm phi tuyến tính như GELU/ReLU.

### 📅 Tuần 7: Ráp nối Transformer Block & Kiến trúc GPT
*   **Mục tiêu:** Kết nối các thành phần đã học thành bộ não hoàn chỉnh.
*   **Hoạt động lớp:** Vẽ sơ đồ luồng dữ liệu đi qua một Block và tính toán thử số lượng tham số (weights).
*   **Điểm nhấn giảng dạy:** Ẩn dụ "cáp truyền tin đường tắt" (Residual Connection) giúp ổn định tín hiệu.

### 📅 Tuần 8: Quy trình huấn luyện (Training Loop) & Vai trò của GPU
*   **Mục tiêu:** Hiểu cách mô hình tự sửa sai qua các bước lặp.
*   **Hoạt động lớp:** Thiết lập môi trường Google Colab kích hoạt GPU, chạy thử chương trình huấn luyện đầu tiên.
*   **Điểm nhấn giảng dạy:** Cơ chế tính Loss (sai số) và thuật toán chỉnh trọng số AdamW.

### 📅 Tuần 9: Suy luận & Sinh chữ (Inference) - Kiểm soát sự sáng tạo
*   **Mục tiêu:** Dùng mô hình đã học để tự gõ văn bản và điều chỉnh phong cách viết.
*   **Hoạt động lớp:** Thay đổi siêu tham số `Temperature` (0.2, 0.7, 1.5) để thấy AI biến đổi từ an toàn sang bay bổng/sáng tạo.
*   **Điểm nhấn giảng dạy:** Phương pháp lấy mẫu ngẫu nhiên có trọng số (`torch.multinomial`).

### 📅 Tuần 10: Showcase Dự Án & Đạo Đức Sử Dụng AI
*   **Mục tiêu:** Học sinh thuyết trình sản phẩm "AI làm thơ" của nhóm và nhận thức được các nguy cơ từ AI.
*   **Hoạt động lớp:** Trình diễn các sản phẩm tự chế và tranh biện về vấn đề bản quyền, ảo giác AI (hallucination).
*   **Điểm nhấn giảng dạy:** Định hướng nghề nghiệp tương lai trong ngành AI và Khoa học máy tính.

---

## 💡 Mẹo sư phạm: Phương pháp "Ẩn dụ hóa kỹ thuật"
Khi dạy học sinh THPT, giáo viên nên tránh đưa ra các định nghĩa toán học khô khan ngay từ đầu. Hãy áp dụng bộ ẩn dụ sau:
1.  **Gradient Descent:** Tập ném bóng rổ. Lệch phải thì chỉnh sang trái, ném mạnh thì giảm lực.
2.  **Residual Connection:** Đường cáp phụ chạy song song. Nếu cáp chính bị đứt hoặc nhiễu qua các tầng sâu, tín hiệu vẫn truyền qua cáp phụ an toàn.
3.  **Softmax:** Quy đổi điểm thi đua của các tổ thành tỉ lệ phần trăm bánh ngọt được chia.
