---
layout: course
title: "Week10"
permalink: /2_LLM_Core/llm-from-scratch-10weeks/lessons/week10.html
---

# Tuần 10 — Capstone, an toàn và demo / Capstone, safety, and demo

[← Tuần 9](week09.md) · [Mục lục khoá](../INDEX.md) · [40 tuần](../../../courses/WEEK_INDEX.md) · [Lịch 20 buổi](../schedule.md)

## Mục tiêu học tập / Learning objectives

- Tích hợp pipeline data→train→evaluate→serve / integrate data, training, evaluation, and serving.
- Viết model card trung thực về giới hạn / write an honest model card.
- Thực hiện threat model và red-team phù hợp / conduct scoped threat modeling and red teaming.
- Trình diễn có số liệu và kế hoạch tái lập / demo with evidence and reproducibility.

## Lý thuyết sâu / Deep theory

Capstone không chỉ là “model chạy được”. Một artifact khoa học cần provenance dữ liệu, config bất biến, checkpoint có hash, evaluation tách biệt và claims giới hạn bởi bằng chứng. Risk có thể ưu tiên bằng $R=P(\text{harm})\times I(\text{harm})\times E(\text{exposure})$; đây là công cụ xếp hạng, không phải xác suất tuyệt đối.

Safety layers gồm dữ liệu, objective, evaluation, giao diện, policy, monitoring và incident response. Model nhỏ vẫn có thể ghi nhớ PII hoặc sinh nội dung độc hại; “chỉ dùng học tập” không thay thế kiểm soát.

## Buổi 1 — Capstone integration và safety review / Session 1 — Integration and safety review

### Definition of done / Định nghĩa hoàn thành

- Lệnh duy nhất tái tạo preprocessing và training smoke run.
- Checkpoint, tokenizer, config và hashes tương thích.
- Baseline + final được đánh giá cùng splits và token budget.
- Model card nêu intended use, out-of-scope use, dữ liệu, metrics, limitations.
- Threat model có assets, actors, attack surfaces, mitigations và residual risks.

```yaml
model:
  architecture: decoder-only-transformer  # Kiến trúc cần để code inference chọn đúng loader.
  checkpoint_sha256: "record-the-real-hash"  # Hash thật để kiểm tra artifact không bị đổi.
data:
  split_strategy: document-level  # Tách theo document để giảm rò rỉ đoạn gần trùng.
evaluation:
  primary_metric: validation_nll  # Metric chính dùng chọn/so sánh checkpoint.
  # Hai test set riêng cho memorization và hành vi trước yêu cầu nguy hại.
  safety_sets: [memorization_probe, harmful_request_probe]
```

### Hands-on safety lab / Lab an toàn

1. Chọn 5 nhóm rủi ro: memorization, toxic continuation, prompt misuse, bias, denial-of-service.
2. Viết tối thiểu 5 probes mỗi nhóm, không dùng dữ liệu cá nhân thật.
3. Ghi pass/fail criteria trước khi chạy.
4. Đề xuất mitigation ở model và application layer; retest sau thay đổi.

## Buổi 2 — Demo và phản biện / Session 2 — Demo and defense

Demo 12 phút: 2 phút problem/data, 3 phút architecture/training, 3 phút quantitative results, 2 phút live generation/failure, 2 phút safety/limitations. Luôn có prerecorded/text fallback. Không cherry-pick: dùng prompt list đóng băng và seed công bố.

### Checklist thực hành / Practical checklist

- Chạy clean-environment smoke test từ README.
- Benchmark trên phần cứng được ghi rõ; báo median và p95.
- Kiểm thử empty prompt, maximum context, Unicode và EOS.
- Tạo release bundle chỉ chứa file cần thiết, không secrets/log cá nhân.
- Peer-review chéo model card và reproduction instructions.

## Chính xác 5 câu hỏi thảo luận / Exactly 5 discussion questions

1. Claim nào được metric capstone hỗ trợ và claim nào chưa? / Which claims are and are not supported by the metrics?
2. Threat model thay đổi thế nào giữa local demo và public API? / How does threat modeling change for a public API?
3. Khi nào nên dừng release dù validation loss tốt? / When should release stop despite good validation loss?
4. Một live demo công bằng cần kiểm soát seed và prompts ra sao? / How should a fair demo control seeds and prompts?
5. Model card nên mô tả failure cases ở mức nào để hữu ích? / How detailed should model-card failures be?

## Bài tập cuối khoá / Final assignment

Nộp repository tái lập, tokenizer, checkpoint nhỏ, training/eval logs, 30-prompt evaluation set, system benchmark, model card, safety report và video demo ≤12 phút. So sánh baseline với final bằng cùng compute budget; đưa ít nhất 3 kết quả âm và kế hoạch cải tiến ưu tiên.

## Rubric đánh giá / Assessment rubric

| Tiêu chí / Criterion | Điểm / Points |
|---|---:|
| Tính đúng và tích hợp / Correctness and integration | 20 |
| Thực nghiệm, baseline, evaluation / Experiments and evaluation | 25 |
| Reproducibility và engineering / Reproducibility | 20 |
| Safety, ethics, model card / Safety and model card | 20 |
| Demo và phản biện / Demo and defense | 15 |

Điều kiện chặn / Gating rule: bài thiếu provenance dữ liệu, chứa secret/PII thật, hoặc không chạy được smoke test có thể không đạt dù tổng điểm cao.

## ⚠️ Hiểu lầm thường gặp / Common misconceptions

- Demo hay không thay thế test set / A polished demo does not replace evaluation.
- Disclaimer không phải mitigation / A disclaimer is not a mitigation.
- Không được gọi model “an toàn” chỉ vì vài probes pass / Passing a few probes does not prove safety.
- Kết quả âm có giá trị nếu phương pháp và phân tích vững / Negative results can be valuable.
