---
layout: course
title: "Week04"
permalink: /4_Training/ai-thuc-chien-10weeks/lessons/week04.html
---

# Tuần 4: Lựa chọn Mô hình & Tokenizer

Việc lựa chọn kiến trúc mô hình nền tảng (Base model) và cấu hình Tokenizer ảnh hưởng lớn đến chi phí huấn luyện.

## Lựa chọn Base Model
- **Dòng SmolLM2 (135M, 360M, 1.7B):** Lý tưởng cho các thử nghiệm ablation nhanh và các đội có ít GPU.
- **Dòng Llama-3 / Qwen-2.5 (1B, 3B, 7B):** Cấu hình tiêu chuẩn cho kết quả chất lượng cao trên các bảng xếp hạng (benchmarks).

## Cấu hình Tokenizer
- Sử dụng bảng từ vựng (Vocabulary size) lớn (ví dụ 100k token) để mã hóa tiếng Việt tiết kiệm dung lượng ngữ cảnh.
- Tránh tình trạng Tokenizer bị phân mảnh ký tự UTF-8.
