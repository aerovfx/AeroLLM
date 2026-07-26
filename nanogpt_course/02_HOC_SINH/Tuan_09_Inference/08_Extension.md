# Tuần 9: Suy Luận & Lấy Mẫu — Extension Material
> **Chủ đề mở rộng:** Toán học đằng sau Temperature Scaling và Top-P (Nucleus) Sampling.

---

### Cơ chế hoạt động của Temperature ($T$):
Trong quá trình suy luận, logits đầu ra $z_i$ được chia cho tham số nhiệt độ $T$ trước khi đưa vào hàm Softmax:
$$P(x_i) = rac{e^{z_i / T}}{\sum_{j} e^{z_j / T}}$$

*   **Khi $T 	o 0$ (Nhiệt độ tiệm cận 0):** Sự chênh lệch giữa logits lớn nhất và các logits khác tiến tới vô cùng. Phân phối xác suất biến thành một phân phối Dirac (Greedy selection), xác suất chọn từ tốt nhất gần như bằng 1.
*   **Khi $T 	o \infty$ (Nhiệt độ cực đại):** Tất cả các giá trị $z_i / T 	o 0$. Khi đó $e^0 = 1$, phân phối xác suất trở thành phân phối đều (Uniform distribution), mọi từ trong bộ từ vựng đều có xác suất chọn ngang nhau (gây nhiễu loạn hoàn toàn).

### Phương pháp lấy mẫu Top-P (Nucleus Sampling):
Thay vì lấy cố định $K$ từ có điểm số cao nhất như Top-K, **Top-P** lựa chọn tập hợp các từ nhỏ nhất có tổng xác suất tích lũy vượt quá ngưỡng $P$ (ví dụ $P = 0.9$ hay 90%):
$$\sum_{i \in V^{(p)}} P(x_i) \ge P$$
*   *Lợi ích:* Kích thước tập lựa chọn thay đổi linh hoạt theo từng bước dự đoán. Nếu mô hình rất tự tin (xác suất tập trung vào 1-2 từ), tập chọn sẽ rất nhỏ. Nếu mô hình phân vân (nhiều từ có xác suất ngang nhau), tập chọn tự động mở rộng để tăng độ sáng tạo.
