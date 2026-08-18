---
layout: course
title: "Week03"
permalink: /4_Training/ai-thuc-chien-10weeks/lessons/week03.html
---

# Tuần 3: Lọc dữ liệu & Pha trộn (Data Mix Optimization)

Có được dữ liệu tổng hợp chưa đủ, ta cần lọc bỏ rác và tối ưu hóa tỷ lệ pha trộn giữa các miền dữ liệu khác nhau.

## Các bước xử lý dữ liệu thô
- **Lọc trùng lặp (Deduplication):** Sử dụng thuật toán MinHash LSH hoặc so khớp nhúng vector để loại bỏ các prompt giống nhau.
- **Lọc an toàn (Toxicity Filtering):** Loại bỏ các mẫu phản hồi chứa từ ngữ thô tục, bạo lực bằng mô hình phân loại nhỏ.
- **Pha trộn dữ liệu (Data Mix):** Tỷ lệ pha trộn tối ưu giữa code, toán học, đối thoại và tài liệu web chung (ví dụ: 30% code, 20% toán, 50% văn bản chung).
