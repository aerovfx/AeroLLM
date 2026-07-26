# TIÊU CHÍ ĐÁNH GIÁ & CÂU HỎI TỰ KIỂM TRA
> **Học phần:** Tự xây dựng nanoGPT cho học sinh THPT  
> **Mục tiêu:** Kiểm tra mức độ hiểu bản chất kiến trúc Transformer và đánh giá kết quả thực hành dự án AI làm thơ.

---

## 📊 Rubric chấm điểm dự án AI sáng tạo (Tổng: 100 điểm)

| Tiêu chí | Xuất sắc (85 - 100 điểm) | Đạt (65 - 84 điểm) | Cần cố gắng (dưới 65 điểm) | Trọng số |
| :--- | :--- | :--- | :--- | :---: |
| **Dữ liệu đầu vào (Data)** | File `input.txt` được chuẩn bị chu đáo, làm sạch định dạng, có phong cách rõ ràng (thơ lục bát, nhạc Rap, truyện cổ tích). | File dữ liệu có dung lượng vừa phải nhưng chưa được loại bỏ kỹ các ký tự lạ hoặc định dạng lỗi. | Dữ liệu quá ít (dưới 10KB), hoặc có quá nhiều ký tự lỗi khiến mô hình không học được. | **20%** |
| **Tùy biến mã nguồn (Code customization)** | Biết cách thay đổi các siêu tham số một cách hợp lý, tối ưu hóa kích thước mô hình phù hợp với thời gian huấn luyện. | Chỉ chạy code mặc định mà không thử nghiệm thay đổi hoặc giải thích được các siêu tham số. | Không chạy được chương trình hoàn chỉnh, code gặp lỗi cú pháp nghiêm trọng. | **25%** |
| **Quy trình Huấn luyện (Training)** | Huấn luyện mô hình đạt chỉ số Loss thấp mong đợi, vẽ được biểu đồ Loss giảm dần qua các bước lặp. | Huấn luyện nửa chừng dừng lại, không tối ưu hóa chỉ số loss hoặc không giải thích được ý nghĩa của Loss. | Không huấn luyện được mô hình hoặc chỉ số loss không đổi (bị nổ/biến mất gradient). | **25%** |
| **Sản phẩm Sinh chữ (Generation)** | Sinh được văn bản/thơ có vần điệu, cấu trúc giống phong cách gốc; giải thích được ảnh hưởng của tham số `Temperature`. | AI sinh được chữ đọc hiểu được nhưng câu cú lộn xộn hoặc bị lặp từ liên tục do đặt temperature chưa tốt. | AI sinh ra toàn các chuỗi ký tự vô nghĩa hoặc bị kẹt lặp lại một từ duy nhất. | **30%** |

---

## ❓ Câu hỏi tự kiểm tra lý thuyết (Self-check Quiz)

Học sinh trả lời các câu hỏi sau để ôn tập kiến thức:
1.  **Câu hỏi về Causal Mask:** Tại sao trong kiến trúc Transformer dùng cho GPT, ma trận Attention phải che đi các giá trị tương lai? Nếu không che thì mô hình sẽ bị lỗi gì khi mang đi sinh văn bản thực tế?
2.  **Câu hỏi về Position Embedding:** Nếu ta loại bỏ Position Embedding ra khỏi mô hình GPT, AI có phân biệt được hai câu `"Tôi yêu lập trình"` và `"Lập trình yêu tôi"` không? Giải thích vì sao.
3.  **Câu hỏi về Loss:** Chỉ số Loss (sai số) giảm dần trong quá trình huấn luyện thể hiện điều gì? Nếu chạy 3000 bước mà Loss vẫn ở mức cao (~3.2), bạn nên kiểm tra những yếu tố nào đầu tiên?
4.  **Câu hỏi về Temperature:** Nếu muốn mô hình sinh ra câu trả lời chính xác, mang tính logic cao (như giải toán), bạn nên đặt `Temperature` cao (ví dụ `1.5`) hay thấp (ví dụ `0.2`)? Vì sao?
