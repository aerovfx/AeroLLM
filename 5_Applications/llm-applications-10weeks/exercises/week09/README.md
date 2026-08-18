---
layout: course
title: "Readme"
permalink: /5_Applications/llm-applications-10weeks/exercises/week09/README.html
---

# Bài tập tuần 09 — Red teaming & guardrails

Liên kết: [Bài học](../../lessons/week09.md) · [Code](../../code/week09/)

## Mức 1 — Cơ bản

Cài guardrail denylist đơn giản; chạy trên 10 prompt (5 vô hại, 5 tấn công) và in kết quả chặn/cho phép kèm lý do.

## Mức 2 — Nâng cao

Thêm phát hiện prompt injection heuristic (ví dụ: "ignore previous instructions"). Đo block rate và false positive rate trên bộ mẫu; giải thích đánh đổi giữa hai con số.

## Mức 3 — Thử thách

Viết 10 mẫu tấn công đa dạng (đóng vai, dịch, mã hoá, liệt kê một phần) và đề xuất ít nhất một cải tiến guardrail để chặn chúng. Ghi rõ mẫu nào guardrail hiện tại bỏ sót.

## Rubric (100 điểm)

| Tiêu chí | Điểm |
|---|---:|
| Đúng chức năng: guardrail chặn đúng, bộ mẫu đa dạng, đo lường hợp lệ | 35 |
| An toàn & xử lý lỗi: không phơi payload thật, xử lý input rỗng, không gọi mạng | 25 |
| Chất lượng code/tài liệu: tách filter rõ, chú thích đúng chỗ | 20 |
| Phân tích & bằng chứng: block rate, false positive, đề xuất cải tiến | 20 |
