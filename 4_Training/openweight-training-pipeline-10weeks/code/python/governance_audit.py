"""Ví dụ policy-as-code cho source manifest JSONL."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ALLOWED_LICENSES = {"mit", "apache-2.0", "cc-by-4.0", "public-domain"}


def release_gate(record: dict) -> list[str]:
    failures = []
    if str(record.get("license", "")).lower() not in ALLOWED_LICENSES:
        failures.append("license")
    if record.get("pii_class") not in {"none", "reviewed"}:
        failures.append("pii")
    if not record.get("source_id") or not record.get("content_sha256"):
        failures.append("lineage")
    return failures


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("manifest", type=Path)
    args = parser.parse_args()
    blocked = []
    with args.manifest.open(encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, 1):
            record = json.loads(line)
            failures = release_gate(record)
            if failures:
                blocked.append({"line": line_number, "failed_gates": failures})
    print(json.dumps({"release": not blocked, "blocked": blocked}, indent=2))
    raise SystemExit(1 if blocked else 0)


if __name__ == "__main__":
    main()
