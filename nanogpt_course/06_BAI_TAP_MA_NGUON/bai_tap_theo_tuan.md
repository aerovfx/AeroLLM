# Bản đồ bài tập nanoGPTsource theo 10 tuần

[← Chỉ mục](index.md) · [Quy trình thực hành](quy_trinh_thuc_hanh.md) · [Phiếu báo cáo](phieu_bao_cao.md)

## Tuần 1 — Next-token prediction và khám phá repository

**Nguồn:** [`README.md`](../../nanoGPTsource/README.md), [`sample.py`](../../nanoGPTsource/sample.py).

- **1A:** Vẽ luồng `start text → encode → model.generate → decode` bằng cách đọc `sample.py`.
- **1B:** Chạy sample từ một checkpoint có sẵn do giáo viên cung cấp; ghi input, số token mới và output.
- **1C:** Liệt kê ba lý do repo phù hợp để học nhưng không nên mặc định dùng cho production năm 2026.

**Nộp:** sơ đồ luồng và 5 quan sát từ code.

## Tuần 2 — Tokenization và dữ liệu nhị phân

**Nguồn:** [`data/shakespeare_char/prepare.py`](../../nanoGPTsource/data/shakespeare_char/prepare.py), [`data/shakespeare/prepare.py`](../../nanoGPTsource/data/shakespeare/prepare.py).

- **2A:** Với chuỗi tự chọn, tự tạo `stoi`, `itos`, encode rồi decode; chứng minh round trip.
- **2B:** Chạy Shakespeare character preparation; kiểm tra vocab size, kiểu `uint16`, số token train/val.
- **2C:** So sánh character tokenizer với GPT-2 BPE trên 10 câu Việt/Anh bằng số token và khả năng xử lý ký tự lạ.

**Nộp:** bảng so sánh và giải thích vì sao `train.bin`/`val.bin` không lưu trực tiếp string.

## Tuần 3 — Token embedding và position embedding

**Nguồn:** `GPT.__init__` và `GPT.forward` trong [`model.py`](../../nanoGPTsource/model.py).

- **3A:** Tìm `wte`, `wpe`; ghi shape theo `vocab_size`, `block_size`, `n_embd`.
- **3B:** Dùng model cực nhỏ, in shape sau token embedding, position embedding và phép cộng.
- **3C:** Thay `block_size`, dự đoán và đo thay đổi số tham số position embedding.

**Nộp:** bảng shape và phép tính số tham số bằng tay.

## Tuần 4 — Causal masking

**Nguồn:** `CausalSelfAttention.forward` trong [`model.py`](../../nanoGPTsource/model.py).

- **4A:** Với sequence length 4, tự vẽ mặt nạ tam giác dưới và các vị trí được phép nhìn.
- **4B:** Chạy attention trên tensor nhỏ; kiểm tra thay token tương lai không làm đổi output vị trí quá khứ.
- **4C:** So sánh nhánh flash attention và nhánh manual về cách thực hiện causal masking; không benchmark nếu thiết bị không hỗ trợ.

**Nộp:** test nhân quả có assertion.

## Tuần 5 — Query, Key, Value và scaled attention

**Nguồn:** `CausalSelfAttention` trong [`model.py`](../../nanoGPTsource/model.py).

- **5A:** Chú thích từng phép reshape/transposition của Q, K, V.
- **5B:** Bỏ hệ số $1/\sqrt{d_k}$ trong một bản sao, đo entropy attention và loss trên cùng batch.
- **5C:** Viết hook hoặc bản debug trả attention weights cho một câu ngắn; mô tả giới hạn diễn giải.

**Nộp:** sơ đồ shape và kết quả ablation có baseline.

## Tuần 6 — Multi-head attention, MLP và GELU

**Nguồn:** `CausalSelfAttention`, `MLP` trong [`model.py`](../../nanoGPTsource/model.py).

- **6A:** Chứng minh `n_embd` phải chia hết cho `n_head` trong cài đặt này.
- **6B:** Tính tham số attention và MLP bằng tay, đối chiếu PyTorch.
- **6C:** Thay GELU bằng ReLU trong bản sao; chạy budget nhỏ cùng seed và so sánh validation loss.

**Nộp:** bảng tham số và phiếu thí nghiệm.

## Tuần 7 — Transformer block và residual stream

**Nguồn:** `Block`, `GPT` trong [`model.py`](../../nanoGPTsource/model.py), [`transformer_sizing.ipynb`](../../nanoGPTsource/transformer_sizing.ipynb).

- **7A:** Vẽ thứ tự LayerNorm → Attention/MLP → residual addition.
- **7B:** Dùng hooks đo norm trước/sau từng block trên một batch.
- **7C:** So sánh model 2, 4 và 6 layer với ngân sách iteration cố định; báo cáo quality–speed–parameters.

**Nộp:** sơ đồ block và bảng trade-off.

## Tuần 8 — Training loop và optimization

**Nguồn:** `get_batch`, `estimate_loss`, `get_lr` và main loop trong [`train.py`](../../nanoGPTsource/train.py); [`config/train_shakespeare_char.py`](../../nanoGPTsource/config/train_shakespeare_char.py).

- **8A:** Chú thích một vòng `zero_grad → forward → backward → clip → optimizer.step`.
- **8B:** Chạy smoke test Shakespeare character bằng cấu hình nhỏ; lưu train/val loss và sample.
- **8C:** So sánh hai learning rate hoặc có/không gradient clipping, chỉ thay một biến.

**Nộp:** config đầy đủ, log rút gọn, checkpoint path và phiếu báo cáo.

## Tuần 9 — Sampling, temperature và top-k

**Nguồn:** `GPT.generate` trong [`model.py`](../../nanoGPTsource/model.py), [`sample.py`](../../nanoGPTsource/sample.py).

- **9A:** Giải thích phép chia logits cho temperature và top-k filtering.
- **9B:** Sinh cùng prompt với temperature 0.5, 1.0, 1.5 và cùng seed; so sánh lặp lại/đa dạng.
- **9C:** Bổ sung top-p sampling trong bản sao `generate`; viết test bảo đảm tập nucleus có cumulative probability đạt ngưỡng.

**Nộp:** bảng sampling và 3 mẫu ngắn.

## Tuần 10 — Đồ án, đánh giá và sử dụng có trách nhiệm

**Nguồn:** [`train.py`](../../nanoGPTsource/train.py), [`sample.py`](../../nanoGPTsource/sample.py), [`bench.py`](../../nanoGPTsource/bench.py).

- **10A:** Viết model card: data, config, intended use, limitations và safety.
- **10B:** Trình bày before/after bằng validation loss, tốc độ và bộ prompt cố định; phân tích ít nhất 5 failure cases.
- **10C:** Benchmark hai cấu hình với `bench.py` hoặc ablation scaling nhỏ; không tuyên bố tổng quát ngoài thiết bị đã đo.

**Nộp:** demo, code/config, model card, báo cáo và phần phản tư.

## Bài không bắt buộc vì tốn tài nguyên

- OpenWebText preparation và GPT-2 124M reproduction.
- GPT-2 medium/large/XL evaluation hoặc fine-tuning.
- DDP nhiều GPU/nhiều node.
- Scaling-law experiment đầy đủ.

Các phần này dùng để đọc config, capacity planning hoặc demo do giáo viên chuẩn bị; không giao chạy đại trà.
