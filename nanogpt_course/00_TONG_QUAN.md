# TỔNG QUAN HỌC PHẦN: TỰ XÂY DỰNG nanoGPT CHO HỌC SINH THPT
> **Đối tượng:** Học sinh THPT (Lớp 10 - 12) đã học qua lập trình Python cơ bản.  
> **Thời lượng:** 10 tuần (mỗi tuần 1 buổi 90 - 120 phút).  
> **Phương pháp giảng dạy:** Học qua dự án (Project-Based Learning), sử dụng các ví dụ trực quan sinh động và thực hành viết mã nguồn trực tiếp trên Google Colab.

---

## 🎯 Chuẩn đầu ra (Learning Outcomes)
Học sinh hoàn thành học phần sẽ đạt được:
1.  **Kiến thức nền tảng về AI:** Hiểu bản chất các mô hình sinh chữ tự hồi quy (Autoregressive) là trò chơi tính xác suất đoán từ tiếp theo.
2.  **Mô tả được kiến trúc Transformer:** Phân biệt được các khối chức năng chính gồm: Tokenization, Embedding, Causal Self-Attention, Multi-Head Attention, MLP và Softmax/Temperature.
3.  **Kỹ năng lập trình PyTorch:** Đọc hiểu và tùy chỉnh được mã nguồn mô hình GPT tối giản [mini_gpt.py](file:///Users/dangvietchung/Aero-HowtoLLMs/docs/mini_gpt.py) (~150 dòng lệnh).
4.  **Huấn luyện mô hình thực tế:** Biết cách tự chuẩn bị dữ liệu văn bản tiếng Việt/tiếng Anh, đưa lên Google Colab cấu hình GPU, tinh chỉnh tham số để AI tự sinh văn bản bắt chước phong cách dữ liệu đầu vào.

---

## 🗂️ Sơ đồ cấu trúc học phần (Hệ thống học liệu Science)
Chương trình học được tổ chức khoa học theo 6 cấu phần chính của dự án `Science/HOC_LIEU`:

```text
nanogpt_course/
├── 00_TONG_QUAN.md              # Tài liệu tổng quan này
├── 01_GIAO_VIEN/                # Kế hoạch bài dạy chi tiết qua 10 tuần và giáo án mẫu
│   └── ke_hoach_giang_day.md
├── 02_HOC_SINH/                 # Tài liệu học tập, thuật ngữ, bài tập của học sinh theo tuần
│   ├── Tuan_01_Intro/           # Tuần 1: Giới thiệu AI & Mô hình ngôn ngữ lớn (LLM)
│   ├── Tuan_02_Tokenization/    # Tuần 2: Tokenization - Mã hóa văn bản thành số nguyên
│   ├── Tuan_03_Embedding/       # Tuần 3: Embedding & Position - Bản đồ ý nghĩa & Thứ tự từ
│   ├── Tuan_04_Causal_Masking/  # Tuần 4: Causal Masking - Che tương lai để tự học
│   ├── Tuan_05_Self_Attention/  # Tuần 5: Self-Attention - Truy vấn, Khóa và Giá trị (Q, K, V)
│   ├── Tuan_06_MultiHead_MLP/   # Tuần 6: Multi-Head Attention & Lớp suy nghĩ độc lập (MLP)
│   ├── Tuan_07_Transformer_Block/ # Tuần 7: Ráp nối Transformer Block & Kiến trúc GPT
│   ├── Tuan_08_Training/        # Tuần 8: Quy trình huấn luyện & Tối ưu hóa AdamW trên GPU
│   ├── Tuan_09_Inference/       # Tuần 9: Sinh chữ & Tùy biến độ sáng tạo (Temperature)
│   └── Tuan_10_Project_Safety/  # Tuần 10: Showcase sản phẩm & Đạo đức sử dụng AI
├── 03_THUC_HANH_DU_AN/          # Hướng dẫn chạy code mini_gpt.py trên Google Colab
│   └── thuc_hanh_colab.md
├── 04_DANH_GIA/                 # Đề kiểm tra lý thuyết và Rubric chấm điểm dự án
│   └── rubric_va_de_thi.md
└── 05_TAI_NGUYEN/               # Danh sách liên kết bài giảng video và tài liệu chuyên sâu
    └── tai_nguyen.md
```
