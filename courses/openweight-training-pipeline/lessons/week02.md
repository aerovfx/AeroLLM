# Tuần 2 — Data governance và licensing / Week 2 — Data governance and licensing

[← Tuần 1](week01.md) · [Mục lục khoá](../INDEX.md) · [40 tuần](../../WEEK_INDEX.md) · [Lịch 20 buổi](../schedule.md) · [Tuần 3 →](week03.md)

## Mục tiêu học tập / Learning objectives

- Tạo source registry và data lineage có kiểm toán. / Build an auditable source registry and lineage.
- Phân loại quyền sử dụng, PII, retention và deletion. / Classify rights, privacy, retention, and deletion.
- Thiết kế approval/quarantine gates. / Design approval and quarantine gates.
- Tạo datasheet/model-release evidence. / Produce release evidence.

## Lý thuyết sâu / Deep theory

“Có thể tải” không đồng nghĩa “được phép train”. Registry tối thiểu gồm source URL/path, owner, retrieval time, license/terms snapshot, allowed purpose, geography, consent basis, PII class, checksum và reviewer. / Accessibility does not establish training rights.

Lineage phải trả lời một record đến từ đâu, trải qua transformation nào, nằm trong shard/checkpoint nào, và làm sao xoá/đào tạo lại khi có yêu cầu. Content-addressed manifests và immutable raw zone giúp audit; raw access theo least privilege. / Traceability enables deletion impact analysis and incident response.

Risk scoring có thể dùng $R=L\times I$ (likelihood × impact), nhưng hard prohibitions không được “bù” bằng score thấp ở hạng mục khác. Legal review là vai trò chuyên môn; course checklist không phải tư vấn pháp lý. / Weighted scores never override hard policy constraints.

## Buổi 1 — Source registry / Session 1 — Source registry

Tạo registry cho 8 nguồn giả lập: approve, reject hoặc quarantine; ghi evidence chứ không chỉ kết luận. Phân biệt license của content, code tải dữ liệu và model output. / Review simulated sources with evidence.

```yaml
source_id: corpus_vi_001  # ID ổn định dùng nối lineage qua raw/clean/train datasets.
retrieved_at: 2026-07-28  # Ngày snapshot nguồn; cần để xử lý update/deletion request.
content_sha256: "..."  # Hash nội dung thật để phát hiện thay đổi và trùng lặp chính xác.
allowed_use: research-only  # Hạn chế từ license/consent; không tự suy rộng sang commercial.
pii_class: possible  # Cờ yêu cầu PII scan hoặc human review trước khi sử dụng.
decision: quarantine  # Chưa được train cho tới khi review giải quyết rủi ro.
reviewer: data-steward  # Vai trò/người chịu trách nhiệm cho quyết định governance.
```

## Buổi 2 — Policy-as-code và deletion drill / Session 2 — Policy and deletion drill

1. Validate required registry fields; block unknown license. / Enforce schema and hard gates.
2. Scan PII/toxicity with measured false positives; route flags to review. / Combine automation and review.
3. Simulate deletion request: locate derived shards, runs and checkpoints. / Perform an impact trace.
4. Produce signed dataset release manifest. / Produce a release manifest.

## Câu hỏi thảo luận / Discussion questions

1. Public-domain claim cần bằng chứng gì? / What evidence supports a public-domain claim?
2. Opt-out sau training ảnh hưởng lineage ra sao? / How does post-training opt-out affect lineage?
3. PII scanner false negatives nên được quản lý thế nào? / How should scanner false negatives be managed?
4. Dữ liệu model-generated mang rủi ro quyền nào? / What rights risks exist in generated data?
5. Khi nào cần quarantine thay vì delete? / When should data be quarantined rather than deleted?

## Bài tập về nhà / Homework

Nộp registry 12 nguồn giả lập, schema validator, approval matrix, deletion drill report và datasheet; không thu thập dữ liệu thật chưa được phép. / Submit a simulated governance package without unauthorized collection.

## Rubric đánh giá / Assessment rubric

| Hạng mục / Criterion | Điểm |
|---|---:|
| Registry/evidence completeness | 25 |
| Rights/privacy reasoning | 25 |
| Gates and validator | 20 |
| Lineage/deletion drill | 20 |
| Clear limitations | 10 |

## ⚠️ Ngộ nhận thường gặp / Common misconceptions

- Ghi attribution biến mọi use thành hợp lệ. / Attribution does not cure incompatible rights.
- Robots.txt là toàn bộ license analysis. / Crawl policy and content rights differ.
- Hash dữ liệu là ẩn danh hoá. / Hashing does not anonymize content.
- Governance chỉ làm sau training. / It begins before acquisition.
