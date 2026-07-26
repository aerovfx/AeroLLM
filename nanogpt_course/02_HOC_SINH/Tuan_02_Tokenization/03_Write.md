# Người dịch mật thư của máy tính

Khi bạn gõ câu hỏi: `"Chào bạn!"` vào cửa sổ chat với AI, bạn có nghĩ cỗ máy thực sự đọc được ba từ tiếng Việt đó không? 

Sự thật là máy tính rất "mù chữ". Dù thông minh đến đâu, các siêu máy tính huấn luyện AI thực chất chỉ là những chiếc máy tính bỏ túi cỡ lớn: chúng không hiểu chữ cái, không hiểu từ ngữ, chúng chỉ hiểu **những con số**. Để AI có thể đọc được văn bản của con người, chúng ta cần một "người phiên dịch" đứng ở cổng vào. Công cụ này được gọi là **Tokenizer** (Bộ mã hóa từ vựng), và quy trình hoạt động của nó được gọi là **Tokenization**.

Hãy tưởng tượng bạn đang chơi trò gửi mật thư với bạn thân. Hai bạn quy ước một mật mã:
*   Chữ `a` đổi thành số `1`
*   Chữ `b` đổi thành số `2`
*   Chữ `c` đổi thành số `3`
*   ... và cứ thế tiếp tục.

Khi bạn muốn gửi chữ `"cab"`, bạn sẽ viết vào giấy dãy số: `[3, 1, 2]`. Bạn thân của bạn khi nhận được dãy số sẽ tra từ điển ngược lại để dịch ra chữ `"cab"`. Trong thế giới AI, hành động dịch từ chữ sang số được gọi là `encode` (mã hóa), và dịch từ số về chữ được gọi là `decode` (giải mã).

Trong nanoGPT bản đơn giản nhất, chúng ta dùng phương pháp **mã hóa ký tự** (Char-level Tokenization). Nếu văn bản của bạn chỉ chứa 65 ký tự khác nhau (chữ hoa, chữ thường, dấu cách, dấu câu), thì bộ từ vựng (Vocabulary) của bạn sẽ chỉ có kích thước là 65. Nhờ vậy, máy tính học rất nhanh và không bao giờ gặp phải từ lạ (vì mọi từ đều được tạo từ các chữ cái quen thuộc).

Tuy nhiên, các mô hình lớn như GPT-4 của OpenAI dùng thuật toán phức tạp hơn gọi là **BPE** (Byte Pair Encoding). Thay vì chia nhỏ từng ký tự, nó ghép các cụm từ thường đi cùng nhau thành một chỉ số (ví dụ từ `"học sinh"` có thể được gộp thành 1 chỉ số thay vì 8 chữ cái riêng lẻ). 

Tokenizer giúp AI đọc chữ siêu nhanh, nhưng cũng mang lại một số "tác dụng phụ" thú vị. Ví dụ, vì từ `"Strawberry"` được Tokenizer cắt thành các mảnh `str`, `aw`, `berry` nên khi bạn hỏi: *"Từ Strawberry có bao nhiêu chữ r?"*, ChatGPT đôi khi trả lời sai vì nó không thực sự nhìn thấy các chữ cái đơn lẻ, nó chỉ nhìn thấy các khối số!
