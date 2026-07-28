# Code lab — Kimi K3 ideas at toy scale

[Trang khoá học](../INDEX.md)

Các script chỉ minh hoạ nguyên lý; chúng không phải implementation Kimi K3 và không tải weights.

| File | Tuần | Mục tiêu | Thiết bị |
|---|---:|---|---|
| [`model_scale_estimator.py`](python/model_scale_estimator.py) | 1 | Ước lượng lower bound bộ nhớ weights | CPU |
| [`toy_kda.py`](python/toy_kda.py) | 2 | Delta recurrence và lower-bounded decay | CPU + NumPy |
| [`toy_attnres.py`](python/toy_attnres.py) | 3 | Attention trên chiều sâu | CPU + NumPy |
| [`quantile_balancing.py`](python/quantile_balancing.py) | 4 | So Top-k với Quantile Balancing | CPU + NumPy |
| [`agent_verifier.py`](python/agent_verifier.py) | 8 | Reward theo trạng thái cuối, budget và hidden test | CPU |
| [`preserved_history_payload.py`](python/preserved_history_payload.py) | 9 | Tạo multi-turn payload mà không làm mất reasoning/tool state | CPU, offline |
| [`architecture_labs.ipynb`](notebooks/architecture_labs.ipynb) | 2–4 | Notebook hướng dẫn chạy các toy lab | Jupyter/Colab |

```bash
# Chạy từ repository root để import và đường dẫn nhất quán.
python courses/kimi-k3-frontier-systems/code/python/model_scale_estimator.py
python courses/kimi-k3-frontier-systems/code/python/toy_kda.py
python courses/kimi-k3-frontier-systems/code/python/toy_attnres.py
python courses/kimi-k3-frontier-systems/code/python/quantile_balancing.py
python courses/kimi-k3-frontier-systems/code/python/agent_verifier.py
python courses/kimi-k3-frontier-systems/code/python/preserved_history_payload.py
```

Mỗi file có comment theo từng bước và assertion để học viên thấy giả định nào đang được kiểm tra.
