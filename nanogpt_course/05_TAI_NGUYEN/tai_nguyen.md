# TÀI NGUYÊN HỌC TẬP VÀ LIÊN KẾT THAM KHẢO
> **Học phần:** Tự xây dựng nanoGPT cho học sinh THPT  
> **Tổng hợp:** Các nguồn tài liệu, video giảng dạy chất lượng cao và hướng dẫn chuyên sâu bổ trợ cho học trình.

## 💻 Mã nguồn và Sổ tay thực hành (Local Code & Notebooks)

Học sinh có thể truy cập và sử dụng trực tiếp các file code được lưu trữ ngay trong thư mục tài nguyên này:
*   **[mini_gpt.py (Mã nguồn Python)](file:///Users/dangvietchung/Aero-HowtoLLMs/nanogpt_course/05_TAI_NGUYEN/mini_gpt.py):** File chạy trực tiếp offline trên máy tính cá nhân.
*   **[mini_gpt.ipynb (Sổ tay Jupyter Notebook)](file:///Users/dangvietchung/Aero-HowtoLLMs/nanogpt_course/05_TAI_NGUYEN/mini_gpt.ipynb):** Phiên bản sổ tay để mở trên Google Colab.

---

## 🚀 Hướng dẫn chạy Sổ tay trên Google Colab (Dành cho máy cấu hình yếu)

Nếu máy tính cá nhân hoặc máy tính phòng Lab của bạn có cấu hình yếu (không có card đồ họa GPU hoặc RAM yếu), hãy sử dụng **Google Colab** để mượn GPU miễn phí của Google để chạy huấn luyện:

### 📥 Bước 1: Tải file Jupyter Notebook về máy
1.  Bấm vào file **[mini_gpt.ipynb](file:///Users/dangvietchung/Aero-HowtoLLMs/nanogpt_course/05_TAI_NGUYEN/mini_gpt.ipynb)**.
2.  Tải tệp tin này về máy tính cá nhân của bạn dưới định dạng `.ipynb`.

### 📤 Bước 2: Tải lên Google Colab
1.  Mở trình duyệt web và truy cập: [colab.research.google.com](https://colab.research.google.com/).
2.  Trong hộp thoại hiện ra, chọn tab **Upload** (Tải lên).
3.  Kéo thả hoặc chọn tệp `mini_gpt.ipynb` bạn vừa tải về để tải lên Colab.

### ⚡ Bước 3: Kích hoạt GPU miễn phí và Chạy
1.  Trên thanh thực đơn của Colab, chọn **Runtime** (Thời gian chạy) -> **Change runtime type** (Thay đổi loại thời gian chạy).
2.  Tại mục *Hardware accelerator* (Bộ tăng tốc phần cứng), chọn **T4 GPU** (đây là card đồ họa miễn phí có hiệu năng rất mạnh).
3.  Bấm **Save** (Lưu).
4.  Bấm nút **Run** (Chạy) ở từng ô lệnh từ trên xuống dưới để tiến hành tải dữ liệu, cấu hình mô hình, chạy huấn luyện và sinh thơ tự động!

---

## 🎥 Video bài giảng chất lượng cao (Youtube)

1.  **Bài giảng gốc của Andrej Karpathy:**
    *   [Let's build GPT: from scratch, in code (YouTube)](https://www.youtube.com/watch?v=kCc8FmEb1nY): Bài giảng 2 tiếng huyền thoại, từng bước xây dựng mô hình GPT từ con số 0 của cựu giám đốc AI tại Tesla và đồng sáng lập OpenAI. Đây là tài liệu nguồn chính của dự án nanoGPT.
    *   [Series Zero To Hero của Karpathy](https://karpathy.ai/zero-to-hero.html): Khóa học lập trình mạng thần kinh cực kỳ dễ hiểu dành cho người bắt đầu.

2.  **Kênh giải thích trực quan về Transformer:**
    *   [3Blue1Brown - But what is a GPT? (YouTube)](https://www.youtube.com/watch?v=wjZofJX0v4M): Video mô phỏng đồ họa 3D trực quan sinh động về cách hoạt động của Attention và Transformer. cực kỳ phù hợp cho học sinh THPT dễ hình dung.

---

## 📚 Tài liệu nghiên cứu chuyên sâu (Local Markdown Files)
Học sinh và giáo viên muốn tìm hiểu sâu hơn về mặt kỹ thuật có thể mở trực tiếp các bài viết sau trong không gian làm việc:

*   **Tổng quan kiến trúc ngôn ngữ lớn:** [docs/04_buildgpt/kien_truc_mo_hinh_ngon_ngu_lon.md](file:///Users/dangvietchung/Aero-HowtoLLMs/docs/04_buildgpt/kien_truc_mo_hinh_ngon_ngu_lon.md)
*   **Chi tiết về cơ chế Attention:** [docs/04_buildgpt/aero_llm_013_the_attention_algorithm_theory_.md](file:///Users/dangvietchung/Aero-HowtoLLMs/docs/04_buildgpt/aero_llm_013_the_attention_algorithm_theory_.md)
*   **Cơ chế tam giác dưới và mặt nạ nhân quả:** [docs/04_buildgpt/aero_llm_011_temporal_causality_via_linear_algebra_theory_.md](file:///Users/dangvietchung/Aero-HowtoLLMs/docs/04_buildgpt/aero_llm_011_temporal_causality_via_linear_algebra_theory_.md)
*   **Phân tích hàm Softmax và tham số Temperature:** [docs/04_buildgpt/aero_llm_05_softmax_temperature_academic_analysis.md](file:///Users/dangvietchung/Aero-HowtoLLMs/docs/04_buildgpt/aero_llm_05_softmax_temperature_academic_analysis.md)
*   **Mô phỏng trực quan nanoGPT:** [docs/04_buildgpt/aero_llm_025_visualizing_nano_gpt.md](file:///Users/dangvietchung/Aero-HowtoLLMs/docs/04_buildgpt/aero_llm_025_visualizing_nano_gpt.md)
