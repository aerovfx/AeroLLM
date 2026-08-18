---
layout: course
title: "Model Finalization And Submission"
permalink: /4_Training/ai-thuc-chien-10weeks/references/round-3/model-training-guideline/model-finalization-and-submission.html
---

# Giai Đoạn IV: Hoàn Thiện & Nộp Mô Hình

Một "mô hình" không chỉ là các trọng số của nó. Bài nộp cuối cùng của bạn phải là một gói hoàn chỉnh.

## Đóng gói Mô hình của bạn

Lưu tất cả các tệp cần thiết:

- Trọng số mô hình (ví dụ: `model.safetensors`)
- Các tệp Tokenizer (ví dụ: `tokenizer.json`)
- Các tệp cấu hình (ví dụ: `config.json`)

## Tạo một Thẻ Mô hình (Model Card)

Điều này là cần thiết. Tệp `README.md` của bạn phải là một thẻ mô hình chi tiết bao gồm:

- **Mô tả Mô hình:** Nó là gì? Các tính năng chính của nó là gì?
- **Dữ liệu Huấn luyện:** Bạn đã sử dụng hỗn hợp dữ liệu nào cho tiền huấn luyện và SFT?
- **Quy trình Huấn luyện:** Chi tiết cấp cao về quá trình huấn luyện của bạn (siêu tham số, chiến lược song song hóa).
- **Đánh giá:** Bạn đã đánh giá mô hình của mình như thế nào? Điểm số của nó là gì?
- **Hạn chế & Thiên kiến (Bias):** Mô hình của bạn không thể làm gì? Nó thất bại ở đâu?

## Nộp Mô hình của bạn

Tải lên kho lưu trữ mô hình hoàn chỉnh của bạn lên nền tảng cuộc thi (Hugging Face Hub).
