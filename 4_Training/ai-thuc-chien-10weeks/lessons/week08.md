---
layout: course
title: "Week08"
permalink: /4_Training/ai-thuc-chien-10weeks/lessons/week08.html
---

# Tuần 8: Tối ưu Sở thích (DPO/ORPO)

Căn chỉnh hành vi để mô hình trả lời lịch sự, hữu ích và tránh độc hại mà không cần huấn luyện mô hình phần thưởng phức tạp.

## Kỹ thuật DPO (Direct Preference Optimization)
- Sử dụng cặp dữ liệu phản hồi ưa thích (Chosen) và phản hồi bị từ chối (Rejected).
- Trực tiếp tối ưu hóa xác suất của mô hình SFT để tăng xác suất chọn câu Chosen và giảm xác suất chọn câu Rejected.

## Kỹ thuật ORPO (Odds Ratio Preference Optimization)
- Gộp pha SFT và pha DPO thành một lượt huấn luyện duy nhất, giúp tối ưu hóa bộ nhớ và tăng tốc độ hội tụ mô hình.
