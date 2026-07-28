# Tuần 10 — Capstone reproduction-style và technical defense

## Mục tiêu / Objectives

- Tích hợp architecture, data, agent và evaluation. / Integrate the course pillars.
- Trình bày kết quả với evidence/limitations. / Defend evidence-backed results.
- Phân biệt reproduction, simulation và conceptual demo. / Label evidence honestly.

## Lý thuyết / Theory

Một capstone tốt không cần model lớn; nó cần hypothesis, controlled baseline, executable artifact, metrics, failure analysis và claim scope. Học viên chọn một cơ chế K3 và một downstream consequence, ví dụ QB → load variance, AttnRes → synthetic recall, verifier design → reward-hacking resistance.

## Buổi 1 / Session 1 — Integration review

Freeze code/data/config, chạy clean environment, kiểm tra seeds, artifact manifest và claim ledger. Peer reviewer thử phá verifier hoặc tìm confounder.

## Buổi 2 / Session 2 — Demo and defense

Demo 8 phút, technical defense 7 phút. Mỗi kết luận phải trỏ tới log/table/test; nêu ít nhất một negative result và một bước tiếp theo có tiêu chí dừng.

## Câu hỏi thảo luận / Discussion questions

1. Artifact này reproduce phần nào của K3? / What exactly is reproduced?
2. Baseline nào mạnh nhất có thể so công bằng? / What is the strongest fair baseline?
3. Kết quả nào không tổng quát lên 2.8T? / What does not scale to K3?
4. Failure nào thay đổi kết luận chính? / Which failure would overturn the result?
5. Experiment tiếp theo có information value cao nhất là gì? / What next test has highest value?

## Bài tập / Homework

Nộp theo [đặc tả đồ án](../projects/final_project.md): code, tests, report, logs, slides/demo và model/data/license notes. / Submit the complete capstone package.

## Rubric

| Correctness | Experimental rigor | Evidence | Limitations | Demo/report |
|---:|---:|---:|---:|---:|
| 25 | 25 | 20 | 15 | 15 |

## ⚠️ Ngộ nhận / Misconceptions

- Demo chạy một lần là reproducible. / Reproducibility needs environment and tests.
- Negative result là thất bại. / It is useful evidence when well controlled.
- Toy implementation có thể mang tên “Kimi K3 reproduction”. / Scope the claim to the mechanism tested.

