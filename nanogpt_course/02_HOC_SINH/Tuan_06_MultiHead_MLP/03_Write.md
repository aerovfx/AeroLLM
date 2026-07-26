# Hội nghị chuyên gia và Thời gian tự ngẫm nghĩ

Khi con người đọc một câu thơ, bộ não của chúng ta không chỉ chú ý đến một khía cạnh duy nhất. 
*   Một phần trong não chú ý đến **vần điệu** (nhạc điệu của câu).
*   Một phần chú ý đến **chủ ngữ và vị ngữ** (ngữ pháp).
*   Một phần chú ý đến **cảm xúc** (vui hay buồn).

Nếu mô hình AI chỉ có một đầu chú ý duy nhất (Single-head attention), nó sẽ bị giới hạn góc nhìn và chỉ học được một loại liên kết thông tin. Để AI trở nên thông minh vượt trội, chúng ta cần cơ chế **Multi-Head Attention** (Nhiều đầu chú ý song song). 

Hãy tưởng tượng bạn đang tổ chức một cuộc họp thiết kế sản phẩm. Thay vì chỉ có một người đưa ra quyết định, bạn mời đến 4 chuyên gia: một người lo tài chính, một người lo mỹ thuật, một người lo kỹ thuật và một người lo marketing. Cả 4 chuyên gia này cùng đọc một yêu cầu thiết kế (Query, Key, Value) nhưng dưới góc nhìn chuyên môn khác nhau của mình. Sau khi thảo luận xong, ta ghép tất cả kết quả của 4 người lại (Concatenate) thành một bản thiết kế tối ưu nhất.

Tuy nhiên, sau khi họp nhóm xong (Attention), mỗi từ vựng cần có không gian riêng để xử lý thông tin nhận được và rút ra kết luận cho riêng mình. Đây chính là nhiệm vụ của lớp **MLP (Multi-Layer Perceptron)** hay còn gọi là Feed-Forward Network. 

Trong lớp MLP, thông tin của từ sẽ được mở rộng ra gấp 4 lần để "suy nghĩ" sâu hơn, đi qua hàm kích hoạt phi tuyến tính **GELU** để loại bỏ các thông tin vô ích, rồi nén lại kích thước cũ. Phép toán này chạy độc lập cho từng từ, không có sự trao đổi chéo giữa các từ, giúp bảo toàn tính cá nhân của dữ liệu.
