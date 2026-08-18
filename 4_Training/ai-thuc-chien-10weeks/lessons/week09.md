---
layout: course
title: "Week09"
permalink: /4_Training/ai-thuc-chien-10weeks/lessons/week09.html
---

# Tuần 9: Đánh giá & Tránh Nhiễm dữ liệu (Evaluation & Contamination)

Làm sao biết mô hình của bạn đã cải tiến chất lượng và câu trả lời đáng tin cậy?

## Các công cụ đánh giá tự động
- **lm-evaluation-harness:** Bộ công cụ mã nguồn mở đánh giá mô hình trên hàng chục benchmark học thuật (MMLU, GSM8K, ARC).
- **LLM-as-a-judge:** Sử dụng mô hình lớn mạnh (như GPT-4, Gemini Pro) để chấm điểm câu trả lời của mô hình bạn dựa trên Rubric quy định.

## Phòng tránh nhiễm dữ liệu (Contamination)
- Quét dữ liệu train của bạn để đảm bảo không chứa các câu hỏi thi hoặc đáp án của tập test.
- Nếu bị phát hiện nhiễm dữ liệu, điểm số bài thi của bạn sẽ bị hủy bỏ.
