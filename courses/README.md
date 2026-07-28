# Các khoá học chuyên đề 10 tuần

[Trang chủ](../README.md) · [Lộ trình dài hạn](../COURSE.md) · [Chỉ mục nội dung](../CONTENT_INDEX.md)

[Mở chỉ mục toàn bộ 40 tuần](WEEK_INDEX.md) · [Yêu cầu máy tính](COMPUTER_REQUIREMENTS.md)

Bốn khoá dưới đây có thể học độc lập. Mỗi khoá gồm 10 tuần, 20 buổi, bài học song ngữ Việt–Anh, thực hành, homework, rubric và đồ án cuối khoá.

Trước khi thực hành, xem [yêu cầu cấu hình máy tính](COMPUTER_REQUIREMENTS.md) và chạy `python courses/tools/check_environment.py`.

| Khoá | Code lab | Đối tượng | Đầu ra |
|---|---|---|---|
| [Xây LLM từ đầu](llm-from-scratch/INDEX.md) | [Python, C++, Notebook, Colab](llm-from-scratch/code/README.md) | Đã biết Python/PyTorch cơ bản | GPT nhỏ huấn luyện trên dữ liệu riêng |
| [Fine-tuning open-weight](openweight-finetuning/INDEX.md) | [Audit, QLoRA planner, Unsloth starter](openweight-finetuning/code/README.md) | Đã biết Transformer, muốn thích nghi model có sẵn | LoRA adapter + evaluation + deployment |
| [Pipeline huấn luyện open-weight](openweight-training-pipeline/INDEX.md) | [Capacity, governance, manifest](openweight-training-pipeline/code/README.md) | Kỹ sư/nhóm nghiên cứu có nền tảng training | Training plan, aligned checkpoint và release package |
| [Kimi K3: frontier architecture & agents](kimi-k3-frontier-systems/INDEX.md) | [KDA, AttnRes, QB, verifier](kimi-k3-frontier-systems/code/README.md) | Đã biết Transformer, muốn học model/system co-design | Toy reproductions + agent environment + technical audit |

## Chọn khoá

- Muốn hiểu từng phép tính trong GPT: học **Xây LLM từ đầu**.
- Muốn nhanh chóng tạo model chuyên biệt với GPU hạn chế: học **Fine-tuning open-weight**.
- Muốn vận hành quy trình dữ liệu → CPT/SFT → alignment → evaluation: học **Pipeline huấn luyện open-weight**.
- Muốn đọc technical report frontier và nối kiến trúc với RL/agent/serving: học **Kimi K3**.

## Mở nhanh từng tuần

| Tuần | Xây LLM từ đầu | Fine-tuning | Training pipeline | Kimi K3 |
|---:|---|---|---|---|
| 1 | [Bài học](llm-from-scratch/lessons/week01.md) | [Bài học](openweight-finetuning/lessons/week01.md) | [Bài học](openweight-training-pipeline/lessons/week01.md) | [Bài học](kimi-k3-frontier-systems/lessons/week01.md) |
| 2 | [Bài học](llm-from-scratch/lessons/week02.md) | [Bài học](openweight-finetuning/lessons/week02.md) | [Bài học](openweight-training-pipeline/lessons/week02.md) | [Bài học](kimi-k3-frontier-systems/lessons/week02.md) |
| 3 | [Bài học](llm-from-scratch/lessons/week03.md) | [Bài học](openweight-finetuning/lessons/week03.md) | [Bài học](openweight-training-pipeline/lessons/week03.md) | [Bài học](kimi-k3-frontier-systems/lessons/week03.md) |
| 4 | [Bài học](llm-from-scratch/lessons/week04.md) | [Bài học](openweight-finetuning/lessons/week04.md) | [Bài học](openweight-training-pipeline/lessons/week04.md) | [Bài học](kimi-k3-frontier-systems/lessons/week04.md) |
| 5 | [Bài học](llm-from-scratch/lessons/week05.md) | [Bài học](openweight-finetuning/lessons/week05.md) | [Bài học](openweight-training-pipeline/lessons/week05.md) | [Bài học](kimi-k3-frontier-systems/lessons/week05.md) |
| 6 | [Bài học](llm-from-scratch/lessons/week06.md) | [Bài học](openweight-finetuning/lessons/week06.md) | [Bài học](openweight-training-pipeline/lessons/week06.md) | [Bài học](kimi-k3-frontier-systems/lessons/week06.md) |
| 7 | [Bài học](llm-from-scratch/lessons/week07.md) | [Bài học](openweight-finetuning/lessons/week07.md) | [Bài học](openweight-training-pipeline/lessons/week07.md) | [Bài học](kimi-k3-frontier-systems/lessons/week07.md) |
| 8 | [Bài học](llm-from-scratch/lessons/week08.md) | [Bài học](openweight-finetuning/lessons/week08.md) | [Bài học](openweight-training-pipeline/lessons/week08.md) | [Bài học](kimi-k3-frontier-systems/lessons/week08.md) |
| 9 | [Bài học](llm-from-scratch/lessons/week09.md) | [Bài học](openweight-finetuning/lessons/week09.md) | [Bài học](openweight-training-pipeline/lessons/week09.md) | [Bài học](kimi-k3-frontier-systems/lessons/week09.md) |
| 10 | [Bài học](llm-from-scratch/lessons/week10.md) | [Bài học](openweight-finetuning/lessons/week10.md) | [Bài học](openweight-training-pipeline/lessons/week10.md) | [Bài học](kimi-k3-frontier-systems/lessons/week10.md) |

Các khoá dùng tài nguyên cục bộ trong repository và trỏ về nguồn chính thức khi API/công cụ có thể thay đổi.

Kiểm tra toàn bộ notebook sau khi chỉnh sửa:

```bash
python courses/tools/validate_course_notebooks.py
```
