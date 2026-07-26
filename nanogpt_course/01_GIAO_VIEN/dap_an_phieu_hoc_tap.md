# ĐÁP ÁN PHIẾU BÀI TẬP VÀ CÂU HỎI ÔN TẬP
> **Học phần:** Tự xây dựng nanoGPT cho học sinh THPT  
> **Mục tiêu:** Cung cấp đáp án chính thức và giải thích sư phạm cho giáo viên chấm điểm.

---

## 🔑 Lời giải các thử thách viết code Python

### 💻 Tuần 2: Thử thách tạo từ điển ngược `itos` (Trang học sinh)
*   **Đề bài:** Tạo từ điển `itos` (int to string) từ danh sách ký tự `chars`.
*   **Đáp án đúng của học sinh:**
    ```python
    itos = { i:ch for i, ch in enumerate(chars) }
    ```
*   **Giải thích sư phạm:** Học sinh sử dụng kỹ thuật Dictionary Comprehension trong Python. Biến `i` nhận chỉ số số nguyên (định danh), biến `ch` nhận ký tự tương ứng.
*   **Mã hóa chuỗi "cab cab"**: Dựa vào `stoi = {' ': 0, 'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}`, kết quả mã hóa là: `[3, 1, 2, 0, 3, 1, 2]`.

---

## 🔑 Giải đáp câu hỏi ôn tập các tuần học chính

### 📅 Tuần 4: Câu hỏi về Causal Masking (Mặt nạ nhân quả)
*   **Câu hỏi:** Tại sao ma trận điểm số chú ý phải che đi các giá trị tương lai bằng giá trị $-\infty$ thay vì số $0$?
*   **Câu trả lời đúng:** 
    *   Hàm Softmax sử dụng số mũ $e^x$ để tính toán phân phối xác suất.
    *   Nếu ta che bằng số $0$, khi tính $e^0 = 1$, các từ ở tương lai vẫn nhận được điểm số xác suất dương từ Softmax (vẫn được AI chú ý).
    *   Nếu ta che bằng giá trị âm vô cùng $-\infty$, vì $e^{-\infty} = 0$, xác suất chú ý ở các vị trí này sẽ bị triệt tiêu hoàn toàn về 0%, ngăn chặn tuyệt đối việc nhìn trộm tương lai.

### 📅 Tuần 5: Câu hỏi về chia căn $\sqrt{d_k}$ trong Self-Attention
*   **Câu hỏi:** Tại sao phải chia tích vô hướng $QK^T$ cho căn bậc hai kích thước vector $\sqrt{d_k}$ trước khi tính Softmax?
*   **Câu trả lời đúng:**
    *   Khi số chiều vector $d_k$ lớn, phép nhân vô hướng của các vector có phương sai bằng 1 sẽ tạo ra kết quả có phương sai rất lớn (bằng $d_k$).
    *   Phương sai lớn khiến các giá trị logits cực kỳ lệch nhau, đẩy hàm Softmax vào các vùng bão hòa (xác suất dồn hết vào 1 từ, các từ khác bằng 0).
    *   Ở vùng bão hòa này, đạo hàm của hàm Softmax tiệm cận về 0, gây ra lỗi **biến mất gradient** khiến mạng thần kinh ngừng học. Chia cho $\sqrt{d_k}$ giúp đưa phương sai về lại 1, đảm bảo gradient truyền đi tốt.

### 📅 Tuần 9: Câu hỏi về tham số Temperature (Nhiệt độ sáng tạo)
*   **Câu hỏi:** Muốn AI gõ code hoặc giải toán chính xác, ta nên chọn Temperature cao hay thấp?
*   **Câu trả lời đúng:**
    *   Nên đặt **Temperature thấp (khoảng 0.1 - 0.2)** hoặc sử dụng chế độ chọn Greedy.
    *   Nhiệt độ thấp giúp mô hình luôn chọn từ có xác suất cao nhất, đảm bảo tính logic, chính xác và không bị ảo giác tạo ra các từ ngẫu nhiên sai lệch thông tin kỹ thuật.
