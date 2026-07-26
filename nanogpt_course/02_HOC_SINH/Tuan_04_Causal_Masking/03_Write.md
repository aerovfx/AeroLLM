# Bịt mắt để đoán chữ

Hãy tưởng tượng bạn đang tham gia một kỳ thi điền vào chỗ trống. Đề bài yêu cầu bạn viết tiếp câu chuyện từ trái qua phải. Nhưng thay vì chỉ được xem những trang sách đã đọc, giám thị lại cho bạn xem trước toàn bộ trang tiếp theo bao gồm cả đáp án. Bạn sẽ làm gì? Tất nhiên là bạn sẽ "chép thẳng" đáp án mà không thèm suy nghĩ. 

Khi AI học ngôn ngữ, nếu không có cơ chế ngăn chặn, nó cũng sẽ "chép bài" như thế. Hiện tượng này được gọi là **Rò rỉ thông tin tương lai**. Để khắc phục, chúng ta cần một chiếc bịt mắt kỹ thuật mang tên **Causal Masking** (Mặt nạ nhân quả).

Trong PyTorch, chúng ta biểu diễn chiếc bịt mắt này bằng một **Ma trận tam giác dưới** (`tril`). Hãy nhìn vào ma trận kích thước 4x4 dưới đây:
```text
1  0  0  0
1  1  0  0
1  1  1  0
1  1  1  1
```
*   Dòng 1 đại diện cho từ thứ nhất: Nó chỉ được nhìn thấy chính nó (số 1), các vị trí tiếp theo bị che (số 0).
*   Dòng 2 đại diện cho từ thứ hai: Nó được nhìn thấy từ 1 và từ 2, không được nhìn thấy từ 3 và từ 4.
*   ... và cứ thế tiếp tục.

Trong phép toán Attention, các vị trí bị che (số 0) sẽ được thay thế bằng giá trị **âm vô cùng** ($-\infty$) thông qua hàm `masked_fill`. Khi đi qua hàm Softmax để tính tỷ lệ phần trăm chú ý, vì $e^{-\infty} = 0$, xác suất chú ý vào các từ tương lai sẽ bị triệt tiêu hoàn toàn về 0%. 

Nhờ chiếc bịt mắt kỳ diệu này, AI buộc phải động não và học cách suy luận từ các từ đã qua để đoán từ tiếp theo.
