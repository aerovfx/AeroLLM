"""Template SFT an toàn: mặc định chỉ in kế hoạch, không tải hoặc train model."""

from __future__ import annotations

import argparse
import json


CONFIG = {
    "model_name": "CHOOSE_A_CURRENT_UNSLOTH_INSTRUCT_MODEL",
    "max_seq_length": 2048,
    "load_in_4bit": True,
    "lora_rank": 16,
    "learning_rate": 2e-4,
    "epochs": 1,
}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run", action="store_true", help="Cho phép đi vào phần training")
    args = parser.parse_args()
    print(json.dumps(CONFIG, indent=2))
    if not args.run:
        print("DRY RUN: chọn model/dataset hợp lệ rồi đọc docs Unsloth trước khi dùng --run.")
        return
    if CONFIG["model_name"].startswith("CHOOSE_"):
        raise SystemExit("Hãy pin model name/revision trước khi training.")
    try:
        import unsloth  # noqa: F401
    except ImportError as exc:
        raise SystemExit("Thiếu Unsloth. Cài theo tài liệu chính thức phù hợp CUDA/PyTorch.") from exc
    raise SystemExit("Starter gate: nối notebook chính thức sau khi data audit và baseline đạt.")


if __name__ == "__main__":
    main()
