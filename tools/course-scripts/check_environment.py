"""Kiểm tra môi trường học tập mà không thay đổi máy tính."""

from __future__ import annotations

import importlib.util
import os
import platform
import shutil
import sys


def gib(value: int) -> float:
    """Đổi byte sang GiB."""
    return round(value / 2**30, 1)


print("Python:", sys.version.split()[0])
print("OS:", platform.platform())
print("Architecture:", platform.machine())
print("CPU cores:", os.cpu_count())
disk = shutil.disk_usage(os.getcwd())
print("Disk free (GiB):", gib(disk.free))
print("C++ compiler:", shutil.which("clang++") or shutil.which("g++") or "not found")
print("Jupyter package:", "available" if importlib.util.find_spec("jupyter") else "not found")

if importlib.util.find_spec("torch"):
    import torch

    print("PyTorch:", torch.__version__)
    print("CUDA available:", torch.cuda.is_available())
    if torch.cuda.is_available():
        print("GPU:", torch.cuda.get_device_name(0))
        print("GPU VRAM (GiB):", gib(torch.cuda.get_device_properties(0).total_memory))
    print("MPS available:", bool(getattr(torch.backends, "mps", None) and torch.backends.mps.is_available()))
else:
    print("PyTorch: not found")

print("\nĐọc courses/COMPUTER_REQUIREMENTS.md trước khi chọn model hoặc chạy training.")
