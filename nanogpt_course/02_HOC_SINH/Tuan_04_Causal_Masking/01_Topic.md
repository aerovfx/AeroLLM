# Tuần 4: Causal Masking — Topic Overview
> **Mục tiêu học tập:** Hiểu rõ tại sao cần cơ chế Tam giác dưới (Causal Masking); cấu trúc ma trận tam giác dưới `tril`; và cách áp dụng phép `masked_fill` bằng giá trị $-\infty$ trong Attention.

---

```mermaid
mindmap
  root((Tuần 4: Causal Mask))
    Lý do sử dụng
      Tự hồi quy Autoregressive
      Không nhìn trộm tương lai
      Mô phỏng quy luật thời gian
    Cấu trúc ma trận
      Tam giác dưới tril
      Đường chéo chính
      Giá trị 0 và 1
    Áp dụng trong PyTorch
      masked_fill
      Điền âm vô cùng -inf
      Softmax triệt tiêu về 0
```
