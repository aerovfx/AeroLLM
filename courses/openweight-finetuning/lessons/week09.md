# Tuần 09 — Xuất GGUF và triển khai / GGUF export and deployment

[← Tuần 8](week08.md) · [Mục lục khoá](../INDEX.md) · [40 tuần](../../WEEK_INDEX.md) · [Lịch 20 buổi](../schedule.md) · [Tuần 10 →](week10.md)

## Mục tiêu học tập / Learning objectives

- Merge adapter có kiểm soát và lưu artifact đầy đủ / merge adapters safely and save complete artifacts.
- Xuất/quantize GGUF, hiểu trade-off chất lượng–bộ nhớ / export and quantize GGUF with understood trade-offs.
- Chạy parity tests giữa training, merged và runtime / run parity tests across runtimes.
- Benchmark và thiết kế API có guardrails / benchmark and design a guarded API.

## Lý thuyết sâu / Deep theory

Merge LoRA áp $W'=W+sBA$ vào base weights. Phải khớp exact base revision, tokenizer và chat template. Quantization ánh xạ weights sang ít bit hơn; dung lượng gần $N\times b/8$ cộng metadata, nhưng quality loss phụ thuộc layer, calibration và scheme. GGUF là container phục vụ runtime hệ llama.cpp; tên quant không phải cam kết chất lượng phổ quát.

Tham khảo workflow xuất trong [Unsloth module](../../../docs/30_unsloth_finetuning/index.md). Không tin file chỉ vì load được: cần semantic parity và regression eval.

## Buổi 1 — Merge, export, quantize / Session 1 — Merge, export, quantize

### Quy trình / Procedure

1. Pin base model revision; hash adapter/config/tokenizer.
2. Load ở precision đủ để merge; kiểm tra missing/unexpected keys.
3. Sinh golden outputs/logits trước và sau merge.
4. Export GGUF FP16/BF16, rồi quantize ít nhất hai mức phù hợp RAM.
5. Ghi command, tool commit, architecture metadata và checksums.

```bash
# Chuyển merged Hugging Face checkpoint sang GGUF float16 làm bản trung gian chất lượng cao.
python convert_hf_to_gguf.py ./merged --outfile model-f16.gguf --outtype f16
# Quantize GGUF f16 xuống Q4_K_M để giảm disk/RAM; phải đánh giá lại sau quantization.
llama-quantize model-f16.gguf model-q4_k_m.gguf Q4_K_M
```

Lệnh cụ thể phụ thuộc version; lưu `--help`/commit của công cụ trong report.

## Buổi 2 — Serving và benchmark / Session 2 — Serving and benchmark

```bash
# Chạy HTTP inference server bằng model Q4_K_M, context tối đa 4096 token.
# Bind 127.0.0.1 chỉ cho phép truy cập từ máy cục bộ; port phục vụ là 8080.
llama-server -m model-q4_k_m.gguf --ctx-size 4096 --host 127.0.0.1 --port 8080
```

### Hands-on lab / Lab thực hành

- Test tokenizer special tokens, EOS, Unicode, JSON format và max context.
- So sánh 50 frozen prompts giữa adapter, merged, F16 GGUF và quantized GGUF.
- Đo model load, TTFT, p50/p95 inter-token latency, tokens/s, RSS/VRAM.
- Load test concurrency 1/2/4; ghi queueing và error rate.
- Thêm request-size limits, timeout, schema validation và không log prompt mặc định.

## Chính xác 5 câu hỏi thảo luận / Exactly 5 discussion questions

1. Vì sao merge parity cần kiểm tra logits lẫn behavior? / Why test both logits and behavior after merging?
2. Quantization nào phù hợp không thể quyết định chỉ bằng file size vì sao? / Why can file size alone not select a quantization?
3. TTFT và throughput tối ưu xung đột thế nào? / How can TTFT and throughput conflict?
4. Chat-template mismatch biểu hiện ra sao khi runtime vẫn chạy? / How does template mismatch appear despite successful loading?
5. Một local endpoint cần guardrails nào trước khi mở mạng? / What guardrails are needed before exposing an endpoint?

## Bài tập về nhà / Homework

Nộp merged model manifest, ít nhất hai GGUF quants, checksums, exact commands, parity results 50 prompts và benchmark matrix context×concurrency. Chọn một artifact triển khai dựa trên quality, p95 latency và memory; kèm API smoke tests và rollback plan.

## Rubric đánh giá / Assessment rubric

| Tiêu chí / Criterion | Điểm / Points |
|---|---:|
| Merge/export đúng và traceable | 25 |
| Parity/regression evaluation | 25 |
| Benchmark methodology | 20 |
| Deployment reliability/security | 20 |
| Decision memo | 10 |

## ⚠️ Hiểu lầm thường gặp / Common misconceptions

- Quantization không chỉ giảm precision activation / It primarily concerns stored weights here.
- Load thành công không chứng minh tokenizer/template đúng / Loading is not semantic correctness.
- `localhost` và public binding có risk khác nhau / Binding scope changes risk.
- Benchmark một prompt không đại diện workload / One prompt is not a benchmark.
