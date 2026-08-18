# Các khoá học 10 tuần

[Trang chủ](../README.md) · [Lộ trình dài hạn](../COURSE.md) · [Chỉ mục nội dung](../CONTENT_INDEX.md)

Tám khoá `*-10weeks` dưới đây có thể học độc lập. Mỗi khoá gồm 10 tuần, bài học song ngữ Việt–Anh, code lab, bài tập và đồ án cuối khoá.

| # | Khoá | Đối tượng | Đầu ra |
|---|---|---|---|
| 1 | [Python & Toán cho LLM](../1_Foundations/python-math-foundations-10weeks/INDEX.md) | Người mới Python/PyTorch | Nền tảng code + toán |
| 2 | [Xây LLM từ đầu](../2_LLM_Core/llm-from-scratch-10weeks/INDEX.md) | Đã biết Python | GPT nhỏ tự huấn luyện |
| 3 | [Fine-tuning open-weight](../3_FineTuning/openweight-finetuning-10weeks/INDEX.md) | Đã biết Transformer | LoRA adapter + deployment |
| 4 | [Pipeline huấn luyện open-weight](../4_Training/openweight-training-pipeline-10weeks/INDEX.md) | Kỹ sư / nhóm nghiên cứu | Training plan + release package |
| 5 | [AI Thực Chiến](../4_Training/ai-thuc-chien-10weeks/INDEX.md) | Đã xong Giai đoạn 4 | Mô hình đóng gói cho cuộc thi |
| 6 | [Ứng dụng LLM](../5_Applications/llm-applications-10weeks/INDEX.md) | Đã biết GPT | RAG + evaluation + safety |
| 7 | [Interpretability](../6_Interpretability/interpretability-10weeks/INDEX.md) | Đã biết Transformer | Báo cáo can thiệp / probing |
| 8 | [Kimi K3 frontier systems](../7_Frontier/kimi-k3-frontier-systems-10weeks/INDEX.md) | Đã biết Transformer | Toy reproduction + technical audit |

Ngoài ra còn khoá **nanoGPT 10 tuần** cho lớp học / học sinh THPT: [mở khoá](../nanogpt_course/README.md).

Trước khi thực hành, xem [yêu cầu cấu hình máy tính](COMPUTER_REQUIREMENTS.md) và chạy `python tools/course-scripts/check_environment.py`.

## Chọn khoá

- Mới bắt đầu: **Python & Toán cho LLM** → **Xây LLM từ đầu**.
- Muốn thích nghi model có sẵn: **Fine-tuning open-weight**.
- Muốn vận hành quy trình dữ liệu → CPT/SFT → alignment → evaluation: **Pipeline huấn luyện** hoặc **AI Thực Chiến**.
- Muốn xây ứng dụng thật (RAG, đánh giá, an toàn): **Ứng dụng LLM**.
- Muốn nghiên cứu hành vi bên trong mô hình: **Interpretability**.
- Muốn đọc technical report frontier và nối kiến trúc với RL/agent: **Kimi K3**.

## Mở nhanh từng tuần

| Tuần | Foundations | Xây LLM | Fine-tuning | Pipeline | Thực Chiến | Ứng dụng | Interp. | Kimi K3 |
|---:|---|---|---|---|---|---|---|---|
| 1 | [B](1_Foundations/python-math-foundations-10weeks/lessons/week01.md) | [B](2_LLM_Core/llm-from-scratch-10weeks/lessons/week01.md) | [B](3_FineTuning/openweight-finetuning-10weeks/lessons/week01.md) | [B](4_Training/openweight-training-pipeline-10weeks/lessons/week01.md) | [B](4_Training/ai-thuc-chien-10weeks/lessons/week01.md) | [B](5_Applications/llm-applications-10weeks/lessons/week01.md) | [B](6_Interpretability/interpretability-10weeks/lessons/week01.md) | [B](7_Frontier/kimi-k3-frontier-systems-10weeks/lessons/week01.md) |
| 2 | [B](1_Foundations/python-math-foundations-10weeks/lessons/week02.md) | [B](2_LLM_Core/llm-from-scratch-10weeks/lessons/week02.md) | [B](3_FineTuning/openweight-finetuning-10weeks/lessons/week02.md) | [B](4_Training/openweight-training-pipeline-10weeks/lessons/week02.md) | [B](4_Training/ai-thuc-chien-10weeks/lessons/week02.md) | [B](5_Applications/llm-applications-10weeks/lessons/week02.md) | [B](6_Interpretability/interpretability-10weeks/lessons/week02.md) | [B](7_Frontier/kimi-k3-frontier-systems-10weeks/lessons/week02.md) |
| 3 | [B](1_Foundations/python-math-foundations-10weeks/lessons/week03.md) | [B](2_LLM_Core/llm-from-scratch-10weeks/lessons/week03.md) | [B](3_FineTuning/openweight-finetuning-10weeks/lessons/week03.md) | [B](4_Training/openweight-training-pipeline-10weeks/lessons/week03.md) | [B](4_Training/ai-thuc-chien-10weeks/lessons/week03.md) | [B](5_Applications/llm-applications-10weeks/lessons/week03.md) | [B](6_Interpretability/interpretability-10weeks/lessons/week03.md) | [B](7_Frontier/kimi-k3-frontier-systems-10weeks/lessons/week03.md) |
| 4 | [B](1_Foundations/python-math-foundations-10weeks/lessons/week04.md) | [B](2_LLM_Core/llm-from-scratch-10weeks/lessons/week04.md) | [B](3_FineTuning/openweight-finetuning-10weeks/lessons/week04.md) | [B](4_Training/openweight-training-pipeline-10weeks/lessons/week04.md) | [B](4_Training/ai-thuc-chien-10weeks/lessons/week04.md) | [B](5_Applications/llm-applications-10weeks/lessons/week04.md) | [B](6_Interpretability/interpretability-10weeks/lessons/week04.md) | [B](7_Frontier/kimi-k3-frontier-systems-10weeks/lessons/week04.md) |
| 5 | [B](1_Foundations/python-math-foundations-10weeks/lessons/week05.md) | [B](2_LLM_Core/llm-from-scratch-10weeks/lessons/week05.md) | [B](3_FineTuning/openweight-finetuning-10weeks/lessons/week05.md) | [B](4_Training/openweight-training-pipeline-10weeks/lessons/week05.md) | [B](4_Training/ai-thuc-chien-10weeks/lessons/week05.md) | [B](5_Applications/llm-applications-10weeks/lessons/week05.md) | [B](6_Interpretability/interpretability-10weeks/lessons/week05.md) | [B](7_Frontier/kimi-k3-frontier-systems-10weeks/lessons/week05.md) |
| 6 | [B](1_Foundations/python-math-foundations-10weeks/lessons/week06.md) | [B](2_LLM_Core/llm-from-scratch-10weeks/lessons/week06.md) | [B](3_FineTuning/openweight-finetuning-10weeks/lessons/week06.md) | [B](4_Training/openweight-training-pipeline-10weeks/lessons/week06.md) | [B](4_Training/ai-thuc-chien-10weeks/lessons/week06.md) | [B](5_Applications/llm-applications-10weeks/lessons/week06.md) | [B](6_Interpretability/interpretability-10weeks/lessons/week06.md) | [B](7_Frontier/kimi-k3-frontier-systems-10weeks/lessons/week06.md) |
| 7 | [B](1_Foundations/python-math-foundations-10weeks/lessons/week07.md) | [B](2_LLM_Core/llm-from-scratch-10weeks/lessons/week07.md) | [B](3_FineTuning/openweight-finetuning-10weeks/lessons/week07.md) | [B](4_Training/openweight-training-pipeline-10weeks/lessons/week07.md) | [B](4_Training/ai-thuc-chien-10weeks/lessons/week07.md) | [B](5_Applications/llm-applications-10weeks/lessons/week07.md) | [B](6_Interpretability/interpretability-10weeks/lessons/week07.md) | [B](7_Frontier/kimi-k3-frontier-systems-10weeks/lessons/week07.md) |
| 8 | [B](1_Foundations/python-math-foundations-10weeks/lessons/week08.md) | [B](2_LLM_Core/llm-from-scratch-10weeks/lessons/week08.md) | [B](3_FineTuning/openweight-finetuning-10weeks/lessons/week08.md) | [B](4_Training/openweight-training-pipeline-10weeks/lessons/week08.md) | [B](4_Training/ai-thuc-chien-10weeks/lessons/week08.md) | [B](5_Applications/llm-applications-10weeks/lessons/week08.md) | [B](6_Interpretability/interpretability-10weeks/lessons/week08.md) | [B](7_Frontier/kimi-k3-frontier-systems-10weeks/lessons/week08.md) |
| 9 | [B](1_Foundations/python-math-foundations-10weeks/lessons/week09.md) | [B](2_LLM_Core/llm-from-scratch-10weeks/lessons/week09.md) | [B](3_FineTuning/openweight-finetuning-10weeks/lessons/week09.md) | [B](4_Training/openweight-training-pipeline-10weeks/lessons/week09.md) | [B](4_Training/ai-thuc-chien-10weeks/lessons/week09.md) | [B](5_Applications/llm-applications-10weeks/lessons/week09.md) | [B](6_Interpretability/interpretability-10weeks/lessons/week09.md) | [B](7_Frontier/kimi-k3-frontier-systems-10weeks/lessons/week09.md) |
| 10 | [B](1_Foundations/python-math-foundations-10weeks/lessons/week10.md) | [B](2_LLM_Core/llm-from-scratch-10weeks/lessons/week10.md) | [B](3_FineTuning/openweight-finetuning-10weeks/lessons/week10.md) | [B](4_Training/openweight-training-pipeline-10weeks/lessons/week10.md) | [B](4_Training/ai-thuc-chien-10weeks/lessons/week10.md) | [B](5_Applications/llm-applications-10weeks/lessons/week10.md) | [B](6_Interpretability/interpretability-10weeks/lessons/week10.md) | [B](7_Frontier/kimi-k3-frontier-systems-10weeks/lessons/week10.md) |

> Mỗi khoá có lịch chi tiết trong `schedule.md` riêng. Kiểm tra notebook sau khi chỉnh sửa: `python tools/course-scripts/validate_course_notebooks.py`.
