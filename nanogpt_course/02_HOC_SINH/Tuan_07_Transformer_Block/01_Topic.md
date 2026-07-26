# Tuần 7: Transformer Block & Architecture — Topic Overview
> **Mục tiêu học tập:** Hiểu cách ráp nối Attention và MLP thành một khối Transformer hoàn chỉnh; vai trò của Residual Connection và Layer Normalization trong việc ổn định luồng dữ liệu.

---

```mermaid
mindmap
  root((Tuần 7: Block & Architecture))
    Khối Block hoàn chỉnh
      LayerNorm 1
      Multi-Head Attention
      LayerNorm 2
      MLP Block
    Cơ chế dòng dư
      Residual Connection
      Đường cộng x +
      Giải quyết biến mất gradient
    Ổn định số học
      Layer Normalization
      Chuẩn hóa trung bình và phương sai
      Tránh tràn số
    Đếm tham số
      Weights & Biases
      Kích thước mô hình
```
