# Tập ném bóng rổ — Cách AI tự sửa lỗi

Làm thế nào một đứa trẻ học cách ném bóng vào rổ? 
*   Lần ném thứ nhất, đứa trẻ dùng lực quá mạnh, quả bóng bay vọt qua bảng rổ. Bộ não ghi nhận: *"Lực quá mạnh, lệch hướng lên"*.
*   Lần ném thứ hai, đứa trẻ giảm lực tay xuống, nhưng bóng lại rơi ngắn trước rổ. Bộ não ghi nhận: *"Lực hơi yếu"*.
*   Qua hàng trăm lần thử và điều chỉnh lực tay một chút, đứa trẻ sẽ tự tìm ra tư thế và lực ném hoàn hảo để bóng vào rổ liên tục.

Quá trình huấn luyện (Training) một mô hình ngôn ngữ lớn hoạt động theo nguyên lý tương tự. Bộ não AI ban đầu có các tham số (trọng số) hoàn toàn ngẫu nhiên. Vòng lặp huấn luyện là chuỗi hành động lặp đi lặp lại hàng nghìn lần:

1.  **Lấy lô dữ liệu (Get Batch):** Lấy một nhóm ngẫu nhiên các đoạn câu đầu vào `X` và đáp án đúng `Y`. Đáp án `Y` chính là chuỗi `X` nhưng dịch sang phải 1 ký tự (vì ta đoán chữ tiếp theo).
2.  **Đoán và Tính sai số (Forward & Loss):** Cho mô hình đoán ký tự tiếp theo và đo mức độ "ngạc nhiên" của nó bằng hàm **Cross-Entropy Loss**. Nếu mô hình đoán sai bét, Loss sẽ rất cao; nếu đoán đúng tự tin, Loss sẽ rất nhỏ.
3.  **Truyền ngược sai số (Backward):** Thuật toán lan truyền ngược (Backpropagation) tính toán xem *"để giảm Loss, cần phải chỉnh mỗi tham số trong mô hình lên hay xuống bao nhiêu"*. Hướng chỉnh này gọi là **Gradient** (Độ dốc).
4.  **Cập nhật trọng số (Step):** Bộ tối ưu hóa **AdamW** tiến hành chỉnh nhẹ các trọng số theo hướng Gradient với một bước chân cực nhỏ gọi là **Learning Rate** (Tốc độ học).

Cứ như vậy, qua hàng nghìn vòng lặp, mô hình sẽ tự sửa đổi "bộ não" của mình cho đến khi nó có thể đoán trúng chữ tiếp theo với độ chính xác cao.
