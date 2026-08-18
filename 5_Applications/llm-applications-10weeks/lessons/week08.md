---
layout: course
title: "Week08"
permalink: /5_Applications/llm-applications-10weeks/lessons/week08.html
---

# Tuần 8 — AI Safety: harms, bias và mô hình đe dọa / Week 8 — AI Safety: harms, bias and threat modeling

[Mục lục khoá](../INDEX.md) · [Lịch](../schedule.md) · [Tuần 7 ←](week07.md) · [Tuần 9 →](week09.md)

## Mục tiêu học tập / Learning objectives

- Phân biệt AI Safety (an toàn cho xã hội) và Alignment (hành xử đúng ý người dùng). / Distinguish safety from alignment.
- Liệt kê các loại harm: bias, toxicity, misinformation, rò rỉ thông tin. / List harm categories.
- Tính và diễn giải metric bias/fairness cơ bản (demographic parity, counterfactual). / Compute basic fairness metrics.
- Lập một threat model: liệt kê tài sản, tác nhân đe dọa, và rủi ro = likelihood × impact. / Build a threat model.

## Công cụ / dữ liệu

- Python 3 chuẩn; dữ liệu giả về nhóm và dự đoán.
- Nguồn: [`../../../docs/19_ai_safety/index.md`](../../../docs/19_ai_safety/index.md) — `aero_llm_01_ai_safety_and_alignment.md`, `aero_llm_02_why_can_t_ai_just_be_safe_and_moral.md`; bias/fairness từ module 09 `aero_llm_14_assessing_bias_and_fairness.md`.

## Lý thuyết + ví dụ / Theory + examples

**Safety** hỏi "hệ thống có gây hại cho xã hội không"; **Alignment** hỏi "hệ thống có làm đúng điều người dùng muốn không". Một AI có thể aligned với kẻ tấn công (đưa code mã hoá ổ cứng) nhưng unsafe với xã hội. / An AI can be aligned with an attacker yet unsafe.

Bias đo bằng chênh lệch dự đoán giữa các nhóm nhạy cảm $A$:

- **Demographic parity**: $|\Pr(\hat Y=1\mid A=0)-\Pr(\hat Y=1\mid A=1)|$ càng nhỏ càng ít lệch.
- **Counterfactual**: cùng một câu, chỉ đổi thuộc tính nhạy cảm ("he"/"she"), so sánh đầu ra.

Lưu ý: các định nghĩa fairness có thể **mâu thuẫn nhau** (không thể thoả tất cả đồng thời). / Fairness definitions can conflict.

Threat model đơn giản: liệt kê **tài sản** (dữ liệu, mô hình, người dùng), **tác nhân** (người dùng thường, kẻ tấn công, lỗi hệ thống), rồi chấm từng rủi ro:

$$\mathrm{Risk}=\mathrm{Likelihood}\times\mathrm{Impact}.$$

## Lab từng bước / Step-by-step lab

1. Tạo dữ liệu giả: 200 mẫu dự đoán nhị phân chia hai nhóm; tính demographic parity.
2. Cài counterfactual evaluation: so sánh đầu ra của cặp prompt chỉ khác thuộc tính nhạy cảm.
3. Lập threat model cho một ứng dụng RAG nội bộ: ≥5 tài sản, ≥3 tác nhân, chấm likelihood/impact.
4. Xếp hạng rủi ro và đề xuất một biện pháp giảm thiểu cho rủi ro cao nhất.

## Liên kết code / Code links

- [`../code/week08/01_bias_metrics.py`](../code/week08/01_bias_metrics.py) — demographic parity + counterfactual.
- [`../code/week08/02_threat_model.py`](../code/week08/02_threat_model.py) — risk = likelihood × impact.

## Câu hỏi thảo luận / Discussion questions

1. Một hệ thống "aligned" có thể vẫn unsafe không? Cho ví dụ. / Can an aligned system still be unsafe?
2. Vì sao không tồn tại một định nghĩa fairness duy nhất đúng? / Why is there no single correct fairness definition?
3. Bias đo được là do dữ liệu, do mô hình, hay do cách đo? / Is measured bias from data, model, or measurement?
4. Threat model nên cập nhật khi nào? / When should a threat model be updated?

## Bài tập / Homework

- **Cơ bản**: Tính demographic parity cho dữ liệu giả; giải thích giá trị.
- **Nâng cao**: Viết counterfactual eval cho 5 cặp prompt; chỉ ra cặp nào lệch nhất.
- **Thử thách**: Lập threat model đầy đủ (tài sản × tác nhân × rủi ro) và xếp hạng; đề xuất giảm thiểu.

## Yêu cầu nộp / Submission

- 1 file bias metric + 1 threat model (bảng) + nhận xét giới hạn của metric.
- Chỉ dùng dữ liệu giả; không chạy trên người dùng thật.

## Rubric (100 điểm)

| Tiêu chí | Điểm |
|---|---:|
| Đúng chức năng: công thức fairness đúng, threat model đầy đủ | 35 |
| An toàn & xử lý lỗi: xử lý nhóm thiếu dữ liệu, không phơi dữ liệu nhạy cảm | 25 |
| Chất lượng code/tài liệu: bảng rủi ro rõ, chú thích đúng chỗ | 20 |
| Phân tích & bằng chứng: giải thích metric, xếp hạng rủi ro có lý | 20 |

## ⚠️ Lưu ý an toàn / Safety notes

- Đo bias trên dữ liệu giả chỉ để học; kết luận về nhóm người thật cần dữ liệu đại diện và đạo đức nghiên cứu.
- Không dùng thuộc tính nhạy cảm thật của cá nhân khi chưa được phép.
- Threat model là tài liệu sống; cập nhật khi hệ thống, dữ liệu hoặc tác nhân thay đổi.
