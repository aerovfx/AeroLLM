---
layout: course
title: "Index"
permalink: /6_Interpretability/interpretability-10weeks/INDEX.html
---

# Interpretability — Mechanistic Interpretability thực hành (10 tuần)

Nhánh chuyên sâu về **diễn giải cơ chế** (mechanistic interpretability, "mech interp") của AeroLLM. Khoá học đi từ quan sát (observational) sang can thiệp nhân quả (causal): học cách *đọc* biểu diễn bên trong mô hình, sau đó *ghi* vào đó — cắt bỏ, vá (patch), thay thế kích hoạt — để kiểm chứng giả thuyết về cách LLM thực sự tính toán.

Phù hợp sau khi đã nắm kiến trúc Transformer (attention, MLP, residual stream, LayerNorm) từ các khoá nền tảng của repo.

## Cấu trúc

- [Lịch học](schedule.md)
- `lessons/week01.md` … `week10.md`: bài học theo tuần.
- [Dự án cuối khóa](projects/final_project.md)
- [Code & môi trường](code/README.md)
- [Ánh xạ tài liệu nguồn](references/README.md)
- `exercises/weekNN/README.md`: bài tập 3 mức kèm rubric từng tuần.

## Lộ trình 10 tuần

| Tuần | Chủ đề | Trục kỹ năng |
|---:|---|---|
| 1 | Nhập môn interpretability & phương pháp | Nền tảng, residual stream, observational vs causal |
| 2 | Identifying circuits | Sparse probing, SAE, tìm mạch nhỏ |
| 3 | Token embeddings I: probing không gian nhúng | Cosine, RSA, analogy, trục ngữ nghĩa |
| 4 | Neurons và dimensions | Activation maximization, hooks, selectivity |
| 5 | Layers | Effective dimensionality, logit lens, MI |
| 6 | Modify activations | Causal mech interp, zero/mean/noise edit |
| 7 | Editing hidden states | Activation patching, IOI, skip layer |
| 8 | Interfering with attention | Head ablation, head patching |
| 9 | Modifying MLP | Median replacement, lesioning, subspace removal |
| 10 | Token embeddings II: trajectories + capstone | PCA trajectories, path length, báo cáo can thiệp |

## Quy tắc thực hành

1. Chỉ chạy thí nghiệm trên mô hình nhỏ/dữ liệu giả mà bạn kiểm soát được; không tải model lớn thật khi chưa cần.
2. Mọi can thiệp phải có **baseline (mô hình sạch)** để so sánh, và có **một giả thuyết** trước khi chạy.
3. Diễn giải là **bằng chứng hỗ trợ, không phải chân lý**: luôn ghi rõ giới hạn (variance ≠ relevance, thiếu ground truth).
4. Không can thiệp vào mô hình đang phục vụ người dùng thật; lab local có thể rollback.
