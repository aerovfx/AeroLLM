# Tuần 8: Huấn Luyện Mô Hình — Topic Overview
> **Mục tiêu học tập:** Hiểu rõ cấu trúc vòng lặp huấn luyện (Training Loop); cách chuẩn bị lô dữ liệu (Batching); phép toán Cross-Entropy Loss; và thuật toán tối ưu hóa AdamW.

---

```mermaid
mindmap
  root((Tuần 8: Huấn Luyện))
    Dữ liệu lô Batch
      Đầu vào X
      Đáp án Y dịch phải 1
      Kích thước Batch Size
    Đo lường sai số
      Cross-Entropy Loss
      Thước đo ngạc nhiên
      Mục tiêu giảm Loss
    Bộ tối ưu AdamW
      Lan truyền ngược Backprop
      Tính độ dốc Gradient
      Cập nhật trọng số
    Hạ tầng GPU
      Tương thích CUDA
      Tính toán song song
```
