# HƯỚNG DẪN THỰC HÀNH TRÊN GOOGLE COLAB
> **Dự án thực hành:** Huấn luyện mô hình MiniGPT tự viết văn bản / thơ lục bát.  
> **Yêu cầu môi trường:** Tài khoản Google để chạy Google Colab (miễn phí).

---

## 🚀 Quy trình thực hành từng bước (Step-by-Step)

### 📌 Bước 1: Tạo Notebook mới trên Google Colab
1.  Truy cập [Google Colab](https://colab.research.google.com/).
2.  Bấm chọn **New Notebook** (Sổ tay mới).
3.  Thay đổi bộ tăng tốc phần cứng sang GPU để học nhanh hơn: Chọn **Runtime** (Thời gian chạy) -> **Change runtime type** (Thay đổi loại thời gian chạy) -> Chọn **T4 GPU** -> Bấm **Save**.

### 📌 Bước 2: Chuẩn bị dữ liệu huấn luyện (`input.txt`)
AI cần đọc một lượng văn bản lớn để bắt chước phong cách. Chúng ta có thể dùng Tiny Shakespeare hoặc thơ ca Việt Nam.
Tải dữ liệu Tiny Shakespeare bằng lệnh sau trong Colab:
```bash
!curl -o input.txt https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt
```
*Gợi ý dự án cá nhân:* Học sinh có thể tự tải lên file `input.txt` tự chọn (ví dụ: các bài thơ lục bát, lời bài hát, các đoạn hội thoại ngắn) bằng cách bấm vào biểu tượng Thư mục ở thanh công cụ bên trái Colab và chọn Upload.

### 📌 Bước 3: Chạy code huấn luyện MiniGPT
Copy toàn bộ mã nguồn của file [mini_gpt.py](file:///Users/dangvietchung/Aero-HowtoLLMs/docs/mini_gpt.py) dán vào một ô code trên Colab và bấm nút Run.

Học sinh sẽ quan sát:
1.  **Số tham số:** Mô hình mẫu có khoảng hơn 300K tham số (rất nhỏ so với hàng tỷ tham số của GPT-4, giúp học sinh chạy được trên phần cứng yếu).
2.  **Chỉ số Loss (Sai số):** Ban đầu loss sẽ rất cao (~3.4) do mô hình chỉ đoán mò. Qua các lượt lặp (iterations), loss sẽ giảm dần xuống dưới 1.5.
3.  **Văn bản sinh ra (Generated Text):** Ban đầu là các chữ cái lộn xộn không có nghĩa, sau đó bắt đầu xuất hiện các từ có nghĩa và cấu trúc câu tương tự phong cách viết của Shakespeare.

---

## 🛠️ Thử nghiệm khoa học: Tùy biến siêu tham số (Hyperparameters)

Học sinh hãy thử thay đổi các thông số ở đầu file code và ghi nhận sự thay đổi:
*   `max_iters`: Tăng lên `5000` hoặc `10000` xem văn bản sinh ra có rõ nghĩa hơn không?
*   `n_layer`: Tăng số tầng Transformer từ `3` lên `6`. Ghi nhận sự thay đổi về thời gian chạy mỗi bước và tổng số lượng tham số.
*   `lr` (Learning Rate): Thử đặt learning rate lên `1e-1` (quá cao) và `1e-5` (quá thấp) để quan sát hiện tượng loss bị lỗi không giảm hoặc giảm cực kỳ chậm.
