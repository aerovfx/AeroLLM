---
layout: course
title: "Index"
permalink: /3_FineTuning/openweight-finetuning-10weeks/INDEX.html
---

# Fine-tuning mô hình Open-Weight / Fine-tuning Open-Weight Models

[Danh mục khoá ngắn](../../courses/README.md) · [Chỉ mục 40 tuần](../../courses/WEEK_INDEX.md) · [Lịch 20 buổi](schedule.md) · [Đồ án](projects/final_project.md)

[Mã minh hoạ và bài tập](code/README.md) · [Yêu cầu máy tính](../../courses/COMPUTER_REQUIREMENTS.md)

## Tổng quan / Overview

Khoá 10 tuần xây một pipeline SFT/QLoRA bằng Unsloth: xác định task, chọn model theo license/hardware, quản trị dataset/chat template, train, đánh giá, preference optimization, export và triển khai.

## Điều kiện đầu vào / Prerequisites

Python/PyTorch, Transformer và supervised learning cơ bản; tài khoản notebook/GPU khi thực hành. Người học phải tuân thủ license model/data và không đưa credential vào notebook.

## Chuẩn đầu ra / Learning outcomes

Thiết kế dataset có provenance, fine-tune model instruct bằng QLoRA, đánh giá before/after, nhận diện leakage/overfit, lưu adapter, export GGUF hoặc deployment phù hợp, viết model card.

## Bản đồ 10 tuần / Course map

| Tuần | Chủ đề | Bài học |
|---:|---|---|
| 1 | Task, baseline, chọn phương pháp | [Week 01](lessons/week01.md) |
| 2 | Model, license, hardware | [Week 02](lessons/week02.md) |
| 3 | Dataset design và QA | [Week 03](lessons/week03.md) |
| 4 | Chat templates và tokenization | [Week 04](lessons/week04.md) |
| 5 | LoRA/QLoRA | [Week 05](lessons/week05.md) |
| 6 | SFT và hyperparameters | [Week 06](lessons/week06.md) |
| 7 | Evaluation và error analysis | [Week 07](lessons/week07.md) |
| 8 | Preference optimization/DPO | [Week 08](lessons/week08.md) |
| 9 | Export GGUF và deployment | [Week 09](lessons/week09.md) |
| 10 | Capstone và model card | [Week 10](lessons/week10.md) |

## Đánh giá / Assessment

Data/model audits 20%, labs 30%, evaluation report 15%, capstone 35%. Điều kiện đạt: từ 70/100, không có leakage đã biết và artifact nạp được trong session sạch.

## Nguồn / Sources

- [Module Unsloth hiện có](../../docs/30_unsloth_finetuning/index.md).
- [Fine-tuning Guide chính thức](https://unsloth.ai/docs/get-started/fine-tuning-guide).
- [Tài liệu tham khảo khoá](references/README.md).
