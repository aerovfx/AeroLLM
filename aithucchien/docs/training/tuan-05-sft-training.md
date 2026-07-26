# Tuần 5: Tinh chỉnh Giám sát (Supervised Fine-Tuning - SFT)

Biến đổi mô hình cơ sở thành một trợ lý biết nghe lời thông qua SFT chất lượng cao.

## Cấu hình Framework Axolotl / TRL
- **Prompt Template:** Áp dụng mẫu trò chuyện chuẩn (ChatML, Llama-3 Instruct template).
- **Siêu tham số SFT:**
  - `learning_rate`: Đặt trong khoảng `2e-5` cho Full FT, hoặc `1e-4` cho LoRA.
  - `warmup_ratio`: Thường chọn `0.03` (3% số bước đầu tiên tăng dần tốc độ học).
  - `packing`: Gộp các câu thoại ngắn vào cùng một độ dài context tối đa (ví dụ 2048) để tối đa hóa hiệu năng GPU.
