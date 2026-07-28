# Tuần 1 — Mô hình ngôn ngữ và baseline / Week 1 — Language models and baselines

## Mục tiêu học tập / Learning objectives

- Phát biểu bài toán dự đoán token kế tiếp và phân biệt mô hình ngôn ngữ với chatbot. / Formulate next-token prediction and distinguish a language model from a chatbot.
- Tính negative log-likelihood (NLL), cross-entropy và perplexity; nhận biết leakage. / Compute NLL, cross-entropy, and perplexity; identify leakage.
- Xây unigram/bigram baseline có train/validation split tái lập. / Build reproducible unigram and bigram baselines.
- Đọc luồng tối giản trong [`nanoGPTsource/train.py`](../../../nanoGPTsource/train.py). / Trace the minimal training flow in the local source.

## Lý thuyết sâu / Deep theory

Với chuỗi token $x_{1:T}$, quy tắc dây chuyền cho phép phân rã / For token sequence $x_{1:T}$, the chain rule gives:

$$p(x_{1:T})=\prod_{t=1}^{T}p(x_t\mid x_{<t}),\qquad \mathcal L=-\frac1T\sum_t\log p_\theta(x_t\mid x_{<t}).$$

Perplexity là $\mathrm{PPL}=\exp(\mathcal L)$ khi dùng log tự nhiên. Nó là “số lựa chọn hiệu dụng”, không phải độ chính xác và chỉ so sánh công bằng khi tokenizer, split và preprocessing giống nhau. / Perplexity is an effective branching factor, not accuracy, and comparisons require identical tokenization, splits, and preprocessing.

Unigram bỏ qua ngữ cảnh: $p(x_t=v)=c(v)/N$. Bigram dùng $p(v\mid u)=(c(u,v)+\alpha)/(c(u)+\alpha|V|)$. Smoothing tránh xác suất 0 trên validation. Neural LM thay bảng đếm bằng hàm tham số nhưng giao thức đánh giá phải được giữ cố định. / A neural LM replaces count tables with a parameterized function while preserving the evaluation protocol.

Baseline trả lời ba câu hỏi: pipeline có chạy đúng không, mô hình học hơn thống kê đơn giản không, và cải tiến có đáng chi phí không. Split phải theo tài liệu hoặc theo thời gian; cắt ngẫu nhiên từng dòng có thể đưa đoạn gần trùng sang cả train và validation. / A baseline checks pipeline correctness, learning signal, and cost-benefit; document-level or temporal splits reduce near-duplicate leakage.

## Buổi 1 — Từ xác suất đến loss / Session 1 — From probability to loss

1. Giảng viên tạo vocabulary nhỏ, viết chuỗi thành chỉ số và tính từng log-probability. / Encode a tiny corpus and calculate every log-probability.
2. Học viên giải thích vì sao xác suất toàn chuỗi rất nhỏ nhưng log-likelihood ổn định số. / Explain why sequence probability underflows while log-likelihood is stable.
3. Cả lớp lập “evaluation contract”: dữ liệu, unit token, split, seed, metric, hardware và commit. / Define an evaluation contract.

```python
import math  # Dùng log tự nhiên và hàm mũ để tính NLL/perplexity.

# Xác suất mà model gán cho token đúng tại ba vị trí; mọi giá trị phải thuộc (0, 1].
probs = [0.5, 0.25, 0.8]
# NLL là trung bình âm log-likelihood: xác suất đúng càng cao thì NLL càng thấp.
nll = -sum(math.log(p) for p in probs) / len(probs)
# Perplexity = exp(NLL); có thể hiểu gần đúng là số lựa chọn model còn phân vân.
print({"nll": nll, "ppl": math.exp(nll)})
```

## Buổi 2 — Baseline đếm và kiểm thử / Session 2 — Count baseline and tests

Thực hành / Hands-on:

1. Chuẩn hoá newline nhưng giữ nguyên Unicode; chia 90/10 theo vị trí. / Normalize newlines, preserve Unicode, and make a positional 90/10 split.
2. Đếm unigram/bigram chỉ trên train; chọn $\alpha$ trên validation. / Count only on train and tune $\alpha$ on validation.
3. Kiểm tra tổng phân phối bằng 1 và loss hữu hạn với token chưa thấy. / Test normalization and finite loss for unseen tokens.
4. Ghi baseline, seed và hash dữ liệu vào bảng kết quả. / Record baseline, seed, and data hash.

```python
from collections import Counter  # Đếm tần suất token và cặp token hiệu quả.

def bigram_probs(tokens, alpha=0.1):
    # Tạo vocabulary ổn định; sorted giúp kết quả có thứ tự tái lập được.
    vocab = sorted(set(tokens))
    # Ghép mỗi token với token kế tiếp để đếm bigram (u, v).
    pairs = Counter(zip(tokens, tokens[1:]))
    # Đếm số lần u xuất hiện ở vị trí có token kế tiếp.
    prev = Counter(tokens[:-1])
    # Add-alpha smoothing tránh xác suất bằng 0 cho bigram chưa từng thấy.
    return {
        (u, v): (pairs[u, v] + alpha) / (prev[u] + alpha * len(vocab))
        for u in vocab
        for v in vocab
    }
```

## Câu hỏi thảo luận / Discussion questions

1. Khi nào perplexity thấp hơn nhưng trải nghiệm sinh văn bản lại tệ hơn? / When can lower perplexity yield worse generation?
2. Vì sao không được fit vocabulary trên validation? / Why must vocabulary not be fitted on validation?
3. Bigram mạnh bất ngờ nói gì về dataset? / What does a surprisingly strong bigram reveal?
4. Baseline nào phù hợp hơn cho dữ liệu mã nguồn? / Which baseline better suits code data?
5. Ta cần log gì để tái lập một con số loss? / What must be logged to reproduce a loss number?

## Bài tập về nhà / Homework

Xây unigram và bigram trên corpus Việt–Anh nhỏ; báo cáo NLL/PPL train và validation, kiểm thử normalization, 10 mẫu sinh, một failure analysis và model card 1 trang. Không dùng validation để cập nhật counts. / Build both baselines on a small Vietnamese–English corpus; report metrics, tests, ten samples, failure analysis, and a one-page model card without fitting on validation.

## Rubric đánh giá / Assessment rubric

| Hạng mục / Criterion | Điểm / Points |
|---|---:|
| Split, provenance và chống leakage / split, provenance, leakage controls | 20 |
| Công thức và implementation đúng / correct math and implementation | 30 |
| Evaluation tái lập / reproducible evaluation | 20 |
| Phân tích mẫu lỗi / error analysis | 20 |
| Trình bày song ngữ, rõ ràng / bilingual clarity | 10 |

## ⚠️ Ngộ nhận thường gặp / Common misconceptions

- “LM hiểu sự thật vì dự đoán token tốt.” Loss chỉ đo khớp phân phối dữ liệu. / Loss measures distribution fit, not truth.
- “PPL so sánh được giữa mọi tokenizer.” Unit token khác làm mẫu số khác. / Different token units invalidate direct comparison.
- “Validation là dữ liệu để tinh chỉnh weights.” Nó dùng chọn quyết định, không backpropagate. / Validation is not training data.
- “Baseline đơn giản là không cần thiết.” Thiếu baseline khiến improvement không có mốc. / Improvements need a reference.
