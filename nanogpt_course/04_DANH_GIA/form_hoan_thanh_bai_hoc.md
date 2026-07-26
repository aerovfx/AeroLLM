# PHIẾU BÁO CÁO HOÀN THÀNH BÀI HỌC & NHẬT KÝ LẬP TRÌNH
> **Học phần:** Tự xây dựng nanoGPT cho học sinh THPT  
> **Hướng dẫn:** Học sinh ghi nhận tiến độ thực hiện bài học theo từng tuần và lưu lại các minh chứng kỹ thuật (chỉ số loss, mẫu chữ sinh ra).

---

## 👤 Thông tin cá nhân / Nhóm
*   **Họ và tên học sinh (hoặc tên Nhóm):** ........................................................................
*   **Lớp:** ............................................................  **Trường:** ....................................................
*   **Link Github/Google Drive chứa dự án cá nhân:** ..............................................................

---

## 📅 Bảng theo dõi tiến độ hoàn thành 10 tuần học

Học sinh tích dấu `[x]` vào các buổi học đã hoàn thành đầy đủ lý thuyết, bài tập và chạy code thực hành:

- `[ ]` **Tuần 1:** Đã hiểu bản chất Next-token prediction, chạy thử thành công file `mini_gpt.py` mặc định.
- `[ ]` **Tuần 2:** Đã hoàn thành thử thách viết code `encode`/`decode` ký tự và tạo được file dữ liệu `input.txt` riêng.
- `[ ]` **Tuần 3:** Đã phân biệt được `nn.Embedding` và `nn.Linear`, cộng thành công tọa độ Position Embedding.
- `[ ]` **Tuần 4:** Đã thực hành nhân ma trận tam giác dưới `tril` che giấu thông tin tương lai.
- `[ ]` **Tuần 5:** Đã trả lời được câu hỏi ôn tập về 3 vector $Q, K, V$ và lý do toán học chia căn $\sqrt{d_k}$.
- `[ ]` **Tuần 6:** Đã giải thích được vai trò chạy song song của Multi-Head Attention và hàm phi tuyến GELU trong MLP.
- `[ ]` **Tuần 7:** Đã ráp nối hoàn chỉnh cấu trúc một khối Transformer Block và vẽ được sơ đồ luồng dữ liệu.
- `[ ]` **Tuần 8:** Đã chạy huấn luyện thành công mô hình trên GPU Google Colab, vẽ được biểu đồ Loss giảm dần.
- `[ ]` **Tuần 9:** Đã thử nghiệm sinh thơ/văn bản với ít nhất 3 mức `Temperature` khác nhau và ghi nhận kết quả.
- `[ ]` **Tuần 10:** Đã hoàn thành báo cáo đồ án "AI làm thơ", thuyết trình sản phẩm trước lớp và tham gia tranh biện đạo đức AI.

---

## 📈 Nhật ký thông số huấn luyện (Training Log)
Học sinh ghi lại kết quả thử nghiệm chạy huấn luyện tốt nhất của mình:

| Lần thử | Số layer (`n_layer`) | Số đầu attention (`n_head`) | Tốc độ học (`lr`) | Số vòng lặp (`max_iters`) | Chỉ số Loss cuối cùng | Đánh giá chất lượng chữ sinh ra (Tốt/Trung bình/Kém) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Mẫu** | *3* | *4* | *1e-3* | *3000* | *1.45* | *Trung bình (đã ra từ có nghĩa nhưng câu chưa mượt)* |
| **1** | | | | | | |
| **2** | | | | | | |
| **3** | | | | | | |

*   **Mẫu đoạn thơ/văn bản hay nhất do AI của bạn tự sáng tác:**
    > *........................................................................................................................................*
    > *........................................................................................................................................*
    > *........................................................................................................................................*

---

## ✍️ Xác nhận của giáo viên
*   **Nhận xét của Giáo viên:** ............................................................................................................
*   **Đánh giá tiến độ:** `[ ]` Hoàn thành xuất sắc | `[ ]` Đạt yêu cầu | `[ ]` Cần hoàn thiện thêm
*   **Chữ ký xác nhận của Giáo viên:** ........................................................
