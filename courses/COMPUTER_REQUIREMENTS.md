# Yêu cầu cấu hình máy tính / Computer Requirements

[Danh mục khoá học](README.md)

## Cấu hình chung

| Mức | CPU | RAM | Lưu trữ trống | GPU/VRAM | Phù hợp |
|---|---|---:|---:|---|---|
| Tối thiểu | 4 core x86-64 hoặc Apple Silicon | 8 GB | 15 GB SSD | Không bắt buộc | Đọc code, tokenizer, tensor nhỏ, data audit |
| Khuyến nghị | 8 core | 16–32 GB | 50 GB SSD | NVIDIA 8–16 GB hoặc Apple Silicon 16 GB unified memory | Mini-GPT, notebook, QLoRA model nhỏ |
| Nâng cao | 16+ core | 64+ GB | 200 GB–2 TB NVMe | NVIDIA 24–80 GB | Model 7B/8B, context dài, experiment nhiều run |
| Lab phân tán | Server-class | 128+ GB | NVMe/shared storage theo capacity plan | 2–8 GPU, interconnect nhanh | DDP/FSDP, pipeline training, DeepSpec thu nhỏ |

Dung lượng thực tế phụ thuộc model, precision, sequence length, batch, optimizer và dataset. Luôn chạy preflight/capacity estimate trước khi tải hoặc train.

## Phần mềm

- Python 3.10–3.12; Git; môi trường ảo `venv`/Conda/uv.
- PyTorch tương thích thiết bị: CPU, CUDA hoặc MPS.
- JupyterLab/Notebook hoặc Google Colab cho `.ipynb`.
- C++17 compiler (`clang++` hoặc `g++`) chỉ cần cho ví dụ C++.
- Linux là lựa chọn ổn định nhất cho CUDA/distributed; Windows nên dùng WSL2 khi công cụ yêu cầu Linux.

## Theo từng khoá

### Xây LLM từ đầu

- Tuần 1–7: 8 GB RAM, CPU đủ cho examples và unit tests.
- Tuần 8–10: khuyến nghị GPU 8 GB; CPU/MPS vẫn chạy được với model nhỏ và ít iteration.
- Không yêu cầu chạy OpenWebText hay reproduce GPT-2 124M.

### Fine-tuning open-weight

- Dataset/chat-template labs: 8–16 GB RAM, không cần GPU.
- QLoRA model 1B–3B: thường cần khoảng 8–12 GB VRAM tuỳ context/batch/runtime.
- QLoRA 7B/8B: nên có 16–24 GB VRAM; xác nhận bằng notebook/model guide hiện hành.
- Nếu không có NVIDIA GPU, dùng Colab/Kaggle cho training; local vẫn làm data/evaluation labs.

### Pipeline training open-weight

- Governance/capacity/evaluation: laptop 16 GB RAM.
- CPT/SFT reduced run: GPU 16–24 GB trở lên.
- Distributed/DeepSpec: hạ tầng chuyên dụng. Không chạy cấu hình mặc định DeepSpec nếu chưa kiểm tra storage; target cache mặc định có thể cực lớn.

### Kimi K3: frontier architecture & agents

- Toy KDA/AttnRes/QB/verifier: CPU 4 core, RAM 8 GB, Python + NumPy; PyTorch chỉ cần khi mở rộng sang model trainable.
- Notebook/ablation model nhỏ: RAM 16 GB; GPU 8–16 GB là tuỳ chọn.
- API experiment: không cần GPU nhưng cần quota, cost cap và dữ liệu không nhạy cảm.
- Full Kimi K3: **không phải lab máy cá nhân**. Với 2.8T weights, lower bound lý thuyết đã khoảng 1.40 TB ở 4 bit, chưa gồm cache/runtime overhead; cần cluster và inference engine/hardware tương thích.

## Kiểm tra nhanh

```bash
python tools/course-scripts/check_environment.py
```

Script chỉ thu thập thông tin và đưa khuyến nghị; không cài package, tải model hoặc thay đổi hệ thống.
