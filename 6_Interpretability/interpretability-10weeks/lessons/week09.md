---
layout: course
title: "Week09"
permalink: /6_Interpretability/interpretability-10weeks/lessons/week09.html
---

# Tuần 9 — Modifying MLP / Week 9 — Modifying MLP

[Mục lục khoá](../INDEX.md) · [Tài liệu nguồn](../../../docs/17_modifying_mlp/index.md) · [← Tuần 8](week08.md) · [Tuần 10 →](week10.md)

## Mục tiêu học tập / Learning objectives

- Giải thích median replacement: thay nhóm neuron hoạt động mạnh nhất bằng trung vị của tầng. / Explain median replacement of the most-active neurons.
- Mô tả "ripple-rate experiment": quét tỷ lệ can thiệp và đo logit change. / Describe the ripple-rate experiment sweeping intervention ratios.
- Diễn giải hiệu ứng ngưỡng: phần lớn thông tin do ~1–2% neuron mang, còn lại là dự phòng. / Interpret the threshold effect where ~1–2% of neurons carry most information.
- Thực hiện một "lesioning" thống kê và một phép loại bỏ subspace trên mô hình giả. / Perform a statistics-based lesion and a subspace removal.

## Công cụ và dữ liệu / Tools and data

- Python 3 + NumPy; MLP giả với vài nghìn neuron, trong đó một nhóm nhỏ mang tín hiệu ngữ nghĩa cấy sẵn.
- [`../code/week09/01_median_replacement.py`](../code/week09/01_median_replacement.py) và [`../code/week09/02_subspace_removal.py`](../code/week09/02_subspace_removal.py).

## Lý thuyết / Theory

Khối MLP là nơi xử lý phi tuyến và lưu trữ tri thức, nhưng có "sự bùng nổ chiều": mỗi block hàng nghìn neuron. Không thể khảo sát từng neuron, nên ta can thiệp theo *thống kê mô tả*.

**Median replacement**: lấy $p\%$ neuron có kích hoạt cao nhất, ghi đè giá trị của chúng bằng trung vị của toàn tầng. Trung vị đại diện "mức nền", nên ta chỉ xoá các đỉnh tín hiệu mà không làm sụp đổ phân phối năng lượng.

**Ripple-rate experiment**: quét $p = 10\%, 20\%,\dots,90\%$ rồi đo logit change. Kết quả kinh điển (trên GPT-2 Large) rất phản trực giác: đường 10% và 90% gần như đè lên nhau — một khi đã vô hiệu hoá "nhóm lõi", xoá thêm hàng nghìn neuron cũng chẳng thay đổi thêm. Ngược lại, ở mức siêu nhỏ ($0.2\%$–$4.5\%$), sự biến thiên mới xuất hiện rõ. Kết luận: phần lớn thông tin do ~1–2% neuron mạnh nhất mang, còn lại là nền dự phòng.

**Subspace removal**: thay vì chọn neuron, ta loại bỏ một *hướng* (subspace) trong không gian kích hoạt — tinh tế hơn khi thông tin nằm theo hướng, không theo neuron đơn lẻ.

## Lab từng bước / Step-by-step lab

1. Chạy [`01_median_replacement.py`](../code/week09/01_median_replacement.py), quét tỷ lệ $p$ và vẽ logit change theo $p$. / Sweep p and plot logit change.
2. Xác định "ngưỡng" nơi biến thiên bắt đầu xuất hiện. / Identify the threshold where variation appears.
3. Chạy [`02_subspace_removal.py`](../code/week09/02_subspace_removal.py), loại bỏ một hướng chính và đo tác động. / Remove a principal direction and measure impact.
4. So sánh: can thiệp theo neuron vs theo subspace, khi nào cái nào tốt hơn. / Compare neuron-wise vs subspace intervention.

## Liên kết code / Code links

- [`../code/week09/01_median_replacement.py`](../code/week09/01_median_replacement.py) — median replacement + ripple-rate.
- [`../code/week09/02_subspace_removal.py`](../code/week09/02_subspace_removal.py) — subspace removal.

## Câu hỏi thảo luận / Discussion questions

1. Vì sao 10% và 90% cho kết quả gần giống nhau? / Why do 10% and 90% give similar results?
2. "1–2% neuron mang thông tin" có mâu thuẫn với distributed representations không? / Does "1–2% of neurons carry information" contradict distributed representations?
3. Median replacement tốt hơn zero-out ở điểm nào? / How is median replacement better than zero-out?
4. Khi nào subspace removal chính xác hơn neuron ablation? / When is subspace removal more precise than neuron ablation?

## Bài tập về nhà / Homework

- **Cơ bản**: chạy hai script, báo cáo đường ripple-rate và ngưỡng tìm được.
- **Nâng cao**: thay median bằng mean, so sánh độ nhạy của hai phép thay thế.
- **Thử thách**: dùng PCA tìm hướng mang tín hiệu ngữ nghĩa nhất, loại bỏ nó, và chứng minh tác động lớn hơn việc loại bỏ hướng nhiễu.

## Yêu cầu nộp / Submission

- Đường ripple-rate + bảng neuron/subspace + nhận xét về mã hoá thưa, nộp theo đường dẫn thầy chỉ định.

## Rubric (100 điểm) / Assessment rubric

| Tiêu chí | Điểm |
|---|---:|
| Đúng chức năng: replacement/subspace đúng, logit change đúng | 35 |
| An toàn & xử lý lỗi: xử lý median, chiếu subspace, seed | 25 |
| Chất lượng code/tài liệu: chú thích, hàm rõ | 20 |
| Phân tích: đọc hiệu ứng ngưỡng, nêu mã hoá thưa | 20 |

## Lưu ý an toàn / Safety notes

- Chỉ can thiệp MLP giả local; không chạy lesioning trên model thật chưa được phép.
- "Ít neuron mang thông tin" là kết quả của một thí nghiệm cụ thể, không nên tổng quát hoá bừa.
- Ghi rõ cách chọn ngưỡng neuron (top-p theo giá trị tuyệt đối hay theo hạng) để tái lập.
