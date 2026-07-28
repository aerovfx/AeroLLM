# Chỉ mục bài giảng Aero How to LLMs

[Trang chủ](../README.md) · [Lộ trình](../COURSE.md) · [Mã thực hành](../src/README.md)

Các module dưới đây được xếp theo thứ tự sư phạm. Mã module giữ nguyên để liên kết cũ tiếp tục hoạt động.

## 0. Nền tảng lập trình và toán

| Mã | Nội dung |
|---|---|
| 20-P | [Google Colab](20_python_colab_notebooks/index.md) |
| 21 | [Python: kiểu dữ liệu](21_python_data_types/index.md) |
| 22 | [Python: hàm](22_python_functions/index.md) |
| 23 | [Python: luồng điều khiển](23_python_flow_control/index.md) |
| 24 | [Python: trực quan dữ liệu](24_python_data_visualization/index.md) |
| 25 | [Python: chuỗi và văn bản](25_python_strings_texts/index.md) |
| 03 | [Indexing và slicing](03_python_indexing_and_slicing/index.md) |
| 26 | [PyTorch căn bản](26_python_pytorch/index.md) |
| 27 | [Toán cho deep learning](27_math_deep_learning/index.md) |
| 28 | [Gradient descent](28_gradient_descent/index.md) |
| 29 | [Bản chất mạng neural](29_essence_deep_learning/index.md) |

## 1. Tổng quan LLM

| Mã | Nội dung |
|---|---|
| 01 | [LLM Course: overview, Transformer, training, reasoning, agents](01_llm_course/index.md) |

## 2. Token và biểu diễn

| Mã | Nội dung |
|---|---|
| 02 | [Words to tokens to numbers](02_words_to_tokens_to_numbers/index.md) |
| 05 | [Embedding spaces](05_embeddings_spaces/index.md) |

## 3. Kiến trúc GPT

| Mã | Nội dung |
|---|---|
| 04 | [Build GPT from scratch](04_buildgpt/index.md) |

## 4. Huấn luyện

| Mã | Nội dung |
|---|---|
| 06 | [Pre-training](06_pretraining/index.md) |
| 07 | [Fine-tune pretrained models](07_fine_tune_pretrained_models/index.md) |
| 08 | [Instruction tuning](08_instruction_tuning/index.md) |

## 5. Đánh giá

| Mã | Nội dung |
|---|---|
| 09 | [Quantitative evaluations](09_quantitative_evaluations/index.md) |

## 5A. Thực hành fine-tuning với Unsloth

| Mã | Nội dung |
|---|---|
| 30 | [Fine-tuning LLM với Unsloth: QLoRA, SFT, evaluation và deployment](30_unsloth_finetuning/index.md) |

## 5B. Huấn luyện draft model và tối ưu inference

| Mã | Nội dung |
|---|---|
| 31 | [DeepSpec: speculative decoding, target cache, draft training và evaluation](31_deepspec_training/index.md) |

## 6. Ứng dụng và an toàn

| Mã | Nội dung |
|---|---|
| 18 | [Retrieval-Augmented Generation](18_rag/index.md) |
| 19 | [AI Safety](19_ai_safety/index.md) |

## 7. Interpretability nâng cao

| Mã | Nội dung |
|---|---|
| 15-I | [Nhập môn interpretability](15_interpretability/index.md) |
| 10 | [Identifying circuits](10_identifying_circuits/index.md) |
| 11 | [Investigating token embeddings I](11_investigating_token_embeddings/index.md) |
| 12 | [Investigating neurons và dimensions](12_investigating_neurons_dimensions/index.md) |
| 13 | [Investigating layers](13_investigating_layers/index.md) |
| 14 | [Modify activations](14_modify_activations/index.md) |
| 15-H | [Editing hidden states](15_editing_hidden_states/index.md) |
| 16 | [Interfering with attention](16_interfering_with_attention/index.md) |
| 17 | [Modifying MLP](17_modifying_mlp/index.md) |
| 20-I | [Embedding trajectories và residual stream](20_investigating_token_embeddings/index.md) |

## Ghi chú mã module

Kho cũ có hai module mang số 15 và hai module mang số 20. Chỉ mục dùng hậu tố `I`, `H`, `P` để phân biệt nhưng không đổi tên thư mục: `15-I` là nhập môn interpretability, `15-H` là hidden states, `20-P` là Python/Colab và `20-I` là nghiên cứu embedding.

Nhật ký phát triển được tách khỏi giáo trình tại [project_logs](project_logs/).
