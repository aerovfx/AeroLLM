# Tuần 09 — Suy luận, lấy mẫu và đánh giá / Inference, sampling, and evaluation

## Mục tiêu học tập / Learning objectives

- Cài greedy, temperature, top-k và top-p sampling / implement greedy, temperature, top-k, and top-p sampling.
- Dùng KV cache và hiểu đánh đổi memory–latency / use a KV cache and explain memory–latency trade-offs.
- Tính perplexity không rò rỉ và đánh giá generation / compute leakage-free perplexity and evaluate generations.
- Thiết kế benchmark latency/throughput đáng tin / design trustworthy latency and throughput benchmarks.

## Lý thuyết sâu / Deep theory

Temperature biến logits $z$ thành $p_i\propto\exp(z_i/\tau)$. Top-k giữ k logits lớn nhất. Nucleus/top-p giữ tập nhỏ nhất có tổng xác suất ít nhất $p$. Perplexity là $\exp(\frac1N\sum -\log p(x_i|x_{<i}))$; phải tính theo token và xử lý cửa sổ context không double-count.

Không cache, decoding token-by-token tính lại K,V của prefix. KV cache lưu mỗi tầng, có kích thước xấp xỉ $2LBTHd_h$ phần tử; latency giảm nhưng memory tăng tuyến tính theo context và batch.

## Buổi 1 — Sampling và KV cache / Session 1 — Sampling and KV cache

```python
@torch.no_grad()  # Tắt autograd vì sampling không cần backward, giúp giảm memory.
def sample_next(logits, temperature=1.0, top_k=None):
    # Temperature <= 0 được quy ước là greedy decoding, chọn token logit lớn nhất.
    if temperature <= 0:
        return logits.argmax(-1, keepdim=True)
    logits = logits / temperature  # T<1 làm distribution sắc; T>1 làm phẳng/đa dạng hơn.
    if top_k:
        # Lấy ngưỡng là logit nhỏ nhất trong k token tốt nhất của từng sample.
        v, _ = torch.topk(logits, min(top_k, logits.size(-1)))
        # Loại mọi token dưới ngưỡng bằng -inf để softmax cho xác suất 0.
        logits = logits.masked_fill(logits < v[:, [-1]], float("-inf"))
    probs = torch.softmax(logits, -1)  # Chuẩn hoá logits thành xác suất tổng bằng 1.
    return torch.multinomial(probs, 1)  # Lấy một token ngẫu nhiên theo distribution.
```

### Thực hành / Hands-on

- Thêm top-p bằng sort, cumulative sum, shift mask để luôn giữ token đầu.
- Với seed cố định, kiểm tra greedy deterministic và sampling reproducible.
- Sinh cùng 5 prompts ở `(temperature, top_p)` = `(0,1)`, `(0.7,.9)`, `(1.2,.95)`.
- Đo time-to-first-token (TTFT), inter-token latency và tokens/s sau warmup.
- Cài cache từng layer; kiểm chứng logits cached/non-cached gần bằng nhau.

## Buổi 2 — Đánh giá / Session 2 — Evaluation

Đánh giá gồm intrinsic (NLL/perplexity), behavioral (đúng yêu cầu, coherence), safety và systems. Không chọn hyperparameter trên test. Generation rubric cần blind review và thứ tự xáo trộn; báo agreement giữa người chấm.

```python
@torch.no_grad()  # Evaluation không lưu computation graph.
def token_nll(model, batches):
    total_nll = 0  # Tổng negative log-likelihood có trọng số theo token.
    total_tokens = 0  # Tổng token target dùng làm mẫu số.
    for x, y in batches:
        _, loss = model(x, y)  # loss mặc định là mean trên token của batch.
        n = y.numel()  # Số target token trong batch hiện tại.
        total_nll += loss.item() * n  # Đổi mean loss thành tổng loss.
        total_tokens += n  # Cộng mẫu số để xử lý batch có kích thước khác nhau.
    # Chia một lần ở cuối để mọi token có trọng số bằng nhau.
    return total_nll / total_tokens
```

### Lab đánh giá / Evaluation lab

1. Tạo held-out split theo document trước tokenization.
2. Tính NLL/perplexity và bootstrap interval theo document.
3. Xây 20 prompts phủ factual continuation, structure, long dependency và safety.
4. Chấm blind theo rubric 1–5; lưu cả failure examples, không chỉ trung bình.
5. Benchmark batch size 1/4 và context 64/256, có/không KV cache.

## Chính xác 5 câu hỏi thảo luận / Exactly 5 discussion questions

1. Temperature thấp có đảm bảo câu trả lời đúng hơn không? / Does lower temperature guarantee correctness?
2. Top-k và top-p phản ứng khác nhau thế nào với phân phối phẳng? / How do top-k and top-p differ on flat distributions?
3. Perplexity giữa hai tokenizer có so sánh trực tiếp được không? / Is perplexity directly comparable across tokenizers?
4. Vì sao throughput cao có thể đi cùng latency người dùng tệ? / Why can high throughput coexist with poor user latency?
5. Human evaluation cần biện pháp nào để giảm bias? / How can human-evaluation bias be reduced?

## Bài tập về nhà / Homework

Xây `generate.py` hỗ trợ seed, temperature, top-k, top-p, max tokens và EOS; thêm KV cache có parity test. Nộp evaluation report gồm perplexity held-out, 20-prompt rubric, ít nhất 10 failure cases và benchmark TTFT/tokens-s theo context/batch.

## Rubric đánh giá / Assessment rubric

| Tiêu chí / Criterion | Điểm / Points |
|---|---:|
| Sampling đúng và an toàn số / Correct sampling | 25 |
| KV cache và parity tests / KV cache and parity | 25 |
| Evaluation design / Thiết kế đánh giá | 25 |
| Benchmark có warmup/sync / Sound benchmark | 15 |
| Failure analysis / Phân tích lỗi | 10 |

## ⚠️ Hiểu lầm thường gặp / Common misconceptions

- Sampling parameters không sửa kiến thức sai trong weights / Sampling cannot fix missing knowledge.
- Cần `torch.cuda.synchronize()` khi đo GPU latency / Synchronize GPU timing.
- Perplexity thấp không tự động đồng nghĩa hữu ích/an toàn / Low perplexity is not sufficient.
- KV cache phải cập nhật position chính xác / Cached decoding still needs correct positions.
