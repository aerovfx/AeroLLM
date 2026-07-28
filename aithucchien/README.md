# AI Thực Chiến — nhánh training nâng cao

Nhánh ứng dụng của [Aero How to LLMs](../COURSE.md), phù hợp sau khi hoàn thành Giai đoạn 4. Nội dung tập trung vào dữ liệu, huấn luyện phân tán, post-training, đánh giá và đóng gói mô hình.

## Lộ trình 10 tuần

| Tuần | Nội dung |
|---:|---|
| 1 | [Nhập môn và mục tiêu](docs/training/tuan-01-intro.md) |
| 2 | [Synthetic data](docs/training/tuan-02-synthetic-data.md) |
| 3 | [Lọc dữ liệu](docs/training/tuan-03-data-filtering.md) |
| 4 | [Model và tokenizer](docs/training/tuan-04-model-tokenizer.md) |
| 5 | [Supervised fine-tuning](docs/training/tuan-05-sft-training.md) |
| 6 | [Continued pre-training](docs/training/tuan-06-continued-pretraining.md) |
| 7 | [Distributed training](docs/training/tuan-07-distributed.md) |
| 8 | [Preference optimization](docs/training/tuan-08-preference-opt.md) |
| 9 | [Evaluation](docs/training/tuan-09-evaluation.md) |
| 10 | [Model submission](docs/training/tuan-10-model-submission.md) |

## Chuyên đề hệ thống nâng cao

- [DeepSpec — huấn luyện draft model cho speculative decoding](../docs/31_deepspec_training/index.md): học sau distributed training và evaluation; yêu cầu capacity planning nghiêm ngặt do pipeline mặc định giả định 8 GPU và target cache rất lớn.

## Chuyên đề và tài liệu cuộc thi

- [Round 2](docs/round-2.md): quy định, công cụ Google GenAI và vibe coding.
- [Round 3: hướng dẫn model training](docs/round-3/model-training-guideline.md).
- [Round 3: synthetic data](docs/round-3/synthetic-data.md).
- [Round 4](docs/round-4.md).

Thứ tự khuyến nghị cho phần model training: [giới thiệu](docs/round-3/model-training-guideline/model-training-introduction.md) → [pre-training](docs/round-3/model-training-guideline/pre-training-strategy-and-setup.md) → [distributed training](docs/round-3/model-training-guideline/distributed-training.md) → [post-training/alignment](docs/round-3/model-training-guideline/post-training-alignment.md) → [finalization/submission](docs/round-3/model-training-guideline/model-finalization-and-submission.md).
