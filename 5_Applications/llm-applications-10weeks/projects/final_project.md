---
layout: course
title: "Final Project"
permalink: /5_Applications/llm-applications-10weeks/projects/final_project.html
---

# Capstone — Ứng dụng RAG an toàn có đánh giá

## Bài toán

Xây dựng một hệ thống hỏi–đáp RAG (Retrieval-Augmented Generation) chạy local, có lớp an toàn (guardrails) và được đánh giá định lượng end-to-end. Ứng dụng dùng tài liệu nội bộ giả (chính sách, hướng dẫn, FAQ) và một mô hình trả lời được **mock** (không gọi API thật), để tập trung vào đúng các kỹ năng của khóa: retrieval, generation, an toàn và đo lường.

## Phạm vi

- Tài liệu: ít nhất 10 văn bản ngắn (mỗi văn bản ~1 trang), dữ liệu giả do bạn tự viết.
- Bộ câu hỏi đánh giá (golden set): tối thiểu 30 cặp (câu hỏi, câu trả lời đúng + nguồn tham chiếu).
- Ngăn xếp: Python 3, vector store in-memory, embedding mock (bag-of-words/hash) hoặc local embedding nếu có.
- Không chứa secret, không gọi dịch vụ ngoài, không xử lý dữ liệu thật.

## Yêu cầu chức năng

1. **Ingest**: đọc văn bản → làm sạch → chunking (có overlap) → gán metadata → lưu vector.
2. **Retrieve**: embed câu hỏi → tìm top-k theo cosine similarity → (tùy chọn) re-rank.
3. **Generate**: trả lời chỉ dựa trên ngữ cảnh, kèm danh sách nguồn trích dẫn; nếu không đủ bằng chứng thì trả lời "không tìm thấy".
4. **Guardrails**: lọc đầu vào độc hại/tiêm nhiễm prompt; lọc đầu ra chứa nội dung cấm; chặn prompt injection.
5. **Đánh giá**: tính recall@k, MRR, nDCG (retrieval) và faithfulness/groundedness (generation) trên golden set.

## Yêu cầu phi chức năng

- Chạy được bằng `python` (không cần GPU, không cần mạng).
- Thời gian trả lời một câu hỏi trên golden set < vài giây.
- Kết quả tái lập được (seed cố định, log rõ ràng).
- Mã có chú thích tiếng Việt ở đầu file và theo khối logic.

## Milestones

| Tuần | Mốc |
|---:|---|
| 4–5 | Ingest + chunk + vector store chạy được trên tài liệu giả |
| 6 | Pipeline retrieve → generate → trích nguồn |
| 7 | Bộ metric retrieval + faithfulness trên golden set |
| 8 | Threat model + báo cáo bias/harms |
| 9 | Guardrails + red team log |
| 10 | Tích hợp, demo, báo cáo cuối |

## Deliverables

- `README.md` tái lập được: lệnh chạy, cấu trúc, seed, kết quả mong đợi.
- Mã nguồn Python đủ các module: ingest, retrieve, generate, guardrail, eval.
- Báo cáo đánh giá: bảng metric, phân tích lỗi, ví dụ thành công/thất bại.
- Model card / system card: giới hạn, rủi ro đã biết, biện pháp giảm thiểu.

## Demo script (5 phút)

1. Nạp 10 văn bản, in số chunk và metadata.
2. Hỏi 3 câu "có câu trả lời" → in câu trả lời + nguồn.
3. Hỏi 1 câu ngoài phạm vi → in "không tìm thấy".
4. Gửi 1 prompt injection → in guardrail chặn.
5. In bảng metric tổng hợp trên golden set.

## Threat model / Risk assessment

| Rủi ro | Khả năng | Tác động | Giảm thiểu |
|---|---|---|---|
| Hallucination ngoài ngữ cảnh | Cao | Trung bình | Chỉ trả lời từ context + kiểm tra groundedness |
| Prompt injection đọc dữ liệu khác | Trung bình | Cao | Lọc input, cô lập context khỏi chỉ thị hệ thống |
| Rò rỉ dữ liệu nhạy cảm | Trung bình | Cao | Chỉ dùng dữ liệu giả; mask PII nếu có |
| Retrieval sai nguồn | Cao | Trung bình | Re-rank + ngưỡng similarity + trích nguồn |
| Bias trong trả lời | Trung bình | Trung bình | Báo cáo bias + đánh giá nhóm đối xứng |

## Rubric (100 điểm)

| Tiêu chí | Điểm |
|---|---:|
| Đúng chức năng & tái lập được (ingest→retrieve→generate chạy end-to-end) | 35 |
| An toàn & xử lý lỗi (guardrail, chặn injection, xử lý ngoài phạm vi, cleanup) | 25 |
| Chất lượng code & tài liệu (chú thích, cấu trúc, README, model card) | 20 |
| Đánh giá định lượng & phân tích (metric retrieval + faithfulness, phân tích lỗi, bằng chứng chạy) | 20 |

## Tiêu chí thất bại bắt buộc (fail criteria)

- Chứa secret/token hoặc gọi dịch vụ ngoài không được ủy quyền.
- Không chạy được end-to-end bằng một lệnh duy nhất.
- Không có bất kỳ guardrail nào (đầu vào hoặc đầu ra).
- Không có bảng metric định lượng (chỉ mô tả định tính).
- Báo cáo "đã kiểm tra mô hình thật" mà không ghi rõ quyền sở hữu/ủy quyền.
