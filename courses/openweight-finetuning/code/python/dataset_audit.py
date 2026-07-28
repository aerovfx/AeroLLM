"""Audit dataset JSONL trước SFT; không gửi dữ liệu ra mạng."""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path


def canonical_hash(record: dict) -> str:
    raw = json.dumps(record, ensure_ascii=False, sort_keys=True).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def validate(record: dict, line_number: int) -> list[str]:
    errors = []
    messages = record.get("messages")
    if not isinstance(messages, list) or not messages:
        return [f"line {line_number}: messages must be a non-empty list"]
    roles = [message.get("role") for message in messages if isinstance(message, dict)]
    if len(roles) != len(messages) or roles[-1] != "assistant" or "user" not in roles:
        errors.append(f"line {line_number}: invalid role sequence")
    if not record.get("source") or not record.get("license"):
        errors.append(f"line {line_number}: missing source/license")
    for index, message in enumerate(messages):
        if not isinstance(message.get("content"), str) or not message["content"].strip():
            errors.append(f"line {line_number}: empty content at message {index}")
    return errors


def audit(path: Path) -> dict:
    hashes, errors, role_patterns = set(), [], Counter()
    rows = duplicates = 0
    with path.open(encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, 1):
            if not line.strip():
                continue
            rows += 1
            try:
                record = json.loads(line)
            except json.JSONDecodeError as exc:
                errors.append(f"line {line_number}: invalid JSON: {exc.msg}")
                continue
            errors.extend(validate(record, line_number))
            fingerprint = canonical_hash(record)
            duplicates += fingerprint in hashes
            hashes.add(fingerprint)
            if isinstance(record.get("messages"), list):
                role_patterns[tuple(m.get("role") for m in record["messages"])] += 1
    return {"rows": rows, "exact_duplicates": duplicates,
            "errors": errors[:20], "role_patterns": {str(k): v for k, v in role_patterns.items()}}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("dataset", type=Path, help="JSONL with messages/source/license")
    args = parser.parse_args()
    report = audit(args.dataset)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    raise SystemExit(1 if report["errors"] else 0)


if __name__ == "__main__":
    main()
