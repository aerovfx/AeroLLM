# Đồ án — Training Release Candidate / Capstone — Training Release Candidate

[← Tổng quan](../INDEX.md) · [Lịch học](../schedule.md)

## Đề bài / Brief

Thiết kế và thực hiện ở quy mô phù hợp một pipeline CPT hoặc SFT + preference alignment cho model open-weight. Sản phẩm là release candidate có lineage, checkpoint, evaluation và runbook—không chỉ một notebook train thành công.

## Deliverables

- training charter, capacity và risk budget;
- data/model cards, license/provenance, split/contamination audit;
- resolved configs cho CPT/SFT/alignment;
- logs, checkpoint/resume evidence và incident note;
- capability/safety evaluation cùng failure taxonomy;
- packaged artifact, serving benchmark, model card, release/rollback decision.

## Rubric 100 điểm

| Hạng mục | Điểm |
|---|---:|
| Scope, capacity và stage gates | 10 |
| Data governance/quality | 20 |
| Training correctness/observability | 25 |
| Alignment/evaluation/red team | 25 |
| Release, serving, rollback, documentation | 20 |

## Scale-neutral policy

Điểm không phụ thuộc GPU count hoặc parameter count. Một reduced experiment có kiểm soát, provenance tốt và kết luận trung thực đạt điểm cao hơn full run thiếu baseline/evaluation.
