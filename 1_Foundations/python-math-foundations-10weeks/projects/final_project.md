---
layout: course
title: "Final Project"
permalink: /1_Foundations/python-math-foundations-10weeks/projects/final_project.html
---

# Đồ án cuối khoá — Capstone mini: mạng nơ-ron nhỏ / Final project — Mini capstone: a small neural network

[← Tổng quan](../INDEX.md) · [Lịch học](../schedule.md)

## Bài toán / Brief

Xây một mạng nơ-ron nhỏ (một tầng ẩn là đủ) bằng PyTorch, huấn luyện trên dữ liệu giả do bạn sinh ra, giải thích forward/backward và báo cáo quá trình hội tụ. Không chấm theo độ lớn của mô hình; chấm theo tính đúng, khả năng tái lập và chất lượng phân tích.

## Phạm vi / Scope

- **Trong phạm vi:** Dữ liệu giả (hồi quy hoặc phân loại nhị phân), một tầng ẩn ReLU, CPU, PyTorch, đồ thị loss.
- **Ngoài phạm vi:** Dữ liệu thật/có bản quyền, huấn luyện phân tán, triển khai production, mô hình lớn.

## Yêu cầu chức năng / Functional requirements

1. Sinh dữ liệu giả có seed, tách train/validation.
2. Định nghĩa model (perceptron/tầng ẩn) với forward pass.
3. Tính loss (MSE hoặc cross-entropy) và chạy backward pass bằng autograd.
4. Cập nhật tham số bằng gradient descent, ghi lại loss theo epoch.
5. Vẽ đồ thị loss và báo cáo tham số hội tụ.

## Yêu cầu phi chức năng / Non-functional requirements

- Chạy tái lập được (seed cố định), thời gian huấn luyện dưới vài phút trên CPU.
- Không chứa secret/token; không tải dữ liệu bên ngoài.
- Code có docstring và chú thích khối; README có lệnh chạy.

## Milestones

| Tuần | Mốc |
|---:|---|
| 8 | Sinh dữ liệu giả, tính softmax/loss bằng NumPy |
| 9 | Cài đặt GD 1D/2D để hiểu bước cập nhật |
| 10 | Lắp model PyTorch, forward/backward, vẽ loss và nộp |

## Deliverables

- `README.md` tái lập được (lệnh chạy + seed).
- Script huấn luyện + đồ thị loss.
- Một đoạn phân tích forward/backward và giải thích hội tụ.

## Demo script

1. Chạy script sinh dữ liệu và in 5 mẫu đầu.
2. Chạy huấn luyện, in loss mỗi N epoch.
3. In tham số hội tụ và hiển thị đồ thị loss.
4. Trả lời câu hỏi: vì sao model học được quan hệ trong dữ liệu?

## Threat model / Risk assessment

| Rủi ro | Hậu quả | Giảm thiểu |
|---|---|---|
| Learning rate quá lớn | Phân kỳ, loss NaN | Giới hạn epoch, kiểm tra hữu hạn, dừng sớm |
| Dữ liệu rò rỉ train/val | Đánh giá lạc quan sai | Sinh seed riêng, tách trước khi train |
| Thiếu tái lập | Không chứng minh được kết quả | Ghi seed và phiên bản thư viện |
| Dữ liệu nhạy cảm | Rò rỉ thông tin | Chỉ dùng dữ liệu giả |

## Rubric 100 điểm / 100-point rubric

| Hạng mục | Điểm |
|---|---:|
| Đúng chức năng & tái lập được | 35 |
| Xử lý lỗi/an toàn (zero-grad, kiểm tra NaN, không secret) | 25 |
| Chất lượng code/tài liệu | 20 |
| Phân tích forward/backward và bằng chứng hội tụ | 20 |

## Tiêu chí thất bại bắt buộc / Mandatory failure criteria

Đồ án bị coi là không đạt nếu: script không chạy được; loss không giảm sau khi đã chọn learning rate hợp lý; chứa secret/token hoặc dữ liệu thật không được phép; không cung cấp seed nên không tái lập được kết quả.
