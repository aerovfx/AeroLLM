# Giai Đoạn I: Chiến Lược & Thiết Lập Tiền Huấn Luyện

Trước khi bạn viết một dòng mã huấn luyện nào, đội của bạn phải xác định chiến lược của mình. "Thực tế lộn xộn" của việc huấn luyện mô hình là thành công phụ thuộc rất nhiều vào kế hoạch tốt.

Xác định "Kim chỉ nam Huấn luyện" của bạn:

- *Tại sao bạn lại huấn luyện mô hình này?*
- *Mục tiêu của bạn là hiệu suất hàng đầu (state-of-the-art) trên một benchmark cụ thể, một đóng góp nghiên cứu mới, hay một mô hình hiệu quả nhất cho một tác vụ giống như sản xuất?*

Câu trả lời cho "tại sao" sẽ định hướng mọi quyết định. Dưới đây là một số nguyên tắc hướng dẫn để giúp bạn thiết lập chiến lược tiền huấn luyện của mình:

- **Bắt đầu với các Thí nghiệm Riêng lẻ (Ablations):** Tất cả các mô hình lớn đều bắt đầu từ những thí nghiệm nhỏ. Trước khi mở rộng quy mô, hãy chạy nhiều "ablations" (thí nghiệm quy mô nhỏ) để kiểm tra các giả thuyết của bạn.
  
  
  
  
  > [Quy tắc Vàng]
  > Chỉ sửa đổi một biến tại một thời điểm (ví dụ: một nguồn dữ liệu duy nhất, một siêu tham số). Nếu bạn thay đổi nhiều thứ và hiệu suất cải thiện, bạn sẽ không biết điều gì đã gây ra nó.
- **Tuyển chọn Dữ liệu là Trên hết:** Mô hình của bạn chỉ tốt bằng dữ liệu của bạn. "Sự pha trộn dữ liệu là quan trọng nhất."
  
  
  
  - **Pha trộn Dữ liệu (Data Mix):** Xác định "chương trình giảng dạy" (training curricula) của bạn. Đây là sự kết hợp các nguồn dữ liệu (ví dụ: văn bản web chung, mã nguồn, toán học, dữ liệu đa ngôn ngữ) mà bạn sẽ sử dụng.
  - **Chất lượng > Số lượng:** Tập trung vào dữ liệu chất lượng cao, sạch và được lọc kỹ.
  - **Các giai đoạn:** Cân nhắc phát triển hỗn hợp dữ liệu của bạn theo từng giai đoạn. Ví dụ, bắt đầu với dữ liệu web chung và giới thiệu dữ liệu chuyên biệt (như mã nguồn hoặc toán học) sau này trong quá trình huấn luyện.
- **Kiến trúc & Siêu tham số (Hyperparameters):**
  
  
  
  - **Kiến trúc:** Đưa ra các lựa chọn có chủ đích về kiến trúc của mô hình (ví dụ: cơ chế chú ý (attention), mã hóa vị trí (positional encodings), Mixture of Experts (MoE)).
  - **Siêu tham số:** Chốt các lựa chọn ban đầu của bạn cho trình tối ưu hóa (optimizer, ví dụ: AdamW), lịch trình tốc độ học (learning rate schedule), và kích thước lô toàn cục (global batch size) dựa trên các thử nghiệm quy mô nhỏ của bạn.
