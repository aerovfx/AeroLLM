# Tuần 09 · Bài 02: Subspace removal (loại bỏ không gian con).
# Mục tiêu: Loại bỏ một HƯỚNG trong không gian kích hoạt (thay vì từng neuron) và so sánh
#           tác động khi hướng đó mang tín hiệu ngữ nghĩa vs chỉ là nhiễu.
# Đầu vào: Kích hoạt giả (N x D) với một hướng "ngữ nghĩa" cấy sẵn.
# Đầu ra: Logit change khi loại bỏ hướng ngữ nghĩa vs hướng nhiễu.
# Cách chạy: python 02_subspace_removal.py
# An toàn: Chỉ chạy local; chiếu subspace bằng phép trừ hình chiếu; seed cố định.

import numpy as np

rng = np.random.default_rng(16)
N, D = 300, 20

# ---- Bước 1: dữ liệu và hướng ngữ nghĩa ----
u = rng.standard_normal(D); u /= np.linalg.norm(u)      # hướng ngữ nghĩa thật
noise_dir = rng.standard_normal(D); noise_dir /= np.linalg.norm(noise_dir)
# Kích hoạt = tín hiệu dọc theo u (mạnh) + nhiễu.
X = np.outer(rng.standard_normal(N), u) * 5.0 + 0.3 * rng.standard_normal((N, D))

# Readout: logit đọc mạnh theo hướng u (mô phỏng "mạch đọc" ngữ nghĩa).
readout = u * 10.0
def logit(X):
    return float((X @ readout).mean())

base = logit(X)
print(f"Baseline logit = {base:.2f}")


def remove_direction(X, direction):
    """Loại bỏ thành phần của X dọc theo `direction` (trừ hình chiếu)."""
    d = direction / (np.linalg.norm(direction) + 1e-12)
    return X - np.outer(X @ d, d)


# ---- Bước 2: loại bỏ hai hướng khác nhau ----
X_no_semantic = remove_direction(X, u)
X_no_noise = remove_direction(X, noise_dir)

print(f"Loại bỏ hướng NGỮ NGHĨA: logit change = {logit(X_no_semantic) - base:+.2f}")
print(f"Loại bỏ hướng NHIỄU     : logit change = {logit(X_no_noise) - base:+.2f}")

# ---- Bước 3: nhận xét ----
# Loại bỏ hướng ngữ nghĩa làm logit sụp đổ; loại bỏ hướng nhiễu gần như không đổi.
# Điều này minh hoạ vì sao can thiệp theo "hướng" chính xác hơn can thiệp theo neuron đơn lẻ
# khi thông tin được mã hoá dọc theo một subspace.
print("\n=> Loại bỏ đúng hướng mang thông tin có tác động lớn hơn nhiều so với hướng nhiễu.")
