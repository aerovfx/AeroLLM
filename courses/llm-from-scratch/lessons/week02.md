# Tuần 2 — Tokenization và dữ liệu / Week 2 — Tokenization and data

## Mục tiêu học tập / Learning objectives

- So sánh character, byte và subword tokenization. / Compare character, byte, and subword tokenization.
- Mô tả BPE bằng pair statistics và merge rules. / Explain BPE via pair counts and merge rules.
- Thiết kế pipeline dữ liệu có provenance, split và kiểm tra Unicode. / Design a provenance-aware data pipeline.
- Đo fertility, compression và round-trip correctness. / Measure fertility, compression, and round-trip correctness.

## Lý thuyết sâu / Deep theory

Tokenizer là hàm $E:\text{text}\to\{0,\ldots,V-1\}^*$ và decoder $D$ nên thỏa $D(E(s))=s$ cho văn bản hỗ trợ. Character vocabulary nhỏ nhưng chuỗi dài; byte bao phủ mọi UTF-8; subword cân bằng độ dài và vocabulary. / A tokenizer defines the model's atomic units; byte fallback guarantees coverage while subwords trade sequence length for vocabulary size.

BPE bắt đầu từ đơn vị cơ sở, lặp việc gộp cặp kề nhau có tần suất lớn nhất. Chi phí attention xấp xỉ $O(T^2)$ nên tokenization làm chuỗi ngắn hơn có thể tiết kiệm đáng kể, nhưng vocabulary lớn làm embedding/output matrix tăng $O(Vd)$. / BPE repeatedly merges frequent adjacent pairs; shorter sequences reduce quadratic attention while larger vocabularies increase $Vd$ parameters.

Các metric: fertility $=\#tokens/\#words$, bytes-per-token $=\#UTF8\ bytes/\#tokens$, tỷ lệ `<unk>`, và độ dài percentile. Với tiếng Việt cần kiểm tra NFC/NFD, dấu kết hợp và khoảng trắng; chuẩn hoá làm thay đổi dữ liệu nên phải version. / Vietnamese evaluation must cover NFC/NFD, combining marks, and whitespace; normalization is a versioned transformation.

Tham chiếu pipeline cục bộ: [`nanoGPTsource/data/shakespeare_char/prepare.py`](../../../nanoGPTsource/data/shakespeare_char/prepare.py) và [bài tập tuần 2](../../../nanogpt_course/06_BAI_TAP_MA_NGUON/bai_tap_theo_tuan.md). / Inspect the local character and GPT-2 BPE pipelines.

## Buổi 1 — Thiết kế tokenizer / Session 1 — Tokenizer design

1. Encode cùng 20 câu Việt–Anh bằng character, UTF-8 byte và một subword tokenizer. / Encode the same bilingual sample three ways.
2. Lập bảng vocabulary size, mean/P95 length, bytes/token và round-trip errors. / Tabulate vocabulary and sequence metrics.
3. Mô phỏng ba vòng BPE trên corpus nhỏ bằng tay. / Simulate three BPE merges by hand.

```python
from collections import Counter  # Cộng dồn số lần xuất hiện của từng cặp symbol.

def pair_counts(words):
    # words chứa các tuple: (chuỗi symbol đã tách, tần suất của từ trong corpus).
    counts = Counter()
    for symbols, freq in words:
        # zip tạo các cặp liền kề; mỗi cặp được cộng theo tần suất của cả từ.
        counts.update({p: freq for p in zip(symbols, symbols[1:])})
    # Kết quả dùng để chọn cặp phổ biến nhất trong một bước BPE merge.
    return counts
```

## Buổi 2 — Pipeline dữ liệu có kiểm soát / Session 2 — Governed data pipeline

Hands-on:

1. Tạo manifest gồm URI/path, license, retrieval date, SHA-256, language và transformations. / Create a provenance manifest.
2. Deduplicate theo document trước khi split; giữ test “đóng băng”. / Deduplicate before splitting and freeze test.
3. Train tokenizer chỉ từ train; serialize vocabulary và ordered merges. / Fit only on train and serialize artifacts.
4. Viết test round-trip, deterministic IDs, BOS/EOS/PAD uniqueness và outlier length. / Test round trips, determinism, special IDs, and length outliers.

```python
# Chuyển Unicode string thành dãy byte 0..255; đây là tokenizer byte-level tối giản.
def utf8_encode(text):
    return list(text.encode("utf-8"))

# Ghép lại các byte rồi giải mã UTF-8 để phục hồi chuỗi gốc.
def utf8_decode(ids):
    return bytes(ids).decode("utf-8")

# Round-trip test bảo đảm tiếng Việt và emoji không bị mất dữ liệu.
assert utf8_decode(utf8_encode("LLM tiếng Việt 🚀")) == "LLM tiếng Việt 🚀"
```

## Câu hỏi thảo luận / Discussion questions

1. Tokenizer tiếng Anh có thể gây bất lợi định lượng nào cho tiếng Việt? / How can an English-centric tokenizer disadvantage Vietnamese?
2. Khi nào byte tokenizer tốt hơn BPE? / When is byte tokenization preferable to BPE?
3. Vì sao deduplication phải diễn ra trước split? / Why deduplicate before splitting?
4. Thay tokenizer sau pretraining phá vỡ những thành phần nào? / What breaks if the tokenizer changes after pretraining?
5. Metric tokenization nào liên hệ trực tiếp nhất với chi phí? / Which tokenization metric best predicts cost?

## Bài tập về nhà / Homework

Viết tokenizer character hoặc BPE tối giản, chạy trên ít nhất 1.000 câu Việt–Anh, chứng minh round-trip, báo cáo 4 metric, 20 edge cases và data card có license/provenance. / Implement a minimal tokenizer, evaluate it on at least 1,000 bilingual sentences, and submit tests, metrics, edge cases, and a data card.

## Rubric đánh giá / Assessment rubric

| Hạng mục / Criterion | Điểm |
|---|---:|
| Thuật toán encode/decode đúng / algorithm correctness | 30 |
| Pipeline, split, provenance / governed pipeline | 25 |
| Metrics và so sánh / metrics and comparison | 20 |
| Unicode/edge-case tests | 15 |
| Giải thích / communication | 10 |

## ⚠️ Ngộ nhận thường gặp / Common misconceptions

- Token không đồng nghĩa từ; một từ có thể thành nhiều token. / Tokens are not words.
- Unicode code point không đồng nghĩa byte. / Code points are not bytes.
- Vocabulary càng lớn không luôn tốt; embedding và rare tokens tăng. / Bigger vocab is not universally better.
- Decode đẹp không chứng minh pipeline không leakage. / Good decoding says nothing about leakage.
