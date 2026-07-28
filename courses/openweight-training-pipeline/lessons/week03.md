# Tuần 3 — Dữ liệu tổng hợp và lọc / Week 3 — Synthetic data and filtering

## Mục tiêu học tập / Learning objectives

- Thiết kế generator–critic–filter pipeline có provenance. / Design a traceable synthesis pipeline.
- Đo diversity, validity, contamination và human quality. / Measure quality and contamination.
- Hiệu chỉnh threshold thay vì tin tuyệt đối model judge. / Calibrate filters.
- Nhận biết model collapse và bias amplification. / Recognize collapse and bias amplification.

## Lý thuyết sâu / Deep theory

Synthetic pipeline: seed specification → prompt/program generation → candidate generation → deterministic validation → semantic/quality scoring → dedup → human audit → versioned release. Mỗi record lưu generator model/revision, decoding params, prompt hash và parent seed. / Synthetic records require lineage as much as collected data.

Nếu score $s$ và threshold $\tau$, precision/recall phải được đo trên human-labeled calibration set. Chọn $\tau$ theo cost của false accept versus false reject; đừng chọn bằng chính test cuối. / Filter thresholds are decision parameters requiring held-out calibration.

Self-training lặp có thể thu hẹp support, khuếch đại lỗi và phong cách. Diversity cần đo cả lexical n-grams, embedding clusters, intent coverage, length và answer strategy. Generator và judge cùng họ model có correlated errors. / Independent checks reduce correlated failure.

## Buổi 1 — Controlled generation / Session 1 — Controlled generation

Tạo taxonomy và quota trước khi generate. Dùng structured schema, bounded temperature và retry cap; log failed generations. / Define coverage before synthesis and preserve failures.

```python
import hashlib  # SHA-256 tạo fingerprint ổn định cho prompt.
import json  # Serialize decoding params khi lưu manifest bên ngoài hàm này.

def lineage(prompt, model, params):
    # encode() mặc định UTF-8; hexdigest dễ lưu trong JSON/CSV.
    prompt_hash = hashlib.sha256(prompt.encode()).hexdigest()
    # Ghi cả generator revision và decoding config để synthetic sample tái lập/audit được.
    return {
        "prompt_sha256": prompt_hash,
        "generator": model,
        "decoding": params,
    }
```

## Buổi 2 — Filter calibration / Session 2 — Filter calibration

1. Lấy stratified sample 200 records để double-review. / Create a human calibration set.
2. Vẽ precision/recall theo threshold; chọn policy và confidence interval. / Select a threshold transparently.
3. Dedup với seed/train/eval; kiểm tra answer leakage. / Check contamination against all protected sets.
4. So sánh raw/filtered distributions để phát hiện bias. / Audit distribution shift caused by filters.

## Câu hỏi thảo luận / Discussion questions

1. Model judge cùng họ generator gây lỗi gì? / What errors arise from correlated judge and generator?
2. Filter mạnh có thể giảm diversity ra sao? / How can strict filtering reduce diversity?
3. Khi nào synthetic data bổ sung thay vì thay thế human data? / When should synthetic data augment humans?
4. Làm sao phát hiện answer leakage? / How can answer leakage be detected?
5. Tại sao cần lưu rejected records metadata? / Why retain rejection metadata?

## Bài tập về nhà / Homework

Sinh 300 samples từ seed được phép; nộp lineage, taxonomy/quota, deterministic validators, 100-label calibration set, threshold curve, dedup report và 30-sample human audit. / Build and calibrate a small synthetic-data pipeline.

## Rubric đánh giá / Assessment rubric

| Hạng mục / Criterion | Điểm |
|---|---:|
| Generation design/lineage | 25 |
| Filter calibration | 25 |
| Diversity/contamination | 20 |
| Human audit | 20 |
| Limitations | 10 |

## ⚠️ Ngộ nhận thường gặp / Common misconceptions

- Synthetic đồng nghĩa không bản quyền/PII. / Generated data is not risk-free.
- Judge score là ground truth. / Model judging needs calibration.
- Dedup exact đủ bắt paraphrase leakage. / Semantic overlap remains.
- Acceptance rate cao chứng minh chất lượng. / It may indicate a weak filter.
