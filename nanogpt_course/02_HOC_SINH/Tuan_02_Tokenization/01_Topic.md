# Tuần 2: Tokenization — Topic Overview
> **Mục tiêu học tập:** Hiểu rõ cách Tokenizer cắt nhỏ văn bản và mã hóa thành các số nguyên (Token IDs); phân biệt được char-level tokenization và Byte Pair Encoding (BPE).

---

```mermaid
mindmap
  root((Tuần 2: Tokenization))
    Mã hóa văn bản
      Ký tự sang Số nguyên
      Bộ từ điển Vocabulary
      Hàm Encode & Decode
    Các cấp độ cắt chữ
      Char-level
        Ký tự đơn lẻ
        Từ vựng siêu nhỏ
        Dễ học, dễ viết
      Word-level
        Cắt theo từ đơn
        Từ vựng khổng lồ
        Không xử lý được từ lạ
      Subword-level
        Ghép cụm ký tự phổ biến
        Dùng thuật toán BPE
        Chuẩn của ChatGPT/Gemini
    Giới hạn kỹ thuật
      Lỗi đếm chữ cái
      Không hiểu trực quan
      Hiệu suất đa ngôn ngữ
```
