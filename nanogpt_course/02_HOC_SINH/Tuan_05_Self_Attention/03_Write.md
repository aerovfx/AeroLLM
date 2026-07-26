# Cuộc họp thảo luận của các từ vựng

Hãy tưởng tượng bạn đang đọc câu sau:
`"Con chó đuổi con mèo vì nó chạy nhanh."`

Làm thế nào bạn biết được từ **"nó"** trong câu đang ám chỉ con chó hay con mèo? Con người chúng ta hiểu ngay lập tức nhờ vào ngữ cảnh ngữ pháp và logic hành động (chó đuổi mèo vì chó chạy nhanh hơn, hoặc mèo chạy trốn vì mèo chạy nhanh). Nhưng đối với máy tính, các từ chỉ là những tọa độ vector vô hồn. Làm thế nào máy tính biết từ **"nó"** cần liên kết chặt chẽ với từ **"con chó"** (hoặc "con mèo")?

Đột phá lớn nhất giải quyết vấn đề này ra đời năm 2017 với tên gọi **Self-Attention** (Cơ chế tự chú ý) — trái tim của kiến trúc Transformer.

Cơ chế Self-Attention hoạt động giống như một **thư viện tra cứu thông tin thông minh**. Mỗi từ trong câu sẽ được cấp cho 3 vector riêng biệt, đóng vai trò khác nhau:
1.  **Query (Q) - Câu hỏi:** Đại diện cho nội dung từ đó đang tìm kiếm. (Ví dụ từ `"nó"` gửi đi câu hỏi: *"Tôi là ai? Ai đang thực hiện hành động chạy nhanh?"*).
2.  **Key (K) - Nhãn dán:** Đại diện cho đặc điểm nhận dạng của từ đó để các từ khác tìm kiếm. (Ví dụ từ `"con chó"` dán nhãn: *"Tôi là danh từ, giống đực, đang thực hiện hành động đuổi"*).
3.  **Value (V) - Giá trị:** Nội dung tri thức thực sự của từ đó mang lại nếu được chọn.

Quy trình ghép đôi diễn ra như sau:
*   Mỗi từ lấy **Query (Q)** của mình nhân với **Key (K)** của tất cả các từ khác trong câu (phép nhân ma trận Dot Product) để ra điểm số tương đồng.
*   Điểm số này được chia cho căn bậc hai kích thước vector để số không bị quá lớn, sau đó đi qua hàm **Softmax** để tạo thành các tỷ lệ phần trăm chú ý (ví dụ: từ `"nó"` chú ý 70% đến `"con chó"`, 20% đến `"con mèo"`, và 10% đến các từ khác).
*   Cuối cùng, lấy các tỷ lệ phần trăm này nhân với **Value (V)** tương ứng để trộn thông tin lại. 

Nhờ cơ chế này, từ `"nó"` sau khi đi qua lớp Attention sẽ mang đầy đủ đặc tính ý nghĩa của `"con chó"`. Đây chính là cách AI hiểu được ngữ cảnh sâu sắc của ngôn ngữ!
