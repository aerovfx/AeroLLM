# Tuần 7: Transformer Block & Architecture — Extension Material
> **Chủ đề mở rộng:** Toán học đằng sau Layer Normalization.

---

Layer Normalization chuẩn hóa các giá trị đầu vào cho mỗi mẫu dữ liệu một cách độc lập. Với một vector đầu vào $x = (x_1, x_2, \dots, x_d)$, quy trình chuẩn hóa gồm:

1.  **Tính giá trị trung bình (Mean - $\mu$):**
    $$\mu = rac{1}{d} \sum_{i=1}^{d} x_i$$
2.  **Tính phương sai (Variance - $\sigma^2$):**
    $$\sigma^2 = rac{1}{d} \sum_{i=1}^{d} (x_i - \mu)^2$$
3.  **Chuẩn hóa về phân phối chuẩn (Normalize):**
    $$\hat{x}_i = rac{x_i - \mu}{\sqrt{\sigma^2 + \epsilon}}$$
    *Trong đó $\epsilon$ là một số cực nhỏ (ví dụ $10^{-5}$) để tránh lỗi chia cho 0.*
4.  **Áp dụng hệ số tỉ lệ và dịch chuyển (Scale and Shift):**
    $$y_i = \gamma \hat{x}_i + eta$$
    *Trong đó $\gamma$ (gamma) và $eta$ (beta) là các tham số học được trong quá trình huấn luyện, cho phép mô hình khôi phục lại dải phân phối tối ưu.*
