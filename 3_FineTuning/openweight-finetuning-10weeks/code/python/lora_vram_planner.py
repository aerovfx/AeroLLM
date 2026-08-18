"""Ước lượng sơ bộ weights và LoRA parameters; không thay thế profiler thực tế."""

from __future__ import annotations

import argparse


def weight_gib(parameters_billion: float, bits: int) -> float:
    return parameters_billion * 1e9 * bits / 8 / 2**30


def lora_parameters(width: int, rank: int, target_modules: int) -> int:
    # Với linear width→width: A(rank×width) + B(width×rank).
    return target_modules * 2 * width * rank


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--params-b", type=float, default=3.0)
    parser.add_argument("--bits", type=int, choices=(4, 8, 16), default=4)
    parser.add_argument("--width", type=int, default=3072)
    parser.add_argument("--rank", type=int, default=16)
    parser.add_argument("--target-modules", type=int, default=64)
    args = parser.parse_args()
    adapter = lora_parameters(args.width, args.rank, args.target_modules)
    print({"weight_only_gib": round(weight_gib(args.params_b, args.bits), 2),
           "lora_parameters": adapter,
           "warning": "Add activations, KV cache, gradients, optimizer and runtime overhead."})


if __name__ == "__main__":
    main()
