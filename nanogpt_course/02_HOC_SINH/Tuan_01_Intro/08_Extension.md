# Tuần 1: Giới thiệu AI & Mô hình ngôn ngữ lớn (LLM) — Extension Material
> **Chủ đề mở rộng:** Phân loại kiến trúc Transformer: Encoder-only, Decoder-only và Encoder-Decoder.

---

Trong khi mô hình **nanoGPT** (và dòng GPT của OpenAI) sử dụng kiến trúc **Decoder-only** chuyên phục vụ việc tạo sinh văn bản tự hồi quy, các mô hình Transformer khác lại sử dụng các cấu hình khác tùy thuộc vào mục đích sử dụng:

1.  **Encoder-only (Chỉ bộ mã hóa - ví dụ BERT):**
    *   *Nguyên lý:* Nhìn thấy toàn bộ văn bản cùng một lúc (không dùng Causal Mask để che tương lai).
    *   *Ứng dụng:* Phân tích cảm xúc (vui/buồn), tìm kiếm thông tin, phân loại câu, đặt câu hỏi.
2.  **Decoder-only (Chỉ bộ giải mã - ví dụ GPT, LLaMA, Gemini):**
    *   *Nguyên lý:* Chỉ nhìn về quá khứ để đoán tương lai (sử dụng Causal Mask).
    *   *Ứng dụng:* Tạo văn bản, chatbot hội thoại tự do, lập trình code.
3.  **Encoder-Decoder (Cả hai bộ - ví dụ T5, BART):**
    *   *Nguyên lý:* Bộ Encoder đọc hiểu ngữ nghĩa câu đầu vào (ví dụ tiếng Anh), bộ Decoder nhận kết quả mã hóa đó để giải mã sang câu đầu ra (ví dụ dịch sang tiếng Việt).
    *   *Ứng dụng:* Dịch thuật máy, tóm tắt văn bản.
