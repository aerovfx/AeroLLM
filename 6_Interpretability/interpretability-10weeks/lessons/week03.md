---
layout: course
title: "Week03"
permalink: /6_Interpretability/interpretability-10weeks/lessons/week03.html
---

# Tuần 3 — Token embeddings I: probing không gian nhúng / Week 3 — Token embeddings I: probing embedding space

[Mục lục khoá](../INDEX.md) · [Tài liệu nguồn](../../../docs/11_investigating_token_embeddings/index.md) · [← Tuần 2](week02.md) · [Tuần 4 →](week04.md)

## Mục tiêu học tập / Learning objectives

- Tính cosine similarity giữa các vector nhúng và diễn giải ma trận tương đồng. / Compute cosine similarity between embeddings and interpret the similarity matrix.
- Dùng phép toán vector (analogy) $king - man + woman \approx queen$ để khảo sát cấu trúc ngữ nghĩa. / Use vector arithmetic to probe semantic structure.
- Xây một "trục ngữ nghĩa tuyến tính" (linear semantic axis) từ hiệu hai cực. / Build a linear semantic axis from the difference of two poles.
- Nêu giới hạn: similarity thô dễ gây ảo giác diễn giải (random embeddings cũng "trông có nghĩa"). / State limits: raw similarity can produce illusory interpretations.

## Công cụ và dữ liệu / Tools and data

- Python 3 + NumPy; nhúng giả có cấu trúc ngữ nghĩa cấy sẵn (để kiểm chứng phương pháp).
- [`../code/week03/01_cosine_similarity.py`](../code/week03/01_cosine_similarity.py) và [`../code/week03/02_analogy_arithmetic.py`](../code/week03/02_analogy_arithmetic.py).

## Lý thuyết / Theory

Không gian nhúng (embedding space) là nơi mỗi token sống dưới dạng vector $e\in\mathbb{R}^d$. Hai vector "gần nghĩa" thường có hướng giống nhau. Độ tương đồng chuẩn hoá theo hướng là cosine similarity:

$$\cos(e_a, e_b)=\frac{e_a\cdot e_b}{\|e_a\|\,\|e_b\|}\in[-1,1]$$

Vẽ ma trận cosine cho một tập token cho ta "bản đồ nhiệt ngữ nghĩa". Tuy nhiên, similarity thô không chứng minh gì cả: các nhúng *ngẫu nhiên* cũng sinh ra cấu trúc trông có vẻ có nghĩa (đây là một bài học cảnh giác quan trọng trong module nguồn).

Phép số học vector khai thác tính tuyến tính còn lại trong không gian nhúng. Nếu trục "giới tính" xấp xỉ là hướng $king - queen \approx man - woman$, thì

$$king - man + woman \approx queen$$

là một phép "đi dọc trục ngữ nghĩa". Kỹ thuật tổng quát: chọn hai cực $p_+$ và $p_-$, lấy **trục** $u = p_+ - p_-$, rồi chiếu mọi vector lên $u$ để đo "toạ độ theo khái niệm" (linear semantic axis). Cẩn thận: các phép này là "soft-coded", không phải quy luật cứng của mô hình.

## Lab từng bước / Step-by-step lab

1. Chạy [`01_cosine_similarity.py`](../code/week03/01_cosine_similarity.py), đọc ma trận tương đồng và tìm cụm nổi bật. / Read the similarity matrix and spot clusters.
2. Đối chiếu với "nhúng ngẫu nhiên" cùng script in ra để thấy sự khác biệt (và cả điểm giống gây ảo giác). / Compare with random embeddings.
3. Chạy [`02_analogy_arithmetic.py`](../code/week03/02_analogy_arithmetic.py), kiểm tra phép analogy và dựng một trục ngữ nghĩa. / Verify analogy and build a semantic axis.
4. Ghi lại một lưu ý: similarity/analogy chứng minh được gì, không chứng minh được gì. / Note what these methods can and cannot prove.

## Liên kết code / Code links

- [`../code/week03/01_cosine_similarity.py`](../code/week03/01_cosine_similarity.py) — cosine similarity + heatmap.
- [`../code/week03/02_analogy_arithmetic.py`](../code/week03/02_analogy_arithmetic.py) — analogy + linear semantic axis.

## Câu hỏi thảo luận / Discussion questions

1. Vì sao cosine similarity bỏ qua độ lớn vector? Khi nào điều đó là khuyết điểm? / Why does cosine ignore magnitude, and when is that a flaw?
2. Làm sao biết một cụm trên heatmap là "thật" chứ không phải ngẫu nhiên? / How do we know a heatmap cluster is real, not random?
3. Trục ngữ nghĩa tuyến tính giả định gì về không gian nhúng? / What assumption does a linear axis make about the space?
4. Analogy "soft-coded" nghĩa là gì? / What does "soft-coded" analogy mean?

## Bài tập về nhà / Homework

- **Cơ bản**: chạy hai script, liệt kê 3 cặp token tương đồng nhất và giải thích.
- **Nâng cao**: tự thêm một trục ngữ nghĩa mới (ví dụ "thành phố lớn vs làng quê") và chiếu tập token lên đó.
- **Thử thách**: sinh nhúng ngẫu nhiên 10 lần với seed khác nhau, ghi lại "cụm giả" xuất hiện bao nhiêu lần; bàn về nguy cơ overinterpretation.

## Yêu cầu nộp / Submission

- Ma trận/heatmap + bảng analogy + trục ngữ nghĩa + nhận xét giới hạn, nộp theo đường dẫn thầy chỉ định.

## Rubric (100 điểm) / Assessment rubric

| Tiêu chí | Điểm |
|---|---:|
| Đúng chức năng: cosine/analogy tính đúng, trục chiếu đúng hướng | 35 |
| An toàn & xử lý lỗi: chuẩn hoá vector, xử lý norm 0, seed | 25 |
| Chất lượng code/tài liệu: chú thích, đặt tên, in kết quả rõ | 20 |
| Phân tích: nhận diện ảo giác diễn giải, nêu giới hạn | 20 |

## Lưu ý an toàn / Safety notes

- Nhúng giả local; không tải word2vec/GPT thật khi chưa cần.
- Tránh kết luận "model hiểu nghĩa" chỉ từ similarity; luôn đối chiếu baseline ngẫu nhiên.
- Nếu dùng trục ngữ nghĩa về thuộc tính nhạy cảm (giới tính, sắc tộc), phải xử lý khách quan và nêu rõ mục đích nghiên cứu, không dùng để gán nhãn người thật.
