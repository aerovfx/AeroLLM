# Tuần 5: Self-Attention — Topic Overview
> **Mục tiêu học tập:** Nắm vững cấu trúc thuật toán Self-Attention hoàn chỉnh; giải thích được ý nghĩa và cơ chế tính toán của các vector Query (Q), Key (K), Value (V); hiểu cách chuẩn hóa bằng chia căn bậc hai chiều vector ($\sqrt{d_k}$) và Softmax.

---

```mermaid
mindmap
  root((Tuần 5: Self-Attention))
    Thành phần Q K V
      Query - Câu hỏi / Tôi tìm gì
      Key - Nhãn dán / Tôi chứa gì
      Value - Giá trị / Tri thức của tôi
    Quy trình tính toán
      Bước 1: Tích vô hướng Q x K
      Bước 2: Chia căn d_k để ổn định số học
      Bước 3: Causal Masking (che tương lai)
      Bước 4: Softmax ra trọng số xác suất
      Bước 5: Nhân với ma trận V
    Ứng dụng thực tế
      Liên kết từ vựng theo ngữ cảnh
      Tìm kiếm thông tin liên quan
      Ráp nối thông tin đa chiều
```
