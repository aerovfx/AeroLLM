# Tuần 07 · Bài 02: Bỏ qua một tầng (skip a layer).
# Mục tiêu: Đo tầng nào "quan trọng" bằng cách bỏ hẳn cập nhật của tầng đó và xem output
#           thay đổi bao nhiêu.
# Đầu vào: Mô hình giả L tầng, trong đó một tầng mang tín hiệu mạnh.
# Đầu ra: Độ lệch output khi bỏ từng tầng (so với baseline đầy đủ).
# Cách chạy: python 02_skip_layer.py
# An toàn: Chỉ chạy local; skip layer là can thiệp thô, chỉ đo mức "quan trọng" tương đối.

import numpy as np

rng = np.random.default_rng(12)
D, L = 8, 6
CRITICAL_LAYER = 4    # tầng được cấy để mang tín hiệu quyết định

W = [rng.standard_normal((D, D)) * 0.2 for _ in range(L)]
W[CRITICAL_LAYER] = rng.standard_normal((D, D)) * 3.0   # tầng quan trọng, trọng số lớn

x = rng.standard_normal(D)


def run(skip=None):
    """Chạy forward; nếu skip = k thì bỏ cập nhật của tầng k (nối residual thẳng)."""
    h = x.copy()
    for layer in range(L):
        if layer == skip:
            continue                                  # bỏ qua tầng này
        h = h + np.tanh(h @ W[layer])                 # residual + update
    return h


baseline = run()
print("Baseline đầy đủ norm =", round(np.linalg.norm(baseline), 3))
print("Độ lệch output khi bỏ từng tầng:")
for k in range(L):
    out = run(skip=k)
    drift = np.linalg.norm(out - baseline)
    print(f"  Bỏ tầng {k}: lệch = {drift:.3f}")

print("\n=> Bỏ tầng quan trọng (tầng 4) gây lệch lớn nhất; các tầng khác ít ảnh hưởng hơn.")
