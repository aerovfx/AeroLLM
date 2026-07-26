# Tuần 7: Cấu hình Huấn luyện Phân tán (Distributed Training)

Để huấn luyện các mô hình lớn trên 2, 4 hoặc 8 GPU song song mà không bị tràn bộ nhớ VRAM.

## Các công nghệ song song hóa
1. **DeepSpeed ZeRO-3:** Phân tán trọng số mô hình, gradient và trạng thái bộ tối ưu hóa trên toàn bộ các GPU.
2. **FSDP (Fully Sharded Data Parallel):** Kỹ thuật tích hợp sẵn trong PyTorch tương tự DeepSpeed, cấu hình mượt mà.
3. **LoRA / QLoRA:** Đóng băng mô hình nền tảng, chỉ cập nhật adapter để tiết kiệm 70% bộ nhớ đồ họa.
