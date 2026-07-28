# Tuần 5 — Native multimodal, dữ liệu và scaling laws

## Mục tiêu / Objectives

- Thiết kế data taxonomy text/vision có provenance. / Design a multimodal data taxonomy.
- Giải thích joint-from-scratch multimodal training. / Explain native multimodal training.
- Đọc scaling curve mà không suy diễn causal contribution. / Read scaling laws critically.

## Lý thuyết / Theory

K3 joint-optimizes visual và textual tokens từ đầu. Text domains gồm Web, Code, Math, Knowledge; vision gồm caption, interleaved documents, OCR, perception, video và rendered visual-code pairs. MoonViT-V2 27 layers/~401M parameters dùng shared image/video parameters, spatial/temporal attention và token compression.

Scaling studies retune batch, learning rate, tokens-per-parameter và model shape. Report chọn cosine decay sau khi search hyperparameters độc lập cho cosine và WSD—một ví dụ tốt về tránh so scheduler dưới cấu hình chỉ thuận lợi cho một bên.

## Buổi 1 / Session 1 — Dataset card

Tạo schema `source, license, domain, modality, quality, dedup_key, safety, split`. Thiết kế contamination checks và held-out OOD validation.

## Buổi 2 / Session 2 — Scaling experiment design

Thiết kế grid model nhỏ cho cosine/WSD, mỗi scheduler có search space riêng. Không cần chạy full grid; nộp budget, metric và stopping rule.

## Câu hỏi thảo luận / Discussion questions

1. Native multimodal khác projector alignment hậu kỳ thế nào? / How does native multimodal differ from late alignment?
2. Rendered code–visual pairs dạy capability gì? / What do rendered pairs teach?
3. Vì sao dedup phải đi trước split? / Why deduplicate before splitting?
4. Shared hyperparameters làm scheduler comparison lệch ra sao? / How can shared hyperparameters bias comparison?
5. Scaling-law claim nào không suy ra được từ Figure 7? / What cannot Figure 7 establish?

## Bài tập / Homework

Nộp dataset card 1,000-sample hypothetical mixture, QA pipeline, contamination plan và scheduler study protocol. / Submit a dataset and scaling-study design.

## Rubric

| Taxonomy | Provenance/safety | QA | Experiment design | Limitations |
|---:|---:|---:|---:|---:|
| 20 | 25 | 20 | 25 | 10 |

## ⚠️ Ngộ nhận / Misconceptions

- Nhiều modality tự động tạo grounding. / Data and supervision quality still matter.
- Scaling curve chứng minh từng architectural choice. / It is an aggregate result.
- Validation loss thấp đảm bảo agent performance. / Downstream behavior needs separate evaluation.

