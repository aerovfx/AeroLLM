---
layout: course
title: "Week06"
permalink: /4_Training/ai-thuc-chien-10weeks/lessons/week06.html
---

# Tuần 6: Tiền Huấn luyện Bổ sung (Continued Pre-training)

Khi bạn muốn nhồi nhét một lượng lớn tri thức miền mới (ví dụ luật pháp Việt Nam, y học cổ truyền) vào mô hình cơ sở trước khi làm SFT.

## Kỹ thuật thực hiện
- Huấn luyện tự hồi quy (Next-token prediction) trên lượng lớn văn bản thô chưa gắn nhãn.
- Cần đặt tốc độ học thấp hơn tiền huấn luyện gốc (khoảng `1e-5` đến `5e-5`).
- Sử dụng hàm suy giảm tốc độ học dạng Cosine (Cosine learning rate scheduler).
