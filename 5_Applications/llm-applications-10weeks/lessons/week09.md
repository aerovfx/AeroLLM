---
layout: course
title: "Week09"
permalink: /5_Applications/llm-applications-10weeks/lessons/week09.html
---

# Tuần 9 — Red teaming, guardrails và can thiệp an toàn / Week 9 — Red teaming, guardrails and safety interventions

[Mục lục khoá](../INDEX.md) · [Lịch](../schedule.md) · [Tuần 8 ←](week08.md) · [Tuần 10 →](week10.md)

## Mục tiêu học tập / Learning objectives

- Phân biệt red teaming với đánh giá hộp đen thông thường. / Distinguish red teaming from ordinary black-box evals.
- Nhận diện các kỹ thuật tấn công: jailbreak, prompt injection, ignore-instructions. / Identify jailbreak and prompt-injection techniques.
- Cài guardrail đầu vào (filter, deny) và đầu ra (chặn nội dung cấm). / Implement input and output guardrails.
- Viết bộ mẫu tấn công giả định và đo tỷ lệ bị chặn. / Write adversarial probes and measure block rate.

## Công cụ / dữ liệu

- Python 3 chuẩn; mẫu prompt giả định (không nhắm hệ thống thật).
- Nguồn: [`../../../docs/09_quantitative_evaluations/aero_llm_017_red_teaming.md`](../../../docs/09_quantitative_evaluations/aero_llm_017_red_teaming.md) và [`../../../docs/19_ai_safety/aero_llm_05_hands_on_hack_an_ai_to_steal_a_password_.md`](../../../docs/19_ai_safety/aero_llm_05_hands_on_hack_an_ai_to_steal_a_password_.md).

## Lý thuyết + ví dụ / Theory + examples

Red teaming là đánh giá đối kháng **có hệ thống** nhằm tìm lỗ hổng, khác black-box eval ngẫu nhiên ở tính mục tiêu và phương pháp. / Red teaming is systematic and adversarial, not serendipitous.

Các kỹ thuật phổ biến:

1. **Jailbreak**: đổi ngữ cảnh (đóng vai, dịch, mã hoá) để lách từ chối. / Role-play, translation, encoding.
2. **Prompt injection**: nhúng chỉ thị độc hại vào dữ liệu mà mô hình xử lý (ví dụ: "bỏ qua chỉ thị trên..."). / Injecting instructions via data.
3. **Ignore previous instructions**: ghi đè chỉ thị gốc trong cửa sổ ngữ cảnh.

Guardrail là lớp phòng thủ ngoài mô hình: filter đầu vào (denylist, phát hiện injection) và đầu ra (chặn nội dung cấm, kiểm tra groundedness). Guardrail không thể bắt mọi thứ, nhưng giảm rủi ro $P(\text{lỗ hổng})$. / Guardrails reduce, not eliminate, risk.

## Lab từng bước / Step-by-step lab

1. Viết danh sách 10 prompt giả định: 5 vô hại, 5 tấn công (jailbreak/injection).
2. Cài guardrail đầu vào: denylist từ khoá + heuristic phát hiện "bỏ qua chỉ thị".
3. Cài guardrail đầu ra: chặn câu trả lời chứa nội dung cấm hoặc thiếu nguồn.
4. Đo tỷ lệ chặn đúng (block rate) và false positive (chặn nhầm câu vô hại).

## Liên kết code / Code links

- [`../code/week09/01_guardrails.py`](../code/week09/01_guardrails.py) — input/output filter + phát hiện injection.
- [`../code/week09/02_red_team.py`](../code/week09/02_red_team.py) — bộ mẫu tấn công giả định + đo block rate.

## Câu hỏi thảo luận / Discussion questions

1. Vì sao guardrail ngoài mô hình vẫn cần dù mô hình đã được huấn luyện từ chối? / Why are external guardrails still needed?
2. False positive (chặn nhầm câu vô hại) gây hại gì? / What is the cost of false positives?
3. Red teaming nên làm trước hay sau khi phát hành? / Should red teaming happen before or after release?
4. Làm sao biết một guardrail "đủ tốt"? / How do you know a guardrail is good enough?

## Bài tập / Homework

- **Cơ bản**: Cài guardrail denylist đơn giản; chạy trên 10 prompt và in kết quả chặn.
- **Nâng cao**: Thêm phát hiện prompt injection heuristic; đo block rate và false positive.
- **Thử thách**: Viết 10 mẫu tấn công đa dạng (dịch, đóng vai, mã hoá) và đề xuất cải tiến guardrail để chặn chúng.

## Yêu cầu nộp / Submission

- 1 file guardrail + 1 file red team + bảng kết quả (block rate, false positive).
- Chỉ dùng mẫu giả định; không tấn công hệ thống thật.

## Rubric (100 điểm)

| Tiêu chí | Điểm |
|---|---:|
| Đúng chức năng: guardrail chặn đúng, bộ mẫu đa dạng, đo lường hợp lệ | 35 |
| An toàn & xử lý lỗi: không phơi payload thật, xử lý input rỗng, không gọi mạng | 25 |
| Chất lượng code/tài liệu: tách filter rõ, chú thích đúng chỗ | 20 |
| Phân tích & bằng chứng: block rate, false positive, đề xuất cải tiến | 20 |

## ⚠️ Lưu ý an toàn / Safety notes

- Chỉ red team trên hệ thống bạn sở hữu hoặc được ủy quyền bằng văn bản; không tấn công dịch vụ của bên thứ ba.
- Không lưu/đăng tải payload tấn công thật nhằm vào hệ thống đang vận hành.
- Guardrail là một lớp trong phòng thủ nhiều lớp (defense in depth), không phải lá chắn tuyệt đối.
