# Chỉ mục toàn bộ nội dung

Đây là bản đồ tra cứu. Thứ tự học chính thức nằm trong [COURSE.md](COURSE.md).

## Chỉ mục theo loại tài sản

| Loại | Chỉ mục |
|---|---|
| Bài giảng và chuyên đề | [docs/index.md](docs/index.md) |
| Notebook và mã thực hành | [src/README.md](src/README.md) |
| Khoá học nanoGPT 10 tuần | [nanogpt_course/README.md](nanogpt_course/README.md) |
| Các khoá chuyên đề 10 tuần | [courses/README.md](courses/README.md) |
| Training thực chiến | [aithucchien/README.md](aithucchien/README.md) |
| Visualizer web | [src/llm/](src/llm/) và hướng dẫn chạy ở [README](README.md) |
| Nhật ký/thiết kế dự án | [docs/project_logs/](docs/project_logs/) |

## Chỉ mục theo chủ đề

| Chủ đề | Lý thuyết | Thực hành |
|---|---|---|
| Python, PyTorch, toán | [Modules 20–29](docs/index.md#0-nền-tảng-lập-trình-và-toán) | [setup](src/utils/setup/README.md) |
| Tổng quan LLM | [Module 01](docs/01_llm_course/index.md) | [Visualizer](README.md#chạy-công-cụ-trực-quan) |
| Tokenization | [Module 02](docs/02_words_to_tokens_to_numbers/index.md) | [Tokenizer notebooks](src/tokenizer/ch08/README.md) |
| Embeddings | [Module 05](docs/05_embeddings_spaces/index.md) | [Embedding notebooks](src/tokenizer/ch08/README.md) |
| Transformer/GPT | [Module 04](docs/04_buildgpt/index.md) | [Pretrain ch03–04](src/README.md#xây-gpt-và-pre-training) |
| Pre-training | [Module 06](docs/06_pretraining/index.md) | [Pretrain ch05](src/pretrain/ch05/README.md) |
| Fine-tuning | [Module 07](docs/07_fine_tune_pretrained_models/index.md) | [Finetune ch06](src/finetune/ch06/README.md) |
| Unsloth/QLoRA | [Module 30](docs/30_unsloth_finetuning/index.md) | Khoá 8 buổi có lab và đồ án |
| Speculative decoding | [Module 31](docs/31_deepspec_training/index.md) | DeepSpec: data, target cache, draft training, evaluation |
| nanoGPT source exercises | [Khoá nanoGPT 10 tuần](nanogpt_course/README.md) | [Bài tập theo tuần](nanogpt_course/06_BAI_TAP_MA_NGUON/index.md) |
| Instruction/alignment | [Module 08](docs/08_instruction_tuning/index.md) | [Finetune ch07](src/finetune/ch07/README.md) |
| Evaluation | [Module 09](docs/09_quantitative_evaluations/index.md) | [Model evaluation](src/finetune/ch07/03_model-evaluation/README.md) |
| RAG | [Module 18](docs/18_rag/index.md) | [RAG templates](docs/18_rag/index.md) |
| Safety | [Module 19](docs/19_ai_safety/index.md) | [NanoGPT tuần 10](nanogpt_course/02_HOC_SINH/Tuan_10_Project_Safety/01_Topic.md) |
| Interpretability | [Modules 10–17, 20-I](docs/index.md#7-interpretability-nâng-cao) | Bài code challenge trong từng module |

## Nội dung hỗ trợ

- `minGPT/`: cài đặt GPT tối giản để tham khảo.
- `reward_functions.py`: ví dụ reward functions cho bài toán reasoning/training.
- `progress/`: dữ liệu tiến độ kỹ thuật, không phải bài học.
- `public/`, `styles/`, `src/cpu/`, `src/fluidsim/`: tài sản và demo kỹ thuật phụ trợ, không thuộc lộ trình LLM bắt buộc.
