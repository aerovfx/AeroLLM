---
layout: course
title: "Index"
permalink: /4_Training/openweight-training-pipeline-10weeks/INDEX.html
---

# Pipeline đào tạo mô hình Open-Weight / Open-Weight Model Training Pipeline

[Danh mục khoá ngắn](../../courses/README.md) · [Chỉ mục 40 tuần](../../courses/WEEK_INDEX.md) · [Lịch 20 buổi](schedule.md) · [Đồ án](projects/final_project.md)

[Mã minh hoạ và bài tập](code/README.md) · [Yêu cầu máy tính](../../courses/COMPUTER_REQUIREMENTS.md)

## Tổng quan / Overview

Khoá 10 tuần dành cho nhóm kỹ thuật muốn thiết kế pipeline từ data governance, synthetic data, model/tokenizer selection đến continued pre-training, SFT, distributed training, preference optimization, evaluation, release và serving.

## Điều kiện đầu vào / Prerequisites

Đã hoàn thành fine-tuning cơ bản; đọc được PyTorch training code; hiểu distributed systems căn bản. Full-scale runs không bắt buộc—capacity plan, smoke test và reduced experiment được chấp nhận.

## Chuẩn đầu ra / Learning outcomes

Thiết kế training plan có data/model provenance, capacity budget, staged gates, observability, evaluation/safety suite, checkpoint lifecycle và release package; phân biệt CPT, SFT, preference optimization và inference optimization.

## Bản đồ 10 tuần / Course map

| Tuần | Chủ đề | Bài học |
|---:|---|---|
| 1 | Lifecycle và capacity | [Week 01](lessons/week01.md) |
| 2 | Data governance và licensing | [Week 02](lessons/week02.md) |
| 3 | Synthetic data và filtering | [Week 03](lessons/week03.md) |
| 4 | Tokenizer và model selection | [Week 04](lessons/week04.md) |
| 5 | Continued pre-training | [Week 05](lessons/week05.md) |
| 6 | SFT và instruction data | [Week 06](lessons/week06.md) |
| 7 | Distributed training và observability | [Week 07](lessons/week07.md) |
| 8 | Preference optimization/alignment | [Week 08](lessons/week08.md) |
| 9 | Evaluation và red teaming | [Week 09](lessons/week09.md) |
| 10 | Packaging, submission và serving | [Week 10](lessons/week10.md) |

## Đánh giá / Assessment

Design reviews 20%, reduced labs 25%, evaluation/red-team package 20%, capstone 35%. Điều kiện đạt: từ 70/100 và không bỏ qua license, provenance, evaluation hoặc rollback.

## Nguồn / Sources

- [AI Thực Chiến](../ai-thuc-chien-10weeks/INDEX.md), [pre-training](../../docs/06_pretraining/index.md), [instruction tuning](../../docs/08_instruction_tuning/index.md).
- [DeepSpec systems module](../../docs/31_deepspec_training/index.md) là phần mở rộng inference tuần 10.
- [Tài liệu tham khảo khoá](references/README.md).
