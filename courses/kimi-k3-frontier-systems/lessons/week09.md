# Tuần 9 — QAT, serving và benchmark audit

[← Tuần 8](week08.md) · [Mục lục khoá](../INDEX.md) · [40 tuần](../../WEEK_INDEX.md) · [Lịch 20 buổi](../schedule.md) · [Tuần 10 →](week10.md)

## Mục tiêu / Objectives

- Giải thích deployment-aware QAT và speculative draft. / Explain QAT and drafting.
- Đọc benchmark theo harness, effort, tools và sampling. / Audit evaluation setup.
- Chọn API, small-model simulation hoặc cluster deployment. / Make a deployment decision.

## Lý thuyết / Theory

K3 report quantize routed expert weights MXFP4 và expert input activations MXFP8 từ SFT qua RL; non-expert modules ở precision cao hơn. Cùng quantization cho rollout/training giảm mismatch. MTP layer được fine-tune thành EAGLE-3-style draft; objective nhắm acceptance rate trực tiếp. Serving còn phụ thuộc hybrid KDA/MLA cache và engine support.

Benchmark K3 chủ yếu dùng effort max, temperature 1.0; một số task dùng tool augmentation, một số model chạy harness khác hoặc có fallback/cyberguard. Do đó score table là comparison có điều kiện, không phải pure model ablation.

## Buổi 1 / Session 1 — Deployment decision

Ước lượng weight lower bound, cache, concurrency và data sensitivity. Audit `trust_remote_code`, pin revision và license theo [repository guide](../REPOSITORY_GUIDE.md). Chọn: CPU toy, small open model, managed API hoặc cluster. Ghi rõ lý do loại các phương án còn lại.

## Buổi 2 / Session 2 — Evaluation card

Chạy `preserved_history_payload.py`, kiểm tra đủ `reasoning_content`, `content`, `tool_calls` nhưng không log reasoning. Sau đó audit sáu benchmarks: task/version, sample count, metric, harness, tools, effort, temperature/top-p, runs, judge, refusal/fallback và source date.

## Câu hỏi thảo luận / Discussion questions

1. QAT từ SFT mang lợi ích gì so post-hoc quantization? / Why start QAT early?
2. Activated weights và KV cache scale khác nhau thế nào? / How do weight and cache scaling differ?
3. Draft accuracy liên hệ acceptance rate ra sao? / How does draft quality affect acceptance?
4. Harness là confounder hay product component? / Is a harness a confounder or product component?
5. Tool-augmented score nên báo cáo thế nào? / How should tool scores be reported?

## Bài tập / Homework

Nộp deployment decision record, source/license/security manifest, preserved-history test và evaluation card có ít nhất ba limitation quan trọng. / Submit deployment, security, history, and benchmark audit artifacts.

## Rubric

| Technical accuracy | Evaluation controls | Feasibility | Limitations | Decision clarity |
|---:|---:|---:|---:|---:|
| 25 | 25 | 20 | 20 | 10 |

## ⚠️ Ngộ nhận / Misconceptions

- 4-bit nghĩa toàn model dùng 4-bit mọi nơi. / K3 uses mixed precision roles.
- Speculative decoding được phép đổi output distribution. / Lossless sampling should preserve it.
- Score khác nhau luôn do model weights. / Harness, tools, budgets and judges matter.
