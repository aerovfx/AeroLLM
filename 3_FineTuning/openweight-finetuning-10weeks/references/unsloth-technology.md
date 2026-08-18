---
layout: course
title: "Unsloth Technology"
permalink: /3_FineTuning/openweight-finetuning-10weeks/references/unsloth-technology.html
---

# Công nghệ Unsloth — tham chiếu kỹ thuật

Nguồn chính: [Fine-tuning LLMs Guide — Unsloth](https://unsloth.ai/docs/get-started/fine-tuning-llms-guide) (bản Markdown: [`.md`](https://unsloth.ai/docs/get-started/fine-tuning-llms-guide.md)).

## 1. LoRA và QLoRA

Mô hình có ma trận trọng số (Llama 70B = 70 tỷ số). Thay vì cập nhật toàn bộ trọng số, LoRA **thêm hai ma trận mỏng A và B** vào mỗi trọng số và chỉ tối ưu hai ma trận đó — nghĩa là chỉ huấn luyện khoảng **1% số weights**.

- **LoRA**: base model giữ 16-bit (không lượng tử), huấn luyện adapter low-rank.
- **QLoRA**: kết hợp LoRA với **4-bit** để tiết kiệm ~**75% bộ nhớ**.

Cập nhật: $W' = W + \frac{\alpha}{r}BA$, với $A\in\mathbb R^{r\times d_{in}}$, $B\in\mathbb R^{d_{out}\times r}$. Số tham số huấn luyện mỗi ma trận là $r(d_{in}+d_{out})$.

## 2. Dynamic 4-bit quantization (điểm khác biệt của Unsloth)

Unsloth dùng **dynamic 4-bit quants** thay vì BitsAndBytes 4-bit tĩnh:

| Hậu tố tên model | Ý nghĩa |
|---|---|
| `unsloth-bnb-4bit` | **Unsloth dynamic 4-bit** — tốn VRAM hơn một chút so với BnB 4-bit nhưng **chính xác cao hơn đáng kể**; độ mất accuracy so với LoRA 16-bit gần như được khôi phục |
| `bnb-4bit` | BitsAndBytes 4-bit tiêu chuẩn (không có "unsloth") |
| (không hậu tố) | Model gốc 16-bit hoặc 8-bit; Unsloth đôi khi kèm sửa chat template/tokenizer |

Khuyến nghị dùng bản `unsloth-...-unsloth-bnb-4bit` khi có sẵn.

## 3. Chọn model và phương pháp

- Người mới: bắt đầu với instruct model nhỏ (vd Llama 3.1 8B).
- **RL** (GRPO/GSPO): khi cần mô hình giỏi một hành vi cụ thể (tool-calling) qua reward function, không cần dữ liệu label.
- **LoRA/QLoRA**: parameter-efficient; **FFT (full fine-tuning) thường không cần thiết** — LoRA đúng cách có thể ngang FFT.
- **Nghiên cứu cho thấy train và serve cùng precision giúp giữ accuracy**: muốn serve 4-bit thì train 4-bit và ngược lại.

### Các cờ cấu hình Unsloth

| Cờ | Giá trị khuyến nghị | Ghi chú |
|---|---|---|
| `max_seq_length` | `2048` | Context để test; Unsloth cho phép fine-tune context dài gấp 4× |
| `dtype` | `None` | Dùng `torch.float16` / `torch.bfloat16` cho GPU mới |
| `load_in_4bit` | `True` | Bật QLoRA 4-bit (giảm 4× bộ nhớ) |
| `load_in_16bit` | `True` | LoRA 16-bit |
| `load_in_8bit` | `True` | Fine-tune 8-bit |
| `full_finetuning` | `True` | Full fine-tuning (tốn tài nguyên) |

> Chỉ bật **một** phương pháp (`True`) tại một thời điểm. Sai lầm phổ biến là nhảy thẳng vào FFT; hãy thử LoRA/QLoRA trước.

## 4. Dataset

- Thường cần 2 cột **question–answer**; chất lượng + số lượng quyết định lớn kết quả.
- Có thể sinh dữ liệu tổng hợp (QA pairs) bằng ChatGPT hoặc local LLM; Unsloth có notebook Synthetic Dataset (parse PDF/video → QA → auto-clean).
- Instruct model dùng conversational template (ChatML/ShareGPT); **Base model** dùng Alpaca/Vicuna. Instruct cần ít dữ liệu hơn.

## 5. Siêu tham số (Unsloth defaults)

| Tham số | Giá trị | Ý nghĩa |
|---|---|---|
| `per_device_train_batch_size` | `2` | Tăng để dùng GPU tốt hơn nhưng chậm do padding; thay vào đó tăng `gradient_accumulation_steps` |
| `gradient_accumulation_steps` | `4` | Mô phỏng batch lớn hơn không tăng bộ nhớ |
| `max_steps` | `60` | Chạy nhanh; full run thay bằng `num_train_epochs=1` (1–3 epochs tránh overfit) |
| `learning_rate` | `2e-4` | Giảm để chậm mà chính xác hơn: thử `1e-4`, `5e-5`, `2e-5` |

**Đọc loss**: nhiều trường hợp loss ~**0.5–1.0** là dấu hiệu tốt; loss không giảm → chỉnh cấu hình; loss về 0 → có thể overfitting (kiểm tra validation).

## 6. Đánh giá

- Đánh giá thủ công bằng cách chat với model; hoặc bật evaluation (tốn thời gian theo dataset). Tăng tốc: giảm eval set hoặc `evaluation_steps=100`.
- Tách ~20% train data làm test; nếu đã dùng hết thì đánh giá thủ công. Tool tự động có thể không khớp tiêu chí của bạn.

## 7. Chạy và triển khai

- Luôn gọi `FastLanguageModel.for_inference(model)` để hưởng **inference nhanh gấp 2×**.
- Tăng `max_new_tokens` (256/1024) để trả lời dài hơn (chờ lâu hơn).
- Lưu adapter LoRA ~**100MB** (không tự chứa base model).
- **Máy đơn** (laptop/Mac): chuyển **GGUF** qua llama.cpp để dùng Ollama/LM Studio.
- **Enterprise/multi-user** (FP8/AWQ): dùng **vLLM**.

## 8. Quan niệm sai (misconceptions)

- "Fine-tuning không học kiến thức mới" là **sai** — có thể train model chuyên biệt bằng FT + RL.
- "RAG tốt hơn fine-tuning" là **sai** — **fine-tuning có thể tái hiện mọi khả năng của RAG, ngược lại thì không** (RAG không đổi weights, chỉ bổ sung ngữ cảnh lúc inference).
- Đọc thêm: [FAQ + Is Fine-tuning Right For Me?](https://unsloth.ai/docs/get-started/fine-tuning-for-beginners/faq-+-is-fine-tuning-right-for-me.md).

## 9. Liên kết thực hành trong khoá

- Tuần 5 — [LoRA/QLoRA](../lessons/week05.md) và [module nội bộ](../../../docs/30_unsloth_finetuning/04_lora_qlora.md).
- Tuần 6 — [SFT và siêu tham số](../lessons/week06.md).
- Code mẫu an toàn: [`unsloth_sft_template.py`](../code/python/unsloth_sft_template.py) (dry-run, gate trước khi train).
