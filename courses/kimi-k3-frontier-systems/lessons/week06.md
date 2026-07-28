# Tuần 6 — Million-token context và systems co-design

[← Tuần 5](week05.md) · [Mục lục khoá](../INDEX.md) · [40 tuần](../../WEEK_INDEX.md) · [Lịch 20 buổi](../schedule.md) · [Tuần 7 →](week07.md)

## Mục tiêu / Objectives

- Thiết kế curriculum 8K → 64K → 256K → 1M. / Design progressive context extension.
- Phân biệt KDA state, MLA KV cache và prefix cache. / Distinguish cache types.
- Lập systems memo có compute, memory, communication và failure modes. / Write a systems memo.

## Lý thuyết / Theory

K3 dùng NoPE và KDA recurrence nhưng vẫn cần long-context data rải dependency trên toàn sequence. Cooldown tập trung compute dài vào phần nhỏ training budget. Infrastructure phải giải quyết KDA context parallelism, MLA KV exchange, hybrid cache consistency, multimodal sample imbalance và prefix reuse.

## Buổi 1 / Session 1 — Curriculum and data

Thiết kế bốn stages với length distribution, dependency-distance probes, token budget và go/no-go metrics. Thêm exact/fuzzy dedup, perceptual hashing, binary/truncation filters và structural validation.

## Buổi 2 / Session 2 — Cache worksheet

Vẽ lifecycle prefill → decode → prefix hit → eviction cho KDA state và MLA pages. Nêu invariant: hai cache groups phải thống nhất hit boundary; concurrent growth không được sửa shared block.

## Câu hỏi thảo luận / Discussion questions

1. Context window và effective context khác gì? / How do nominal and effective context differ?
2. Vì sao sequence dài tự nhiên chưa đủ? / Why is natural long data insufficient?
3. KDA context parallelism giao tiếp khác softmax CP thế nào? / How does KDA CP differ?
4. Prefix cache có thể sai consistency khi nào? / When can cache consistency fail?
5. Curriculum dài nên dừng theo metric nào? / Which metrics should gate extension?

## Bài tập / Homework

Nộp context curriculum, dependency probe suite và cache design memo gồm failure recovery. / Submit curriculum, probes, and cache memo.

## Rubric

| Curriculum | Probes | Cache model | Failure handling | Feasibility |
|---:|---:|---:|---:|---:|
| 25 | 20 | 25 | 20 | 10 |

## ⚠️ Ngộ nhận / Misconceptions

- Hỗ trợ 1M nghĩa dùng mọi token tốt như nhau. / Capacity is not utilization quality.
- NoPE loại bỏ nhu cầu long-context training. / Data curriculum remains necessary.
- Cache hit chỉ là tối ưu, không ảnh hưởng correctness. / Hybrid cache boundaries must remain consistent.
