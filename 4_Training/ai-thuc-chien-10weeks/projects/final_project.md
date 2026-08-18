---
layout: course
title: "Final Project"
permalink: /4_Training/ai-thuc-chien-10weeks/projects/final_project.html
---

# Capstone — Đóng gói và nộp mô hình

## Bài toán

Huấn luyện hoặc fine-tune một mô hình ngôn ngữ cho một nhiệm vụ cụ thể, rồi đóng gói thành sản phẩm có thể nộp/đánh giá độc lập.

## Yêu cầu

1. **Dữ liệu**: mô tả nguồn, giấy phép, quy trình lọc và thống kê tập train/eval.
2. **Huấn luyện**: ghi rõ base model, chiến lược (CPT/SFT/preference), hyperparameters và tài nguyên (GPU, thời gian).
3. **Đánh giá**: bộ benchmark, kết quả định lượng, phân tích lỗi.
4. **Đóng gói**: checkpoint/GGUF, script inference, model card.
5. **An toàn**: giới hạn của mô hình, rủi ro đã biết và cách giảm thiểu.

## Deliverables

- README tái lập được (lệnh chạy + seed).
- Notebook/script huấn luyện và đánh giá.
- Model card + kết quả đối sánh baseline.

## Rubric (100 điểm)

- Đúng chức năng & tái lập được: 35
- Chất lượng dữ liệu & ghi nhận nguồn: 20
- Đánh giá định lượng & phân tích lỗi: 20
- Đóng gói, model card & an toàn: 25
