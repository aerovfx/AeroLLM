# Code lab — Xây LLM từ đầu

[Khoá học](../INDEX.md) · [Cấu hình máy](../../COMPUTER_REQUIREMENTS.md)

| Tuần | Code | Cách dùng |
|---:|---|---|
| 1–9 | [`python/mini_gpt_lab.py`](python/mini_gpt_lab.py) | Tokenizer, batch, attention, GPT, train và sample |
| 2 | [`cpp/byte_tokenizer.cpp`](cpp/byte_tokenizer.cpp) | Minh hoạ UTF-8 byte tokenizer bằng C++17 |
| 1–9 | [`notebooks/mini_gpt_walkthrough.ipynb`](notebooks/mini_gpt_walkthrough.ipynb) | Notebook tutorial chạy top-to-bottom |
| 8–10 | [`colab/README.md`](colab/README.md) | Đưa notebook lên Colab và bật GPU |

Chạy Python lab:

```bash
python courses/llm-from-scratch/code/python/mini_gpt_lab.py
```

Biên dịch C++:

```bash
clang++ -std=c++17 -O2 courses/llm-from-scratch/code/cpp/byte_tokenizer.cpp -o /tmp/byte_tokenizer
/tmp/byte_tokenizer "LLM tiếng Việt"
```
