---
layout: course
title: "Week10"
permalink: /6_Interpretability/interpretability-10weeks/lessons/week10.html
---

# Tuần 10 — Token embeddings II: trajectories + capstone báo cáo can thiệp / Week 10 — Token embeddings II: trajectories + intervention capstone

[Mục lục khoá](../INDEX.md) · [Tài liệu nguồn](../../../docs/20_investigating_token_embeddings/index.md) · [← Tuần 9](week09.md) · [Đồ án](../projects/final_project.md)

## Mục tiêu học tập / Learning objectives

- Theo dõi "quỹ đạo" (trajectory) của một token qua các tầng bằng cách chiếu PCA xuống 2D trên một hệ toạ độ chung. / Trace a token's trajectory across layers via PCA onto a shared 2D frame.
- Giải thích vì sao phải fit PCA một lần trên toàn bộ dữ liệu ghép (common space), không fit riêng từng tầng. / Explain why PCA must be fit once on concatenated data, not per layer.
- Đo "path length" của residual stream và liên hệ với dự đoán token. / Measure residual-stream path length and relate it to prediction.
- Nêu giới hạn "variance ≠ relevance" và tổng hợp toàn bộ quy trình quan sát → can thiệp thành một báo cáo capstone. / State the "variance ≠ relevance" limit and synthesize the observe→intervene pipeline into a capstone report.

## Công cụ và dữ liệu / Tools and data

- Python 3 + NumPy; các token giả (`him`, `her`, và một token sai ngữ pháp) đi qua một dãy tầng giả lập.
- [`../code/week10/01_trajectory_pca.py`](../code/week10/01_trajectory_pca.py) và [`../code/week10/02_path_length.py`](../code/week10/02_path_length.py).

## Lý thuyết / Theory

Không gian nhúng hàng nghìn chiều không thể nhìn trực tiếp. Để xem một token "di chuyển" qua các tầng, ta giảm chiều xuống 2D. **Sai lầm phổ biến** là fit PCA riêng cho từng tầng: mỗi tầng sẽ có một hệ trục khác nhau, khiến các điểm không so sánh được. Cách đúng là ghép toàn bộ vector của mọi token × mọi tầng thành một ma trận lớn, fit PCA **một lần**, rồi chiếu mọi điểm lên cùng hệ toạ độ chung.

Kết quả là một **quỹ đạo không gian trạng thái**: ban đầu các token nằm chen chúc, càng vào sâu các block càng tách xa nhau; token sai ngữ pháp thường "văng" ra xa khỏi cụm token đúng — mô hình đang xoay sở xử lý một đầu vào bất thường.

**Path length** đo tổng quãng đường vector residual đi qua các tầng (tổng độ dài từng bước cập nhật). Nó cho một đại lượng vô hướng để so sánh "token nào bị xử lý nhiều hơn".

Giới hạn cốt lõi: PCA mặc định coi phương sai lớn = thông tin quan trọng (**variance = relevance**), nhưng một hướng chỉ chiếm 0.1% phương sai vẫn có thể định hình toàn bộ dự đoán. Do đó trajectory chỉ là "cột đèn dẫn lối", không phải kết luận cuối.

Tuần này cũng là lúc đóng gói: từ quan sát (tuần 1–5) đến can thiệp (tuần 6–9) rồi tổng hợp thành một nghiên cứu hoàn chỉnh cho đồ án.

## Lab từng bước / Step-by-step lab

1. Chạy [`01_trajectory_pca.py`](../code/week10/01_trajectory_pca.py), quan sát quỹ đạo 2D của `him`/`her`/token sai. / Watch 2D trajectories of correct and incorrect tokens.
2. Xác nhận token sai ngữ pháp tách xa cụm token đúng ở tầng cuối. / Confirm the bad token diverges late.
3. Chạy [`02_path_length.py`](../code/week10/02_path_length.py), so path length giữa các token. / Compare path lengths.
4. Phác thảo báo cáo capstone: giả thuyết → quan sát → can thiệp → bằng chứng → giới hạn. / Draft the capstone: hypothesis → observe → intervene → evidence → limits.

## Liên kết code / Code links

- [`../code/week10/01_trajectory_pca.py`](../code/week10/01_trajectory_pca.py) — PCA trajectories (common space).
- [`../code/week10/02_path_length.py`](../code/week10/02_path_length.py) — residual-stream path length.

## Câu hỏi thảo luận / Discussion questions

1. Vì sao fit PCA riêng từng tầng là sai? / Why is per-layer PCA fitting wrong?
2. Token sai ngữ pháp "văng xa" gợi ý gì về cơ chế xử lý? / What does the bad token diverging suggest?
3. "Variance ≠ relevance" phá vỡ kết luận trajectory như thế nào? / How does "variance ≠ relevance" undermine trajectory conclusions?
4. Một báo cáo capstone cần những phần nào để đáng tin? / What sections make a trustworthy capstone?

## Bài tập về nhà / Homework

- **Cơ bản**: chạy hai script, mô tả quỹ đạo và path length.
- **Nâng cao**: thêm một token "lạ" mới và dự đoán trước quỹ đạo của nó, rồi kiểm chứng.
- **Thử thách**: viết báo cáo capstone 1–2 trang kết hợp một phép quan sát (tuần 1–5) và một phép can thiệp (tuần 6–9) trên cùng một mô hình giả.

## Yêu cầu nộp / Submission

- Quỹ đạo + bảng path length + bản nháp capstone, nộp theo đường dẫn thầy chỉ định (liên kết với đồ án cuối khoá).

## Rubric (100 điểm) / Assessment rubric

| Tiêu chí | Điểm |
|---|---:|
| Đúng chức năng: PCA common-space đúng, path length đúng | 35 |
| An toàn & xử lý lỗi: chuẩn hoá, xử lý ma trận suy biến, seed | 25 |
| Chất lượng code/tài liệu: chú thích, cấu trúc rõ | 20 |
| Phân tích: đọc quỹ đạo, nêu variance≠relevance, tổng hợp capstone | 20 |

## Lưu ý an toàn / Safety notes

- Chỉ dùng token/embedding giả local; không tải model thật.
- Luôn nêu giới hạn PCA (variance ≠ relevance) khi trình bày trajectory.
- Báo cáo capstone phải tách rõ "bằng chứng quan sát được" và "diễn giải của người viết".
