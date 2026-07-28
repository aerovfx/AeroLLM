# Tuần 1 — Đọc report và audit claim / Reading and auditing claims

[Mục lục khoá](../INDEX.md) · [40 tuần](../../WEEK_INDEX.md) · [Lịch 20 buổi](../schedule.md) · [Tuần 2 →](week02.md)

## Mục tiêu / Objectives

- Phân biệt fact, author claim, independent result và suy luận. / Separate facts, author claims, independent results, and inference.
- Giải thích total, activated parameters và lower-bound memory. / Explain model scale and feasibility.
- Lập claim ledger có nguồn, điều kiện và giới hạn. / Build an auditable claim ledger.

## Lý thuyết / Theory

K3 được công bố với 2.8T total parameters, 104B activated/token và context 1,048,576. MoE giảm compute trên mỗi token bằng sparse routing nhưng weights chưa active vẫn phải được lưu/nạp đâu đó. Lower bound weights là \(P\times b/8\); nó chưa gồm cache, activations, metadata hay runtime workspace.

Claim “2.5× scaling efficiency” là fitted validation-loss comparison với K2 cho toàn bộ architecture/data/training recipe. Không được đổi nghĩa thành “inference nhanh hơn 2.5×” hoặc “mỗi thành phần nhanh hơn 2.5×”. Xem [phân tích report](../TECHNICAL_REPORT.md).

## Buổi 1 / Session 1 — Evidence map

Đọc abstract, §1, §6 và đánh dấu: self-reported, third-party, in-house, dynamic leaderboard. Tạo ledger: `claim | source/section | setup | evidence class | limitation`.

## Buổi 2 / Session 2 — Feasibility lab

Chạy `model_scale_estimator.py`; giải thích vì sao 104B activated không phải 104B storage. Đọc [repository guide](../REPOSITORY_GUIDE.md), hoàn thành license checklist và viết cấu hình ba tầng: CPU lab, model nhỏ có GPU, full K3 qua API/cluster.

## Câu hỏi thảo luận / Discussion questions

1. “Open-weight” khác “open-source” ở đâu? / How do open-weight and open-source differ?
2. Vì sao activated parameters không đủ để tính serving memory? / Why are activated parameters insufficient for memory sizing?
3. Claim tổng hợp 2.5× cần ablation nào? / Which ablations would decompose 2.5×?
4. Benchmark nội bộ có giá trị và rủi ro gì? / What are the value and risk of in-house benchmarks?
5. Khi nào một leaderboard hết hạn làm bằng chứng? / When does leaderboard evidence become stale?

## Bài tập / Homework

Nộp 12-row claim ledger, repository/commit manifest, license checklist, memory worksheet và memo 500 từ chọn nội dung có thể/không thể tái tạo. / Submit a claim ledger, source manifest, license checklist, memory worksheet, and reproducibility memo.

## Rubric

| Claim accuracy | Evidence classes | Calculation | Limitations | Clarity |
|---:|---:|---:|---:|---:|
| 25 | 20 | 20 | 25 | 10 |

## ⚠️ Ngộ nhận / Misconceptions

- Total và activated parameters là cùng một đại lượng. / They are different quantities.
- Một PDF kỹ thuật luôn đủ để reproduce. / A report may omit critical recipe details.
- Điểm cao nhất một benchmark chứng minh model tốt nhất mọi task. / A benchmark win is not universal dominance.
