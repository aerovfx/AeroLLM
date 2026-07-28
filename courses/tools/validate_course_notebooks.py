"""Kiểm tra schema và chạy tuần tự code cells khi Jupyter/nbclient không có sẵn."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
NOTEBOOKS = sorted((ROOT / "courses").glob("*/code/notebooks/*.ipynb"))


for notebook_path in NOTEBOOKS:
    document = json.loads(notebook_path.read_text(encoding="utf-8"))
    assert document["nbformat"] == 4
    assert isinstance(document.get("cells"), list) and document["cells"]
    namespace = {"__name__": "__notebook__"}
    code_cells = 0
    for cell_index, cell in enumerate(document["cells"]):
        assert cell["cell_type"] in {"markdown", "code"}
        if cell["cell_type"] != "code":
            continue
        code_cells += 1
        source = "".join(cell["source"])
        exec(compile(source, f"{notebook_path}:cell-{cell_index}", "exec"), namespace)
    print(f"PASS {notebook_path.relative_to(ROOT)} ({code_cells} code cells)")
