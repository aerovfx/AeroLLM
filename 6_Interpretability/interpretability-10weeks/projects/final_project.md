---
layout: course
title: "Final Project"
permalink: /6_Interpretability/interpretability-10weeks/projects/final_project.html
---

# Capstone — Nghiên cứu can thiệp cơ chế (Mechanistic Intervention Study)

## Bài toán

Chọn **một** câu hỏi diễn giải cơ chế cụ thể trên một mô hình nhỏ (mô hình giả tự xây bằng NumPy, hoặc mô hình nhỏ được cấp phép), rồi trả lời nó bằng đầy đủ quy trình quan sát → can thiệp → bằng chứng → giới hạn. Ví dụ câu hỏi hợp lệ:

- "Mạch nào quyết định quan hệ chủ ngữ–tân ngữ trong câu IOI giả?"
- "Neuron/hướng nào mang thông tin về một khái niệm nhị phân (đúng/sai ngữ pháp)?"
- "Head attention nào chuyển thông tin giữa hai token trong một câu tri thức giả?"

## Phạm vi

- **Trong phạm vi**: mô hình giả hoặc mô hình nhỏ bạn tự kiểm soát, dữ liệu giả local, can thiệp có thể rollback.
- **Ngoài phạm vi**: mô hình thật đang phục vụ người dùng, dữ liệu có thông tin cá nhân, can thiệp không thể hoàn tác.

## Yêu cầu chức năng

1. **Giả thuyết**: phát biểu rõ "thành phần X gây ra hành vi Y", kèm lý do dựa trên quan sát.
2. **Quan sát**: ít nhất một phép probing/giảm chiều/selectivity (tuần 1–5) để định vị ứng viên.
3. **Can thiệp**: ít nhất một phép ablation/patching/editing (tuần 6–9) với baseline sạch và quét cường độ.
4. **Metric**: dùng logit difference hoặc một metric liên tục tương đương, không chỉ đúng/sai.

## Yêu cầu phi chức năng

- Tái lập được: seed, cấu trúc mô hình, dữ liệu, lệnh chạy.
- An toàn: chỉ local, có ghi chú phạm vi và rollback.
- Trình bày song ngữ (Việt chính, thuật ngữ Anh trong ngoặc).

## Milestone

| Tuần | Mốc |
|---:|---|
| 1–2 | Chọn câu hỏi, dựng mô hình giả, model card quan sát |
| 3–5 | Phép quan sát: probing/selectivity/laminar profile |
| 6–8 | Phép can thiệp: ablation/patching trên ứng viên |
| 9 | Tổng hợp, vẽ bản đồ mạch phỏng đoán |
| 10 | Viết báo cáo, demo, peer review, safety retrospective |

## Deliverables

- `README.md` tái lập được (lệnh chạy + seed + cấu trúc).
- 2–4 script `.py` (quan sát + can thiệp) có chú thích Việt.
- Báo cáo 3–5 trang: giả thuyết, phương pháp, kết quả, giới hạn.
- Bản đồ mạch phỏng đoán (sơ đồ/screenshot) kèm bằng chứng số.

## Demo script (gợi ý)

1. Chạy quan sát, chỉ ra "ứng viên" (neuron/head/hướng).
2. Chạy baseline sạch → logit difference gốc.
3. Chạy can thiệp → logit difference mới, quét cường độ.
4. Kết luận ủng hộ/bác bỏ giả thuyết, nêu giới hạn.

## Threat model / Risk assessment

- **Nguy cơ overinterpretation**: tương quan bị đọc thành nhân quả → giảm thiểu bằng can thiệp + baseline + quét scale.
- **Nguy cơ compensation**: mạng tự bù khiến can thiệp "im lặng" → giảm thiểu bằng đo liên tục và nhiều vị trí.
- **Nguy cơ thiếu ground truth**: không có đáp án chuẩn → giảm thiểu bằng cấy đặc trưng đã biết vào mô hình giả.
- **Nguy cơ rò rỉ dữ liệu**: dùng dữ liệu có thông tin cá nhân → cấm, chỉ dùng dữ liệu giả.

## Rubric (100 điểm)

| Tiêu chí | Điểm |
|---|---:|
| Đúng chức năng & tái lập: chạy được, metric đúng, seed rõ | 35 |
| Chất lượng can thiệp: baseline sạch, quét cường độ, nhiều vị trí | 20 |
| Phân tích & bằng chứng: lập luận chặt, đối chiếu quan sát–can thiệp | 20 |
| An toàn & trình bày: phạm vi rõ, threat model, song ngữ | 25 |

## Tiêu chí thất bại bắt buộc (tự đánh giá trước khi nộp)

- Không có baseline sạch để so sánh → **không đạt**.
- Kết luận nhân quả chỉ từ một lần chạy, không quét cường độ → **không đạt**.
- Không ghi rõ giới hạn (variance ≠ relevance, compensation, ground truth) → **không đạt**.
- Can thiệp vào mô hình/dữ liệu thật ngoài phạm vi → **đình chỉ đánh giá**.
