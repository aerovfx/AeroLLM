# Tuần 6: Multi-Head Attention & Lớp MLP — Extension Material
> **Chủ đề mở rộng:** So sánh hàm kích hoạt ReLU và GELU trong các mô hình ngôn ngữ hiện đại.

---

### Hàm kích hoạt ReLU (Rectified Linear Unit):
$$f(x) = \max(0, x)$$
*   *Đặc điểm:* Trả về 0 cho tất cả đầu vào âm. 
*   *Vấn đề:* Có thể dẫn đến hiện tượng **chết nơ-ron** (dying ReLU), nơi các nơ-ron nhận giá trị âm sẽ có đạo hàm bằng 0 và ngừng cập nhật tham số vĩnh viễn.

### Hàm kích hoạt GELU (Gaussian Error Linear Unit):
$$f(x) = x \cdot \Phi(x) = x \cdot P(X \le x), 	ext{ với } X \sim \mathcal{N}(0, 1)$$
Một công thức xấp xỉ phổ biến:
$$f(x) pprox 0.5x\left(1 + 	anh\left(\sqrt{rac{2}{\pi}}\left(x + 0.044715x^3ight)ight)ight)$$
*   *Đặc điểm:* Cho phép một phần nhỏ thông tin âm đi qua (đường cong mượt mà ở vùng âm gần 0).
*   *Lợi ích:* Tránh được hiện tượng chết nơ-ron hoàn toàn, giúp mô hình học các hàm toán học phức tạp mượt mà hơn và hội tụ nhanh hơn. Đây là hàm kích hoạt mặc định của GPT-2, nanoGPT và đa số các LLM hiện đại.
