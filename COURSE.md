# Lộ trình khoá học Aero How to LLMs

## Mục tiêu đầu ra

Sau khi hoàn thành lộ trình chuẩn, người học có thể:

- giải thích luồng text → token → embedding → Transformer → logits;
- tự cài đặt một GPT nhỏ và huấn luyện trên tập văn bản;
- chọn chiến lược pre-training, fine-tuning, instruction tuning và đánh giá phù hợp;
- xây một ứng dụng RAG cơ bản, nhận diện rủi ro an toàn;
- dùng các kỹ thuật interpretability để khảo sát hành vi bên trong mô hình.

## Cách dùng lộ trình

Mỗi giai đoạn có ba phần: **học liệu chính**, **thực hành**, và **đầu ra**. Học liệu “mở rộng” không bắt buộc để chuyển giai đoạn. Người đã vững Python/PyTorch có thể bỏ qua Giai đoạn 0.

## Giai đoạn 0: Bổ trợ khi cần

**Mục tiêu:** đủ Python, tensor và toán để đọc notebook.

1. [Colab](docs/20_python_colab_notebooks/index.md)
2. [Kiểu dữ liệu Python](docs/21_python_data_types/index.md)
3. [Hàm](docs/22_python_functions/index.md), [luồng điều khiển](docs/23_python_flow_control/index.md), [chuỗi](docs/25_python_strings_texts/index.md)
4. [Indexing và slicing](docs/03_python_indexing_and_slicing/index.md)
5. [PyTorch căn bản](docs/26_python_pytorch/index.md)
6. [Toán cho deep learning](docs/27_math_deep_learning/index.md)
7. [Gradient descent](docs/28_gradient_descent/index.md) và [mạng neural căn bản](docs/29_essence_deep_learning/index.md)

**Đầu ra:** thao tác được tensor, viết vòng lặp huấn luyện nhỏ và giải thích loss/gradient.

## Giai đoạn 1: Bức tranh toàn cảnh

**Học liệu chính:** [LLM Course](docs/01_llm_course/index.md), ưu tiên overview, Transformer và training pipeline.

**Thực hành trực quan:** chạy ứng dụng ở trang chủ và quan sát đường đi của token qua mô hình.

**Đầu ra:** vẽ và thuyết minh được pipeline của một causal language model.

## Giai đoạn 2: Biểu diễn văn bản

1. [Text → token](docs/02_words_to_tokens_to_numbers/index.md)
2. [Không gian embedding](docs/05_embeddings_spaces/index.md)
3. [Notebook tokenizer và data loader](src/tokenizer/ch08/README.md)

**Đầu ra:** so sánh character/word/subword tokenization, tạo token IDs và batch huấn luyện.

## Giai đoạn 3: Tự xây GPT

1. [Build GPT from scratch](docs/04_buildgpt/index.md)
2. [Attention thực hành](src/pretrain/ch03/README.md)
3. [Mô hình GPT hoàn chỉnh](src/pretrain/ch04/README.md)

Học theo thứ tự: embedding → positional embedding → causal attention → multi-head attention → MLP → residual/layer norm → Transformer block → GPT.

**Đầu ra:** chạy được forward pass, kiểm tra shape và đếm tham số của một GPT nhỏ.

## Giai đoạn 4: Pre-training và sinh văn bản

1. [Pre-training: lý thuyết và bài tập](docs/06_pretraining/index.md)
2. [Training, weight loading và inference](src/pretrain/ch05/README.md)
3. Mở rộng: scheduler, tìm hyperparameter, Gutenberg, chuyển GPT/Llama và tối ưu bộ nhớ trong các thư mục con của `src/pretrain/ch05/`.

**Đầu ra:** huấn luyện một mô hình nhỏ, lưu/nạp checkpoint và sinh văn bản với tham số sampling đã chọn.

**Mốc dự án:** người muốn dừng ở một sản phẩm gọn có thể chuyển sang [dự án nanoGPT](nanogpt_course/03_THUC_HANH_DU_AN/index.md).

## Giai đoạn 5: Fine-tuning và alignment

1. [Fine-tuning mô hình pretrained](docs/07_fine_tune_pretrained_models/index.md)
2. [Classification fine-tuning code](src/finetune/ch06/README.md)
3. [Instruction tuning](docs/08_instruction_tuning/index.md)
4. [Instruction fine-tuning, evaluation và DPO code](src/finetune/ch07/README.md)
5. [Khoá thực hành Unsloth: QLoRA → SFT → deployment](docs/30_unsloth_finetuning/index.md)
6. Mở rộng thực chiến: [training pipeline](aithucchien/README.md)

**Đầu ra:** chuẩn bị dataset, fine-tune một mô hình, đánh giá baseline và mô tả khác biệt giữa SFT, PEFT/LoRA và preference optimization.

### Chuyên đề hệ thống sau huấn luyện

[Module DeepSpec](docs/31_deepspec_training/index.md) dành cho người đã hoàn thành training và evaluation, muốn huấn luyện draft model cho speculative decoding. Đây là nhánh tối ưu inference nhiều GPU/storage, không phải bước bắt buộc của fine-tuning.

## Giai đoạn 6: Đánh giá, ứng dụng và an toàn

1. [Đánh giá định lượng](docs/09_quantitative_evaluations/index.md)
2. [RAG](docs/18_rag/index.md)
3. [AI Safety](docs/19_ai_safety/index.md)

**Đầu ra:** xây một RAG tối thiểu có bộ câu hỏi đánh giá, ghi lại failure cases và biện pháp giảm rủi ro.

## Giai đoạn 7: Interpretability nâng cao

Học sau Giai đoạn 3 và 6:

1. [Nhập môn interpretability](docs/15_interpretability/index.md)
2. [Identifying circuits](docs/10_identifying_circuits/index.md)
3. [Token embeddings I](docs/11_investigating_token_embeddings/index.md)
4. [Neurons và dimensions](docs/12_investigating_neurons_dimensions/index.md)
5. [Layers](docs/13_investigating_layers/index.md)
6. [Modify activations](docs/14_modify_activations/index.md)
7. [Editing hidden states](docs/15_editing_hidden_states/index.md)
8. [Interfering with attention](docs/16_interfering_with_attention/index.md)
9. [Modifying MLP](docs/17_modifying_mlp/index.md)
10. [Token embeddings II: trajectories](docs/20_investigating_token_embeddings/index.md)

**Đầu ra:** hoàn thành một báo cáo can thiệp hoặc probing, nêu giả thuyết, phép đo, kết quả và giới hạn.

## Đồ án cuối khoá

Chọn một trong ba hướng:

- **Builder:** huấn luyện GPT nhỏ từ dữ liệu riêng và cung cấp demo sinh văn bản.
- **Application:** xây RAG có đánh giá retrieval và answer quality.
- **Research:** tái hiện một thí nghiệm interpretability và viết báo cáo.

Sản phẩm tối thiểu gồm README tái lập được, notebook/script chạy được, kết quả định lượng, phân tích lỗi và ghi chú an toàn.

## Lộ trình rút gọn

- **10 tuần cho lớp học:** [nanoGPT Course](nanogpt_course/README.md).
- **Bốn khoá nghề nghiệp, 10 tuần/20 buổi:** [Xây LLM từ đầu, fine-tuning open-weight, pipeline training và Kimi K3 frontier systems](courses/README.md).
- **Training thực chiến:** [AI Thực Chiến](aithucchien/README.md).
- **Tra cứu từng tài sản:** [Chỉ mục toàn bộ nội dung](CONTENT_INDEX.md).
