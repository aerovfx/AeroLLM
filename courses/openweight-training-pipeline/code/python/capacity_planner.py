"""Capacity planner đơn giản cho training; dùng estimate để quyết định, không làm SLA."""

from __future__ import annotations

import argparse
import json


def estimate(params_b: float, tokens_b: float, gpus: int, peak_tflops: float,
             mfu: float, checkpoint_gib: float, free_disk_gib: float) -> dict:
    flops = 6 * params_b * 1e9 * tokens_b * 1e9
    days = flops / (gpus * peak_tflops * 1e12 * mfu) / 86400
    # Giữ tối thiểu ba checkpoint và 25% biên cho log/cache/temp files.
    required_disk = 3 * checkpoint_gib * 1.25
    return {"estimated_flops": flops, "idealized_days": round(days, 2),
            "required_disk_gib": round(required_disk, 1),
            "disk_gate": free_disk_gib >= required_disk}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--params-b", type=float, default=1.0)
    parser.add_argument("--tokens-b", type=float, default=1.0)
    parser.add_argument("--gpus", type=int, default=1)
    parser.add_argument("--peak-tflops", type=float, default=100.0)
    parser.add_argument("--mfu", type=float, default=0.35)
    parser.add_argument("--checkpoint-gib", type=float, default=8.0)
    parser.add_argument("--free-disk-gib", type=float, default=50.0)
    args = parser.parse_args()
    if not (0 < args.mfu <= 1) or args.gpus < 1:
        raise SystemExit("mfu phải thuộc (0,1] và gpus >= 1")
    print(json.dumps(estimate(**vars(args)), indent=2))


if __name__ == "__main__":
    main()
