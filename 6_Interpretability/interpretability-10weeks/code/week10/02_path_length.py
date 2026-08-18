# Tuần 10 · Bài 02: Path length của residual stream.
# Mục tiêu: Đo tổng quãng đường vector residual đi qua các tầng, so sánh token "đúng" và
#           token "bất thường" để thấy token nào bị mô hình xử lý nhiều hơn.
# Đầu vào: Quỹ đạo residual giả của các token qua nhiều tầng.
# Đầu ra: Path length (tổng độ dài từng bước cập nhật) của mỗi token.
# Cách chạy: python 02_path_length.py
# An toàn: Chỉ chạy local; path length là một đại lượng vô hướng tổng hợp, dễ mất thông tin.

import numpy as np

rng = np.random.default_rng(18)
D, L = 10, 6


def residual_path(kind):
    """Sinh chuỗi h_0..h_L cho một token; trả về (L+1, D)."""
    h = [0.1 * rng.standard_normal(D)]
    if kind == "normal":
        step_dir = rng.standard_normal(D); step_dir /= np.linalg.norm(step_dir)
        for _ in range(L):
            h.append(h[-1] + 0.5 * step_dir + 0.05 * rng.standard_normal(D))
    else:  # "surprising": mỗi bước đổi hướng nhiều -> quãng đường dài hơn
        for _ in range(L):
            h.append(h[-1] + rng.standard_normal(D))
    return np.array(h)


def path_length(h):
    """Tổng độ dài Euclidean giữa các bước liên tiếp."""
    steps = np.diff(h, axis=0)
    return float(np.linalg.norm(steps, axis=1).sum())


print("Path length theo loại token:")
lengths = {}
for kind in ["normal", "surprising"]:
    total = 0.0
    for _ in range(20):                      # trung bình qua 20 câu
        total += path_length(residual_path(kind))
    lengths[kind] = total / 20
    print(f"  {kind:10s}: {lengths[kind]:.2f}")

# ---- Nhận xét ----
# Token bất thường ("surprising") có path length lớn hơn: mô hình phải "xoay xở" nhiều hơn.
# Path length tổng hợp toàn bộ quỹ đạo thành một con số, nên dễ mất chi tiết hướng chuyển động.
print("\n=> Path length lớn gợi ý token bị xử lý nhiều, nhưng không nói rõ xử lý theo hướng nào.")
