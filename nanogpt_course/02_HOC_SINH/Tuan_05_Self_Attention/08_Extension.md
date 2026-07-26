# Tuần 5: Self-Attention — Extension Material
> **Chủ đề mở rộng:** Tại sao phép toán nhân ma trận và chia căn $\sqrt{d_k}$ lại quan trọng?

---

Trong cơ chế Scaled Dot-Product Attention:
$$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$$

Khi số chiều vector $d_k$ (kích thước của Key) lớn, các giá trị tích vô hướng $QK^T$ có xu hướng tăng lên rất lớn về mặt độ lớn. 

### Lý do toán học:
Giả sử các thành phần của vector $q$ và $k$ là các biến ngẫu nhiên độc lập có trung bình bằng 0 và phương sai bằng 1. Tích vô hướng của chúng:
$$q \cdot k = \sum_{i=1}^{d_k} q_i k_i$$
sẽ có trung bình bằng 0 và phương sai bằng $d_k$.

Nếu không chia cho $\sqrt{d_k}$, phương sai lớn sẽ đẩy giá trị của phép nhân lên rất cao. Khi đi qua hàm Softmax:
$$\text{softmax}(x)_i = \frac{e^{x_i}}{\sum e^{x_j}}$$
những giá trị cực đại này sẽ khiến hàm Softmax bị bão hòa (tập trung gần như 100% vào giá trị lớn nhất, các giá trị khác bằng 0). Tại các vùng bão hòa này, đạo hàm (gradient) của hàm Softmax sẽ cực kỳ nhỏ (tiệm cận 0), dẫn đến hiện tượng **biến mất gradient** (vanishing gradient) trong quá trình lan truyền ngược, khiến mô hình không thể học được.

Chia cho $\sqrt{d_k}$ giúp kéo phương sai của kết quả về lại 1, đảm bảo hàm Softmax hoạt động ở vùng có độ dốc tốt nhất, giúp gradient truyền đi ổn định.
