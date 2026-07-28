# Tuần 4 — Chọn tokenizer và model / Week 4 — Tokenizer and model selection

[← Tuần 3](week03.md) · [Mục lục khoá](../INDEX.md) · [40 tuần](../../WEEK_INDEX.md) · [Lịch 20 buổi](../schedule.md) · [Tuần 5 →](week05.md)

## Mục tiêu học tập / Learning objectives

- Benchmark tokenizer trên domain/language mục tiêu. / Benchmark tokenizers on target data.
- Chọn kiến trúc/scale theo budget và deployment. / Select architecture and scale under constraints.
- Tính parameter/memory implications của $V,d,L,T$. / Estimate parameter and memory implications.
- Đóng băng interface contract trước training. / Freeze the interface contract.

## Lý thuyết sâu / Deep theory

Embedding/output parameters xấp xỉ $Vd$ nếu tied và $2Vd$ nếu untied. Transformer decoder rough non-embedding params khoảng $L(12d^2)$ cho standard attention+MLP (hệ số thay đổi theo gated MLP/GQA). Attention activation tăng gần $T^2$. / Vocabulary, width, depth, and context couple quality and cost.

Tokenizer scorecard gồm bytes/token, fertility theo ngôn ngữ, P95 length, unknown/fallback rate, code/math handling và round-trip. Tokenizer hiệu quả tiếng Anh có thể gây sequence inflation tiếng Việt. / Aggregate averages can hide language-specific inequity.

Architecture decisions: absolute/RoPE positions, MHA/GQA, normalization, activation, tied embeddings, context and vocab. Các quyết định này đi vào checkpoint contract; đổi tokenizer sau training làm ID–embedding semantics lệch. / Architecture and tokenizer form a frozen compatibility contract.

## Buổi 1 — Tokenizer bake-off / Session 1 — Tokenizer bake-off

Đối chiếu [module tokenization](../../../docs/02_words_to_tokens_to_numbers/index.md) và local pipelines trong [`nanoGPTsource/data`](../../../nanoGPTsource/data). / Use local teaching and source references.

```python
def fertility(tokenizer, texts):
    # Tổng token trên corpus; tokenizer(t) được giả định trả danh sách token/ID.
    toks = sum(len(tokenizer(t)) for t in texts)
    # Whitespace words là proxy đơn giản; max(1,...) tránh chia 0 cho string rỗng.
    words = sum(max(1, len(t.split())) for t in texts)
    # Token/word thấp thường tiết kiệm context/compute, nhưng không tự chứng minh model tốt hơn.
    return toks / words
```

Chạy 3 tokenizer trên stratified Việt/Anh/code/math sample; report mean/P50/P95 và outliers, không chỉ mean. / Compare three candidates using stratified metrics and outliers.

## Buổi 2 — Model trade study / Session 2 — Model trade study

1. Tạo 3 configurations trong cùng compute envelope. / Create three compute-constrained designs.
2. Tính parameters, estimated FLOPs, weight/activation memory. / Estimate resources.
3. Chạy tiny proxy experiments cùng tokens và seed. / Run controlled proxy experiments.
4. Chốt architecture/tokenizer contract gồm hashes và special IDs. / Freeze a hashed contract.

## Câu hỏi thảo luận / Discussion questions

1. Vocabulary lớn làm training nhanh hơn hay chậm hơn? / Does a larger vocabulary speed training?
2. Width và depth đổi năng lực/parallelism thế nào? / How do width and depth trade off?
3. GQA giải quyết bottleneck nào? / Which bottleneck does GQA address?
4. Vì sao average fertility che giấu vấn đề? / Why can average fertility conceal inequity?
5. Khi nào nên reuse tokenizer của model có sẵn? / When should an existing tokenizer be reused?

## Bài tập về nhà / Homework

Nộp tokenizer bake-off trên ≥3 strata, ba architecture configs cùng budget, parameter/FLOP/memory sheet, proxy results và signed interface contract. / Submit a complete tokenizer/model trade study.

## Rubric đánh giá / Assessment rubric

| Hạng mục / Criterion | Điểm |
|---|---:|
| Tokenizer benchmark | 25 |
| Architecture/resource math | 25 |
| Fair proxy experiment | 20 |
| Contract/reproducibility | 20 |
| Recommendation | 10 |

## ⚠️ Ngộ nhận thường gặp / Common misconceptions

- Tokenizer chỉ ảnh hưởng preprocessing. / It affects cost and learned representation.
- Context dài công bố nghĩa train miễn phí ở context đó. / Long context is costly.
- Parameter count đủ dự đoán throughput. / Kernels and communication matter.
- Có thể đổi special IDs sau training. / IDs are part of checkpoint semantics.
