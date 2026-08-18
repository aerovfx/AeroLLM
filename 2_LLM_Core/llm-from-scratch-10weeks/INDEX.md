---
layout: course
title: "Index"
permalink: /2_LLM_Core/llm-from-scratch-10weeks/INDEX.html
---

# Xây dựng và huấn luyện LLM từ đầu / Build and Train an LLM from Scratch

[Danh mục khoá ngắn](../../courses/README.md) · [Chỉ mục 40 tuần](../../courses/WEEK_INDEX.md) · [Lịch 20 buổi](schedule.md) · [Đồ án](projects/final_project.md)

[Mã minh hoạ và bài tập](code/README.md) · [Yêu cầu máy tính](../../courses/COMPUTER_REQUIREMENTS.md)

## Tổng quan / Overview

Khoá 10 tuần dùng PyTorch và `nanoGPTsource/` để đi từ next-token prediction đến một GPT nhỏ có thể huấn luyện, đánh giá và sinh văn bản. Mã nanoGPT được dùng như nguồn tham chiếu sư phạm; học sinh vẫn phải tự cài đặt các thành phần cốt lõi và kiểm chứng bằng test.

## Điều kiện đầu vào / Prerequisites

- Python, tensor PyTorch, đạo hàm và gradient descent cơ bản.
- Có thể dùng CPU/MPS/CUDA; bài bắt buộc được thiết kế cho cấu hình nhỏ.
- Không yêu cầu tải OpenWebText hoặc reproduce GPT-2.

## Chuẩn đầu ra / Learning outcomes

Người học có thể giải thích và cài đặt tokenizer, embedding, causal multi-head attention, MLP, residual/LN, GPT loss, training loop, checkpoint và sampling; đồng thời thực hiện ablation có baseline và báo cáo giới hạn.

## Bản đồ 10 tuần / Course map

| Tuần | Chủ đề | Bài học |
|---:|---|---|
| 1 | Language modeling và baseline | [Week 01](lessons/week01.md) |
| 2 | Tokenization và data pipeline | [Week 02](lessons/week02.md) |
| 3 | Embeddings và batching | [Week 03](lessons/week03.md) |
| 4 | Causal self-attention | [Week 04](lessons/week04.md) |
| 5 | Multi-head attention | [Week 05](lessons/week05.md) |
| 6 | MLP, normalization, residual | [Week 06](lessons/week06.md) |
| 7 | Lắp ráp GPT | [Week 07](lessons/week07.md) |
| 8 | Training, optimizer, checkpoint | [Week 08](lessons/week08.md) |
| 9 | Inference, sampling, evaluation | [Week 09](lessons/week09.md) |
| 10 | Capstone, safety, demo | [Week 10](lessons/week10.md) |

## Đánh giá / Assessment

Lab hàng tuần 35%, quiz/code reading 15%, mid-course integration 15%, capstone 35%. Điều kiện đạt: tổng từ 70/100 và capstone chạy/tái lập được.

## Nguồn / Sources

- [nanoGPTsource](../../nanoGPTsource/README.md) và [hệ thống bài tập 10 tuần](../../nanogpt_course/06_BAI_TAP_MA_NGUON/index.md).
- [Module Build GPT](../../docs/04_buildgpt/index.md), [Pre-training](../../docs/06_pretraining/index.md).
- [Tài liệu tham khảo khoá](references/README.md).
