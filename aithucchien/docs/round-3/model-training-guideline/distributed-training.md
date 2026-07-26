# Giai Đoạn II: Huấn Luyện Phân Tán (Distributed Training)

Để huấn luyện ở quy mô lớn, bạn phải song song hóa mô hình của mình trên nhiều GPU. Mục tiêu là tìm sự cân bằng phù hợp giữa tính toán, giao tiếp và bộ nhớ.

## Một Số Kỹ Thuật Song Song Hữu Ích​

Kỹ ThuậtMô TảTrường Hợp Sử Dụng**Song song Dữ liệu (Data Parallelism - DP)**Sao chép toàn bộ mô hình trên mọi GPU và chia lô dữ liệu cho từng GPU.Luôn là điểm khởi đầu, làm nền tảng cho hầu hết các thiết lập huấn luyện.**Song song Tensor (Tensor Parallelism - TP)**Chia một lớp (layer) duy nhất (ma trận trọng số của nó) trên nhiều GPU. Ví dụ, trong TP 2 chiều, GPU-A giữ nửa đầu của trọng số và GPU-B giữ nửa còn lại.Khi một lớp duy nhất quá lớn để vừa với bộ nhớ của một GPU.**Song song Pipeline (Pipeline Parallelism - PP)**Chia toàn bộ mô hình theo chiều dọc, mỗi GPU xử lý một chuỗi các lớp. Ví dụ: GPU-A chạy các lớp 1-8, GPU-B chạy các lớp 9-16, v.v., giống như một dây chuyền lắp ráp. Điều này đòi hỏi "phân lô vi mô" (micro-batching) cẩn thận để giữ cho tất cả các GPU luôn bận rộn.Khi toàn bộ mô hình (không chỉ một lớp) quá lớn để vừa trên một GPU.**Song song Chuyên gia (Expert Parallelism - EP)**Kỹ thuật chuyên biệt, chia các "chuyên gia" (experts) trên các GPU khác nhau.Chỉ sử dụng cho các mô hình Mixture of Experts (MoE).

## So sánh chiến lược: Full Fine-tuning vs. Tinh chỉnh Hiệu quả (LoRA)​

> [Lưu ý Chiến lược]
> Trước khi bắt đầu, đội của bạn phải đưa ra một quyết định quan trọng về phương pháp tinh chỉnh

### Full Fine-tuning (Huấn luyện Toàn bộ):​

**Mô tả:** Bạn cập nhật toàn bộ trọng số của mô hình.

**Ưu điểm:** Có khả năng đạt được chất lượng cao nhất vì mô hình học hỏi sâu hơn.

**Nhược điểm:** Yêu cầu VRAM cực kỳ cao. Để huấn luyện toàn bộ một mô hình 7B, bạn có thể cần 4-8 GPU A100/H100 80GB.

### Tinh chỉnh Hiệu quả (ví dụ: LoRA/QLoRA):​

**Mô tả:** Bạn "đóng băng" (freeze) mô hình chính và chỉ huấn luyện một số lượng nhỏ các trọng số "adapter" (thích ứng) được thêm vào.

**Ưu điểm:** Yêu cầu VRAM thấp hơn rất nhiều (có thể huấn luyện mô hình 7B-9B trên 1-2 GPU cao cấp) và huấn luyện nhanh hơn đáng kể.

**Nhược điểm:** Chất lượng có thể thấp hơn một chút so với Full FT trong một số tác vụ, nhưng thường là rất cạnh tranh.

> [Khuyến nghị của BTC]
> Các đội nên ưu tiên bắt đầu với LoRA hoặc QLoRA. Phương pháp này cho phép chu kỳ thử nghiệm nhanh hơn, tiết kiệm tài nguyên và thường mang lại kết quả xuất sắc. Chỉ nên xem xét Full Fine-tuning nếu bạn có đủ tài nguyên và đã thử nghiệm thành công với LoRA.

Để hiểu rõ hơn về sự khác biệt giữa các kỹ thuật này, bạn có thể tham khảo thêm tại đây.

## Gợi ý Training Frameworks​

FrameworkSFTPORLMulti-modalFullFTLoRADistributedTRL✅✅✅✅✅✅✅Axolotl✅✅✅✅✅✅✅OpenInstruct✅✅✅❌✅✅✅Unsloth✅✅✅✅✅✅✅vERL✅❌✅✅✅✅✅Prime RL✅❌✅❌✅✅✅PipelineRL❌❌✅❌✅✅✅ART❌❌✅❌❌✅❌TorchForge✅❌✅❌✅❌✅NemoRL✅✅✅❌✅❌✅OpenRLHF✅✅✅❌✅✅✅
