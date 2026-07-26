# Tuần 9: Suy Luận & Lấy Mẫu — Topic Overview
> **Mục tiêu học tập:** Hiểu quy trình sinh văn bản tự hồi quy (Autoregressive Inference); vai trò của tham số Temperature; và cách hoạt động của phương pháp lấy mẫu xác suất Multinomial, Top-K.

---

```mermaid
mindmap
  root((Tuần 9: Suy Luận))
    Quy trình sinh tự hồi quy
      Nhận ngữ cảnh context
      Đoán token tiếp theo
      Nối vào và lặp lại
    Điều chỉnh sáng tạo
      Tham số Temperature
      Nhiệt độ thấp - An toàn
      Nhiệt độ cao - Sáng tạo
    Phương pháp lấy mẫu
      Greedy - Chọn từ lớn nhất
      Multinomial - Bốc thăm
      Top-K - Lọc từ khả dĩ nhất
```
