# Các khoá học chuyên đề 10 tuần

[Trang chủ](../README.md) · [Lộ trình dài hạn](../COURSE.md) · [Chỉ mục nội dung](../CONTENT_INDEX.md)

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

Các khoá dùng tài nguyên cục bộ trong repository và trỏ về nguồn chính thức khi API/công cụ có thể thay đổi.

Kiểm tra toàn bộ notebook sau khi chỉnh sửa:

```bash
python courses/tools/validate_course_notebooks.py
```
