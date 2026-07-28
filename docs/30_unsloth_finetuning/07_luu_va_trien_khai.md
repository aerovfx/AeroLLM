# Bài 7 — Inference, lưu và triển khai

[← Bài 6](06_danh_gia.md) · [Chỉ mục](index.md) · [Bài 8 →](08_do_an_cuoi_khoa.md)

## Mục tiêu

- phân biệt adapter, merged model và quantized export;
- chạy inference đúng template sau training;
- chọn GGUF/llama.cpp hoặc vLLM theo môi trường phục vụ.

## Ba dạng artifact

| Artifact | Khi dùng | Lưu ý |
|---|---|---|
| LoRA adapter | nhỏ, dễ chia sẻ và tiếp tục train | cần đúng base model/revision |
| Merged model | engine cần weights hợp nhất | tốn dung lượng, cần kiểm tra precision |
| GGUF quantized | laptop/CPU, llama.cpp, Ollama, LM Studio | đánh giá lại sau quantization |

Với triển khai nhiều người dùng/server, tài liệu Unsloth hướng tới vLLM và các precision phù hợp. Với máy cá nhân, GGUF qua llama.cpp là đường phổ biến. Đừng giả định kết quả adapter, merged và quantized giống hệt nhau—hãy chạy lại test.

## Lab bàn giao

1. Chuyển model sang inference mode theo notebook hiện hành.
2. Chạy lại 10 prompt cố định.
3. Lưu adapter kèm tokenizer, config và base model revision.
4. Export một định dạng phục vụ đã chọn.
5. Chạy lại evaluation cốt lõi trên artifact export.
6. Viết lệnh chạy tối thiểu và cấu hình decoding.

## Model card tối thiểu

- base model, revision và license;
- phương pháp/precision/adapter config;
- dataset, quyền sử dụng và split;
- metric before/after;
- hardware và thời gian train;
- intended use, out-of-scope use, rủi ro;
- format export, quantization và hướng dẫn inference;
- phiên bản package/notebook.

Không commit access token. Chỉ push model khi dataset, base license và quyền phân phối cho phép.

## Checkpoint

- [ ] Artifact nạp được trong session sạch.
- [ ] Đúng chat template và EOS khi inference.
- [ ] Evaluation sau export đạt ngưỡng.
- [ ] Có model card và lệnh tái lập.

Nguồn: [Unsloth Fine-tuning Guide — Running + Deploying](https://unsloth.ai/docs/get-started/fine-tuning-guide), [LM Studio deployment](https://unsloth.ai/docs/basics/inference-and-deployment/lm-studio).
