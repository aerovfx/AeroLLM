"""Sinh ba notebook tutorial bằng schema nbformat v4, chỉ dùng Python standard library."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def markdown(text: str) -> dict:
    return {"cell_type": "markdown", "metadata": {}, "source": text.splitlines(keepends=True)}


def code(text: str) -> dict:
    return {"cell_type": "code", "execution_count": None, "metadata": {},
            "outputs": [], "source": text.splitlines(keepends=True)}


def notebook(cells: list[dict]) -> dict:
    return {
        "cells": cells,
        "metadata": {"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
                     "language_info": {"name": "python", "version": "3"}},
        "nbformat": 4,
        "nbformat_minor": 5,
    }


NOTEBOOKS = {
    "courses/llm-from-scratch/code/notebooks/mini_gpt_walkthrough.ipynb": notebook([
        markdown("# Mini-GPT Walkthrough\n\n## Goal / Mục tiêu\nQuan sát tokenizer, next-token batch và một training step nhỏ, chạy được trên CPU."),
        markdown("## Setup / Chuẩn bị\nNotebook chỉ cần PyTorch. Seed cố định giúp kết quả tái lập gần đúng."),
        code("import random\nimport torch\n\nSEED = 3407\nrandom.seed(SEED)\ntorch.manual_seed(SEED)\nprint({'torch': torch.__version__, 'device': 'cpu'})\n"),
        markdown("## Steps / Các bước\n### 1. Tokenize và tạo next-token pairs"),
        code("text = 'học máy từ dữ liệu. ' * 8\nvocab = sorted(set(text))\nstoi = {char: index for index, char in enumerate(vocab)}\nitos = {index: char for char, index in stoi.items()}\ntokens = torch.tensor([stoi[char] for char in text])\nblock_size = 8\nx = tokens[:block_size][None, :]\ny = tokens[1:block_size + 1][None, :]\nprint({'vocab': len(vocab), 'x_shape': tuple(x.shape), 'x': x.tolist(), 'y': y.tolist()})\n"),
        markdown("### 2. Train một bigram neural baseline"),
        code("model = torch.nn.Embedding(len(vocab), len(vocab))\noptimizer = torch.optim.AdamW(model.parameters(), lr=0.05)\nlosses = []\nfor _ in range(40):\n    logits = model(x)\n    loss = torch.nn.functional.cross_entropy(logits.flatten(0, 1), y.flatten())\n    optimizer.zero_grad(set_to_none=True)\n    loss.backward()\n    optimizer.step()\n    losses.append(loss.item())\nprint({'initial_loss': round(losses[0], 4), 'final_loss': round(losses[-1], 4)})\n"),
        markdown("## Checks / Kiểm tra"),
        code("assert x.shape == y.shape == (1, block_size)\nassert losses[-1] < losses[0]\nassert ''.join(itos[i] for i in tokens[:5].tolist()) == text[:5]\nprint('PASS')\n"),
        markdown("## Next Steps / Bước tiếp\nThay bigram Embedding bằng `MiniGPT` trong `../python/mini_gpt_lab.py`; so sánh parameter count và validation loss."),
    ]),
    "courses/openweight-finetuning/code/notebooks/qlora_planning_lab.ipynb": notebook([
        markdown("# QLoRA Planning Lab\n\n## Goal / Mục tiêu\nLập data/model/VRAM plan trước khi mở notebook Unsloth có GPU."),
        markdown("## Setup / Chuẩn bị\nKhông tải model và không cần GPU; mọi con số là estimate cần xác minh bằng profiler."),
        code("from collections import Counter\n\nMODEL_B = 3.0\nBITS = 4\nWIDTH = 3072\nRANK = 16\nTARGET_MODULES = 64\n"),
        markdown("## Steps / Các bước\n### 1. Audit một dataset hội thoại mẫu"),
        code("records = [\n    {'messages': [{'role': 'user', 'content': 'Tóm tắt văn bản'}, {'role': 'assistant', 'content': 'Bản tóm tắt'}], 'source': 'demo', 'license': 'mit'},\n    {'messages': [{'role': 'user', 'content': 'Phân loại rủi ro'}, {'role': 'assistant', 'content': 'low'}], 'source': 'demo', 'license': 'mit'},\n]\npatterns = Counter(tuple(message['role'] for message in row['messages']) for row in records)\nassert all(row['messages'][-1]['role'] == 'assistant' for row in records)\nprint({'rows': len(records), 'role_patterns': dict(patterns)})\n"),
        markdown("### 2. Ước lượng weight-only memory và LoRA parameters"),
        code("weight_gib = MODEL_B * 1e9 * BITS / 8 / 2**30\nlora_parameters = TARGET_MODULES * 2 * WIDTH * RANK\nprint({'weight_only_gib': round(weight_gib, 2), 'lora_parameters': lora_parameters})\n"),
        markdown("## Checks / Kiểm tra"),
        code("assert weight_gib > 0\nassert lora_parameters < MODEL_B * 1e9\nassert set(patterns) == {('user', 'assistant')}\nprint('PASS — tiếp theo phải cộng activation/KV/optimizer/runtime overhead.')\n"),
        markdown("## Next Steps / Bước tiếp\nChọn model/revision và notebook hiện hành từ tài liệu Unsloth; chạy smoke test 20–60 step trước full run."),
    ]),
    "courses/openweight-training-pipeline/code/notebooks/training_pipeline_lab.ipynb": notebook([
        markdown("# Open-Weight Training Pipeline Lab\n\n## Goal / Mục tiêu\nThực hành capacity plan và release gates mà không cần job nhiều GPU."),
        markdown("## Setup / Chuẩn bị\nCác giả định được đặt ở một cell; thay đổi chúng để tạo hai kịch bản."),
        code("PARAMS_B = 1.0\nTOKENS_B = 0.2\nGPUS = 1\nPEAK_TFLOPS = 100.0\nMFU = 0.35\nFREE_DISK_GIB = 80.0\nCHECKPOINT_GIB = 8.0\n"),
        markdown("## Steps / Các bước\n### 1. Capacity estimate"),
        code("flops = 6 * PARAMS_B * 1e9 * TOKENS_B * 1e9\ndays = flops / (GPUS * PEAK_TFLOPS * 1e12 * MFU) / 86400\nrequired_disk = 3 * CHECKPOINT_GIB * 1.25\ncapacity = {'idealized_days': round(days, 2), 'required_disk_gib': required_disk, 'disk_gate': FREE_DISK_GIB >= required_disk}\nprint(capacity)\n"),
        markdown("### 2. Governance gates"),
        code("sources = [\n    {'source_id': 'vi-001', 'license': 'mit', 'pii_class': 'none', 'sha256': 'a' * 64},\n    {'source_id': 'vi-002', 'license': 'unknown', 'pii_class': 'possible', 'sha256': 'b' * 64},\n]\nallowed = {'mit', 'apache-2.0', 'cc-by-4.0', 'public-domain'}\nblocked = [row['source_id'] for row in sources if row['license'] not in allowed or row['pii_class'] not in {'none', 'reviewed'}]\nprint({'blocked_sources': blocked})\n"),
        markdown("## Checks / Kiểm tra"),
        code("assert capacity['disk_gate']\nassert blocked == ['vi-002']\nassert all(len(row['sha256']) == 64 for row in sources)\nprint('PASS')\n"),
        markdown("## Next Steps / Bước tiếp\nLập hai kịch bản GPU/token khác nhau, thêm safety/evaluation gates và viết go/no-go memo."),
    ]),
}


for relative_path, content in NOTEBOOKS.items():
    output_path = ROOT / relative_path
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(content, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(output_path)
