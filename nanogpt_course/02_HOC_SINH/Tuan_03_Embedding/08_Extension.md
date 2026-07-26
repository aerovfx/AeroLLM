# Tuần 3: Embedding & Position — Extension Material
> **Chủ đề mở rộng:** So sánh nhúng vị trí học được (Learned Position Embedding) và nhúng vị trí dạng sóng (Sinusoidal Position Embedding).

---

Trong các mô hình Transformer, có hai cách chính để định nghĩa Position Embedding:

1.  **Sinusoidal Position Embedding (Attention is All You Need - 2017):**
    *   Sử dụng các hàm sóng lượng giác sin và cos ở các tần số khác nhau để tính toán tọa độ cố định cho vị trí.
    *   *Ưu điểm:* Không cần học tham số, có thể suy luận tốt trên các chuỗi dài hơn độ dài tối đa trong tập train.
2.  **Learned Position Embedding (GPT-2, nanoGPT):**
    *   Khởi tạo bảng nhúng vị trí như một tham số huấn luyện bình thường (`nn.Embedding(block_size, n_embd)`). Mô hình sẽ tự học tọa độ tối ưu cho mỗi vị trí.
    *   *Ưu điểm:* Dễ cài đặt, hiệu năng thực nghiệm tốt trên độ dài context cố định.
