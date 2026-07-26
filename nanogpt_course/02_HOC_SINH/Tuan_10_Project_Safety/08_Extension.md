# Tuần 10: Showcase & Đạo Đức AI — Extension Material
> **Chủ đề mở rộng:** Quy trình RLHF (Reinforcement Learning from Human Feedback) chi tiết.

---

### Quy trình căn chỉnh RLHF gồm 3 giai đoạn chính:

```text
 ┌──────────────────────┐     ┌──────────────────────┐     ┌──────────────────────┐
 │ Giai đoạn 1: SFT     │  →  │ Giai đoạn 2: RM      │  →  │ Giai đoạn 3: RL      │
 └──────────────────────┘     └──────────────────────┘     └──────────────────────┘
   Tinh chỉnh có giám sát       Huấn luyện mô hình          Tối ưu hóa chính sách
   (Supervised Fine-Tuning)     chấm điểm (Reward Model)    bằng thuật toán PPO
```

1.  **Supervised Fine-Tuning (SFT - Tinh chỉnh có giám sát):**
    *   Thu thập các kịch bản đối thoại chất lượng cao do con người viết sẵn (Prompt - Response).
    *   Tinh chỉnh mô hình nền tảng trên tập dữ liệu này để nó biết cách trả lời dưới dạng một trợ lý hội thoại.
2.  **Reward Model (RM - Mô hình phần thưởng/chấm điểm):**
    *   Cho mô hình SFT sinh ra nhiều câu trả lời khác nhau cho cùng một câu hỏi.
    *   Con người tiến hành xếp hạng các câu trả lời này từ tốt nhất đến kém nhất (hoặc nguy hiểm nhất).
    *   Huấn luyện một mô hình nơ-ron phụ (Reward Model) để nó tự động chấm điểm số (phần thưởng) cho bất kỳ câu trả lời nào của AI giống như mắt nhìn của con người.
3.  **Reinforcement Learning (RL - Học tăng cường):**
    *   Sử dụng thuật toán tối ưu hóa chính sách (PPO - Proximal Policy Optimization) để cập nhật trọng số của mô hình SFT sao cho các câu trả lời sinh ra nhận được điểm số phần thưởng cao nhất từ Reward Model, đồng thời không bị lệch quá xa so với mô hình gốc để tránh hỏng kiến thức nền.
