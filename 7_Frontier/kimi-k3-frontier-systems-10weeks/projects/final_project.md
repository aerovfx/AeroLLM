---
layout: course
title: "Final Project"
permalink: /7_Frontier/kimi-k3-frontier-systems-10weeks/projects/final_project.html
---

# Đồ án cuối khoá / Final project

[Trang khoá học](../INDEX.md)

## Đề bài

Chọn một hướng:

1. **Architecture:** KDA numerical stability, AttnRes retrieval hoặc QB routing.
2. **Agent systems:** verified environment có persistent state và anti-gaming tests.
3. **Evaluation/serving:** benchmark audit + small-model/API experiment có cost and privacy controls.

## Sản phẩm bắt buộc

- `README` nêu hypothesis, evidence class và giới hạn claim;
- source code có comment, type/shape assumptions và test;
- frozen config, seed, environment instructions và raw result log;
- technical report 1,500–2,500 từ: result-first summary, method, evidence, limitations, robustness checks;
- license/data provenance và safety note;
- source revision manifest; nếu dùng Hugging Face custom code phải pin revision và ghi kết quả code review;
- demo ≤8 phút.

## Hard gates

- Không dùng secret/PII trong repository hoặc API request.
- Không gọi toy demo là full-model reproduction.
- Agent project phải chấm final state bằng verifier, không dùng self-report làm success.
- Benchmark project phải ghi harness, tools, effort/sampling và số runs.
- API project phải giữ nguyên assistant history khi model yêu cầu nhưng không log/publish `reasoning_content`; self-host project phải hoàn thành license và `trust_remote_code` gates.

## Rubric / 100

| Hạng mục | Điểm |
|---|---:|
| Correct implementation + tests | 25 |
| Experimental design/baselines | 20 |
| Evidence and metric integrity | 20 |
| Failure analysis/robustness | 15 |
| Reproducibility + provenance | 10 |
| Communication and defense | 10 |
