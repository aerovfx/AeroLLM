---
layout: course
title: "Week07"
permalink: /3_FineTuning/openweight-finetuning-10weeks/lessons/week07.html
---

# Tuần 07 — Đánh giá và phân tích lỗi / Evaluation and error analysis

[← Tuần 6](week06.md) · [Mục lục khoá](../INDEX.md) · [40 tuần](../../../courses/WEEK_INDEX.md) · [Lịch 20 buổi](../schedule.md) · [Tuần 8 →](week08.md)

## Mục tiêu học tập / Learning objectives

- Xây eval set chống leakage, đại diện use case / build a leakage-resistant, use-case-aligned eval set.
- Kết hợp metric tự động, rubric và pairwise review / combine automated metrics, rubrics, and pairwise review.
- Định lượng uncertainty và phân tích theo slice / quantify uncertainty and analyze slices.
- Biến failure taxonomy thành kế hoạch dữ liệu / turn failure taxonomy into a data plan.

## Lý thuyết sâu / Deep theory

Accuracy $=\frac{TP+TN}{N}$ không đủ cho class imbalance; precision $=TP/(TP+FP)$, recall $=TP/(TP+FN)$, $F_1=2PR/(P+R)$. Với generation mở, exact match thường quá nghiêm; rubric phải tách correctness, completeness, instruction adherence, style và safety.

Bootstrap theo example/document 1.000–10.000 lần để ước lượng confidence interval. Pairwise win rate nên có ties và randomize vị trí A/B. Phải freeze eval trước tuning; deduplicate train/eval bằng exact hash và near-duplicate similarity.

## Buổi 1 — Eval harness / Session 1 — Eval harness

```python
def evaluate(records, generate, score):
    rows = []  # Chứa prediction và metric ở mức từng test case để phân tích lỗi.
    for r in records:
        out = generate(r["prompt"])  # Sinh output với decoding config đã cố định.
        # Giữ id/slice để breakdown metric; score trả dict metric cho chính record này.
        rows.append({"id": r["id"], "slice": r["slice"],
                     "output": out, **score(out, r)})
    return rows  # Không aggregate sớm, tránh mất dữ liệu phục vụ error analysis.
```

### Hands-on / Thực hành

1. Viết eval specification: use case, population, exclusions, metrics, thresholds.
2. Tạo ≥100 items, có slice ngôn ngữ, độ dài, domain và độ khó.
3. Chạy base và tuned bằng cùng decoding config; ẩn model identity khi chấm.
4. Tính metric tổng, theo slice, CI và cost/latency.

## Buổi 2 — Error analysis / Session 2 — Error analysis

Chọn ngẫu nhiên failures và successes, không chỉ ví dụ “thú vị”. Gán primary cause và secondary tags. Taxonomy đề xuất: knowledge gap, reasoning, instruction miss, format/schema, hallucination, verbosity, refusal, toxicity, truncation.

```python
from collections import Counter  # Đếm số lỗi theo taxonomy.

def error_rates(rows):
    n = len(rows)  # Mẫu số là toàn bộ test cases, không chỉ cases thất bại.
    # Mỗi failed case có một primary_error để tránh double-count trong bảng chính.
    c = Counter(r["primary_error"] for r in rows if not r["pass"])
    # Tỷ lệ thể hiện phần test set bị từng nhóm lỗi; cần xử lý riêng khi n=0.
    return {k: v/n for k, v in c.items()}
```

### Lab / Hands-on lab

- Hai người chấm độc lập 30 items; thảo luận disagreement và sửa rubric.
- Pareto chart failure categories; chọn top causes theo frequency × severity.
- Trace mỗi cause tới data/template/hyperparameter/serving hypothesis.
- Đề xuất thí nghiệm phân biệt hypotheses, không sửa dữ liệu mù quáng.

## Chính xác 5 câu hỏi thảo luận / Exactly 5 discussion questions

1. Vì sao một điểm trung bình có thể che giấu regression nghiêm trọng? / How can an average hide severe regressions?
2. LLM-as-judge tạo bias nào và cần kiểm tra ra sao? / What biases does LLM-as-judge introduce?
3. Khi nào exact match là metric phù hợp? / When is exact match appropriate?
4. Data leakage có thể xảy ra ngoài exact duplicates thế nào? / How can leakage occur beyond exact duplicates?
5. Failure taxonomy tốt cần cân bằng độ chi tiết ra sao? / How should a useful taxonomy balance granularity?

## Bài tập về nhà / Homework

Nộp eval set ≥100 items, schema, harness, raw generations base/tuned, blind review ≥30 pairs, bootstrap CI và error-analysis memo. Đề xuất ba can thiệp ưu tiên với expected impact, risk và thí nghiệm xác nhận.

## Rubric đánh giá / Assessment rubric

| Tiêu chí / Criterion | Điểm / Points |
|---|---:|
| Eval design/leakage control | 25 |
| Harness và dữ liệu thô / Harness and raw evidence | 20 |
| Metrics, slices, uncertainty | 25 |
| Taxonomy và root-cause reasoning | 20 |
| Action plan | 10 |

## ⚠️ Hiểu lầm thường gặp / Common misconceptions

- Judge model không phải ground truth / A judge model is not ground truth.
- CI hẹp không sửa systematic bias / Narrow CIs do not remove systematic bias.
- Chỉ đọc failures làm sai ước lượng / Failure-only review biases estimates.
- Eval set không nên được dùng lặp lại như training set / Do not train to the test.
