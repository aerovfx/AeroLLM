---
layout: course
title: "Week02"
permalink: /7_Frontier/kimi-k3-frontier-systems-10weeks/lessons/week02.html
---

# Tuần 2 — Hybrid KDA–Gated MLA / Hybrid sequence mixing

[← Tuần 1](week01.md) · [Mục lục khoá](../INDEX.md) · [40 tuần](../../../courses/WEEK_INDEX.md) · [Lịch 20 buổi](../schedule.md) · [Tuần 3 →](week03.md)

## Mục tiêu / Objectives

- Diễn giải KDA recurrence, decay và delta write. / Explain KDA recurrence.
- So sánh recurrent state với KV cache tăng theo sequence. / Compare state and KV-cache behavior.
- Nêu vai trò của periodic global MLA. / Explain periodic global attention.

## Lý thuyết / Theory

K3 lặp 3 KDA + 1 Gated MLA và kết thúc bằng global MLA. KDA update state bằng decay theo channel, delta correction và key–value write. Lower-bounded log-decay giữ \(\alpha>e^{-5}\), phục vụ ổn định số và kernel path. MLA lưu latent KV rồi reconstruct keys/values; NoPE tránh retune positional parameters khi tăng context.

## Buổi 1 / Session 1 — Derivation walk-through

Theo dõi shape của \(S\in R^{d_k\times d_v}\), `q`, `k`, `v`, `alpha`, `beta`. Chỉ ra output đọc sau current-token update và phân biệt recurrent/parallel chunk forms.

## Buổi 2 / Session 2 — Toy KDA

Chạy `toy_kda.py`; mở rộng thành 32 tokens, plot norm state và thử unbounded decay. Viết unit tests cho shape, lower bound, determinism và finite outputs.

## Câu hỏi thảo luận / Discussion questions

1. Vì sao K3 vẫn cần MLA nếu KDA hiệu quả? / Why retain MLA?
2. Lower bound giải quyết bottleneck tính toán nào? / Which bottleneck does bounded decay address?
3. NoPE đổi giả định về position thế nào? / How does NoPE change position handling?
4. Recurrent state có đánh mất thông tin gì? / What can a recurrent state forget?
5. Toy lab không đo được điều gì về production kernel? / What can the toy lab not measure?

## Bài tập / Homework

Nộp implementation chuỗi, bốn tests và memo so full attention/KDA/MLA về state, global access và complexity. / Submit sequence implementation, tests, and comparison memo.

## Rubric

| Correct recurrence | Tests | Numerical analysis | Comparison | Explanation |
|---:|---:|---:|---:|---:|
| 30 | 25 | 20 | 15 | 10 |

## ⚠️ Ngộ nhận / Misconceptions

- Linear attention luôn chính xác như softmax attention. / Different mechanisms have different inductive biases.
- O(1) recurrent state nghĩa toàn bộ serving O(1). / MLA layers still have growing cache.
- Toy PyTorch loop đo được Tensor Core throughput. / It does not.
