# Khi AI biết nói dối và cách dạy nó làm người tốt

Chào mừng bạn đến với buổi học cuối cùng của hành trình xây dựng nanoGPT. Hôm nay, chúng ta sẽ được thưởng thức những tác phẩm thơ ca độc đáo do các "Nhà thơ AI" của các nhóm tự tay huấn luyện sáng tác. Nhưng bên cạnh niềm vui nhìn thấy cỗ máy viết chữ, chúng ta cũng cần đối mặt với một câu hỏi nghiêm túc: **Làm thế nào để kiểm soát một cỗ máy biết nói dối?**

Trong quá trình chạy thử, bạn sẽ thấy đôi khi AI tự chế ra những thông tin nghe rất thuyết phục nhưng hoàn toàn sai sự thật. Khoa học gọi đây là **Hallucination** (Ảo giác AI). Bản chất là vì GPT chỉ đoán chữ tiếp theo sao cho xuôi tai và hợp ngữ cảnh nhất, nó không hề có ý thức để đối chứng thông tin đó với thực tế thế giới. Đối với AI, `"Quang Trung và Nguyễn Huệ là hai anh em sinh đôi"` nghe có vẻ rất xuôi tai và hợp lý về cấu trúc câu, dù lịch sử không phải như vậy!

Bên cạnh đó, vì AI học từ internet, nếu dữ liệu internet có chứa những lời lẽ ghét bỏ, phân biệt đối xử hay định kiến (Bias), AI sẽ học luôn những thói hư tật xấu đó và nói ra những câu từ gây hại.

Để biến một "Base Model" (chỉ biết nối chữ tự do) thành một trợ lý AI ngoan ngoãn và hữu ích, các nhà khoa học phải thực hiện bước **Alignment** (Căn chỉnh mô hình). Người ta sử dụng phương pháp **RLHF** (Học tăng cường từ phản hồi của con người) — cho con người chấm điểm các câu trả lời của AI để dạy nó biết việc nào nên làm, việc nào cần tránh, giống như cách chúng ta dạy dỗ một đứa trẻ.

Hành trình lập trình AI của bạn chỉ mới bắt đầu. Hy vọng khóa học này đã mở toang cánh cửa hộp đen, giúp bạn không còn sợ hãi AI nữa mà hiểu rõ bản chất của nó để làm chủ công nghệ tương lai!
