# Tuần 8: Huấn Luyện Mô Hình — Extension Material
> **Chủ đề mở rộng:** Phép toán Cross-Entropy Loss chi tiết.

---

Hàm mất mát Entropy chéo (Cross-Entropy Loss) đánh giá mức độ sai lệch giữa phân phối xác suất dự đoán của mô hình $p$ và phân phối thực tế của nhãn đúng $q$ (dưới dạng one-hot vector).

Công thức tính cho một mẫu dữ liệu:
$$L = - \sum_{c=1}^{C} q_c \log(p_c)$$
Vì $q$ là one-hot vector (chỉ bằng 1 tại vị trí đáp án đúng $c^*$, và bằng 0 tại các vị trí khác), công thức thu gọn thành:
$$L = - \log(p_{c^*})$$
Trong đó $p_{c^*}$ là xác suất mô hình gán cho đáp án đúng sau khi đi qua hàm Softmax:
$$p_{c^*} = rac{e^{z_{c^*}}}{\sum_{j=1}^{C} e^{z_j}}$$
*Với $z$ là logits đầu ra của mô hình.*

### Ý nghĩa toán học:
*   Nếu xác suất dự đoán cho đáp án đúng tiệm cận 1 ($p_{c^*} 	o 1$), thì Loss tiệm cận 0 ($L 	o 0$).
*   Nếu xác suất dự đoán cho đáp án đúng tiệm cận 0 ($p_{c^*} 	o 0$), thì Loss bùng nổ tiến về vô cùng ($L 	o +\infty$).
*   Mục tiêu tối ưu hóa của AdamW là tìm các trọng số giúp cực tiểu hóa giá trị Loss trung bình trên toàn tập dữ liệu.
