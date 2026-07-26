# Tuần 2: Tokenization — Extension Material
> **Chủ đề mở rộng:** Thuật toán Byte Pair Encoding (BPE) chi tiết.

---

Thuật toán BPE là một thuật toán nén dữ liệu cổ điển được Sennrich et al. (2015) áp dụng vào việc mã hóa từ vựng cho các mô hình dịch máy và LLM. Quy trình hoạt động của BPE gồm các bước:

1.  **Khởi tạo:**
    *   Tách tất cả từ trong tập ngữ liệu thành các ký tự đơn lẻ.
    *   Thêm ký tự kết thúc từ đặc biệt (ví dụ `</w>`) để phân biệt ranh giới từ.
2.  **Đếm tần suất:**
    *   Quét qua toàn bộ tập dữ liệu huấn luyện và đếm số lần xuất hiện của tất cả các cặp ký tự đi liền nhau (ví dụ: cặp `e` và `s`, `h` và `o`).
3.  **Hợp nhất (Merge):**
    *   Tìm cặp ký tự xuất hiện nhiều nhất và gộp chúng lại thành một token mới (ví dụ: gộp `e` và `s` thành `es`).
4.  **Lặp lại:**
    *   Lặp lại bước 2 và 3 cho đến khi kích thước bộ từ vựng đạt đến giới hạn cấu hình mong muốn (ví dụ: 50.257 đối với GPT-2, hoặc 100.000 đối với GPT-4).

BPE giúp tối ưu hóa dung lượng bộ nhớ ngữ cảnh và tốc độ xử lý của mô hình, đảm bảo tính cân bằng giữa kích thước bộ từ vựng và độ dài của dãy token đầu vào.
