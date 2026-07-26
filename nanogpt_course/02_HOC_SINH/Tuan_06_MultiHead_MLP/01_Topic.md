# Tuần 6: Multi-Head Attention & Lớp MLP — Topic Overview
> **Mục tiêu học tập:** Hiểu nguyên lý hoạt động song song của cơ chế Multi-Head Attention; cách chia nhỏ chiều vector để phân bổ cho các đầu chú ý; vai trò của lớp MLP (Feed-Forward) và các hàm phi tuyến tính.

---

```mermaid
mindmap
  root((Tuần 6: Heads & MLP))
    Multi-Head Attention
      Nhiều đầu chạy song song
      Mỗi đầu bắt 1 liên kết khác nhau
      Ghép nối Concatenate đầu ra
    Lớp MLP
      Feed-Forward network
      Mạng suy nghĩ độc lập
      Biến đổi phi tuyến tính
    Hàm kích hoạt
      GELU vs ReLU
      Độ dốc mượt mà
      Tránh chết nơ-ron
```
