# Tuần 05 · Bài 01: Effective dimensionality (số chiều hiệu quả) theo tầng.
# Mục tiêu: Đo xem biểu diễn ở mỗi tầng "nằm gọn" trong bao nhiêu chiều, dùng phổ PCA.
# Đầu vào: Biểu diễn giả của các token qua 5 tầng (ma trận mẫu x chiều).
# Đầu ra: Số chiều hiệu quả (participation ratio) mỗi tầng.
# Cách chạy: python 01_effective_dimensionality.py
# An toàn: Chỉ chạy local; xử lý giá trị riêng âm/nhiễu; seed cố định.

import numpy as np

rng = np.random.default_rng(7)
D = 20          # chiều biểu diễn
M = 500         # số mẫu (vector token) mỗi tầng
LAYERS = 5


def participation_ratio(X):
    """Số chiều hiệu quả = (tổng phương sai)^2 / tổng bình phương phương sai.
       Giá trị cao nghĩa là biểu diễn trải rộng trên nhiều chiều."""
    Xc = X - X.mean(axis=0)
    cov = (Xc.T @ Xc) / len(Xc)               # ma trận hiệp phương sai
    eigvals = np.linalg.eigvalsh(cov)         # giá trị riêng (tăng dần)
    eigvals = eigvals[eigvals > 1e-10]        # bỏ nhiễu số âm/rất nhỏ
    return float(eigvals.sum() ** 2 / (eigvals ** 2).sum())


print("Số chiều hiệu quả theo tầng:")
# Tầng 0: nhiễu trắng -> trải đều, chiều hiệu quả cao (gần D).
# Các tầng sau: thêm một hướng chính ngày càng mạnh -> biểu diễn "co" về ít chiều.
signal_dir = rng.standard_normal(D)
signal_dir /= np.linalg.norm(signal_dir)
for layer in range(LAYERS):
    strength = layer * 2.0                      # tín hiệu mạnh dần theo tầng
    X = rng.standard_normal((M, D)) + strength * np.outer(rng.standard_normal(M), signal_dir)
    pr = participation_ratio(X)
    print(f"  Layer {layer}: {pr:.2f} / {D}")

print("\n=> Càng sâu, biểu diễn càng nén về ít chiều chính (chiều hiệu quả giảm).")
