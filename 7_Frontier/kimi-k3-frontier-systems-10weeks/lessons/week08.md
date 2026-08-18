---
layout: course
title: "Week08"
permalink: /7_Frontier/kimi-k3-frontier-systems-10weeks/lessons/week08.html
---

# Tuần 8 — Agent environments và verifier-first training

[← Tuần 7](week07.md) · [Mục lục khoá](../INDEX.md) · [40 tuần](../../../courses/WEEK_INDEX.md) · [Lịch 20 buổi](../schedule.md) · [Tuần 9 →](week09.md)

## Mục tiêu / Objectives

- Định nghĩa task bằng state, action, budget và verifier. / Define executable agent tasks.
- Phân biệt public/hidden verifier và self-report. / Separate verifier evidence from claims.
- Thiết kế harness diversity và persistent state. / Design robust environments.

## Lý thuyết / Theory

Unified white-box environment cấu hình tools, prompts, context management, skills, memory và subagents để tránh overfit một scaffold. AET cho agent chỉ objective/constraints/interfaces; reward dựa trên final state. Public verifier hỗ trợ debug, hidden verifier chặn hard-code/reward hacking. Persistent mock apps tạo interdependent events mà không dùng external APIs thật.

## Buổi 1 / Session 1 — Environment contract

Viết contract: initial fixture, JSON tool schemas, permissions, state transition, time/token/action budgets, termination, public checks, hidden checks và reset procedure.

## Buổi 2 / Session 2 — Verifier lab

Chạy `agent_verifier.py`; thêm invalid action, idempotency, hidden scenario và audit log. Tạo một “cheating agent” để xác nhận verifier không tin message `done`.

## Câu hỏi thảo luận / Discussion questions

1. Vì sao final-state reward đáng tin hơn self-report? / Why verify final state?
2. Public verifier tạo reward hacking thế nào? / How can public feedback be gamed?
3. Harness diversity đo generalization ra sao? / How can scaffold generalization be measured?
4. Mock app nên giữ semantics nào? / Which semantics must a mock preserve?
5. Khi nào LLM judge không đủ? / When is an LLM judge insufficient?

## Bài tập / Homework

Nộp một environment package có ≥3 tools, ≥8 tests, public/hidden verifier, hard budget và threat model. / Submit an executable verified environment.

## Rubric

| Contract | Verifier/tests | Anti-gaming | Reproducibility | Documentation |
|---:|---:|---:|---:|---:|
| 20 | 30 | 25 | 15 | 10 |

## ⚠️ Ngộ nhận / Misconceptions

- Agent trả lời đẹp nghĩa task hoàn tất. / Completion requires state evidence.
- LLM judge là ground truth. / Judges can be biased or gamed.
- Hidden tests thay thế sandbox security. / They address different risks.
