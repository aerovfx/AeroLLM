# Bài 1 — Speculative decoding và kiến trúc DeepSpec

[← Chỉ mục](index.md) · [Bài 2 →](02_moi_truong_va_capacity.md)

## Mục tiêu

- giải thích vai trò draft model và target model;
- phân biệt chất lượng model với hiệu năng decoding;
- hiểu pipeline Data → Training → Evaluation của DeepSpec.

## Cơ chế

Draft model rẻ hơn đề xuất một hoặc nhiều token; target model xác minh đề xuất. Token được chấp nhận vẫn phải tuân theo phân phối mục tiêu của thuật toán, vì vậy mục tiêu không đơn thuần là “draft dự đoán giống target” mà là tăng số token được chấp nhận với chi phí draft/verification hợp lý.

Các chỉ số cần tách biệt:

- **Acceptance rate/accepted length:** đề xuất được target chấp nhận đến đâu.
- **Latency:** thời gian đến token đầu tiên và thời gian mỗi output token.
- **Throughput:** token/request xử lý trên đơn vị thời gian ở mức concurrency cụ thể.
- **Quality parity:** đầu ra không suy giảm ngoài sai khác sampling dự kiến.
- **Memory/storage:** draft weights, KV cache, target cache và checkpoint.

DeepSpec hỗ trợ ba họ draft model: DSpark, DFlash và Eagle3. DSpark kết hợp sinh bán tự hồi quy với verification được lập lịch theo confidence; paper báo cáo cải thiện tốc độ trong hệ thống phục vụ của tác giả, nhưng kết quả đó không tự động chuyển sang hardware, engine và workload khác.

## Lab thiết kế baseline

Chọn target model và ghi:

1. workload: chat, code, math hay batch generation;
2. concurrency và context/output length đại diện;
3. baseline không speculative decoding;
4. metric acceptance, latency, throughput, quality và memory;
5. ngưỡng thành công và điều kiện rollback.

## Checkpoint

- [ ] Phân biệt được fine-tuning target với training draft.
- [ ] Có baseline không speculative decoding.
- [ ] Không dùng acceptance rate như metric duy nhất.

Nguồn: [DeepSpec README](https://github.com/deepseek-ai/DeepSpec), [DSpark paper](https://arxiv.org/abs/2607.05147).
