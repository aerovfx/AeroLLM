# Tuần 02 · Bài 01: Sparse probing (hồi quy logistic + phạt L1).
# Mục tiêu: Tìm một "mạch" nhỏ — tập neuron tối thiểu đủ để phân loại — bằng cách ép
#           phần lớn hệ số hồi quy về 0 nhờ phạt L1.
# Đầu vào: Kích hoạt giả (N mẫu x K neuron), trong đó chỉ vài neuron mang tín hiệu thật.
# Đầu ra: Danh sách neuron "sống sót" (hệ số != 0) và độ chính xác.
# Cách chạy: python 01_sparse_probe.py
# An toàn: Chỉ chạy local trên dữ liệu giả; ghi seed; cảnh báo statistical suppression.

import numpy as np

rng = np.random.default_rng(1)

# ---- Bước 1: sinh dữ liệu ----
N, K = 300, 200                  # 300 mẫu, 200 neuron
TRUE_NEURONS = [5, 17, 42]       # ba neuron thật sự mang tín hiệu
X = rng.standard_normal((N, K))  # kích hoạt nền nhiễu

# Tín hiệu: nhãn được quyết định bởi tổ hợp tuyến tính của 3 neuron thật.
logit_true = 3.0 * X[:, TRUE_NEURONS[0]] - 2.0 * X[:, TRUE_NEURONS[1]] + 2.5 * X[:, TRUE_NEURONS[2]]
p = 1.0 / (1.0 + np.exp(-logit_true))      # xác suất qua sigmoid
y = (rng.random(N) < p).astype(float)      # nhãn nhị phân {0,1}


def sigmoid(z):
    # Giới hạn z để tránh tràn số exp.
    z = np.clip(z, -50, 50)
    return 1.0 / (1.0 + np.exp(-z))


def l1_logistic(X, y, lam=0.3, lr=0.05, steps=3000):
    """Hồi quy logistic phạt L1 bằng proximal gradient descent (soft-thresholding)."""
    N, K = X.shape
    w = np.zeros(K)                          # khởi tạo hệ số bằng 0
    b = 0.0
    for _ in range(steps):
        z = X @ w + b
        grad_w = (X.T @ (sigmoid(z) - y)) / N   # gradient của BCE theo w
        grad_b = np.sum(sigmoid(z) - y) / N     # gradient theo bias
        w = w - lr * grad_w
        b = b - lr * grad_b
        # Soft-thresholding: ép các hệ số nhỏ về đúng 0 (đây chính là hiệu ứng L1).
        w = np.sign(w) * np.maximum(np.abs(w) - lr * lam, 0.0)
    return w, b


def accuracy(w, b, X, y):
    pred = (sigmoid(X @ w + b) >= 0.5).astype(float)
    return float(np.mean(pred == y))


# ---- Bước 2: huấn luyện sparse probe ----
w, b = l1_logistic(X, y, lam=0.3)
surviving = np.where(np.abs(w) > 1e-6)[0]   # neuron có hệ số khác 0
acc = accuracy(w, b, X, y)

print("Neuron sống sót (chỉ số):", surviving.tolist())
print("Neuron thật đã cấy     :", TRUE_NEURONS)
print("Số neuron sống / tổng   :", len(surviving), "/", K)
print("Độ chính xác            :", round(acc, 4))

# ---- Bước 3: nhận xét ----
# Phạt L1 giữ lại vài neuron trùng (hoặc gần) với neuron thật, phần còn lại bị ép về 0.
# Lưu ý: trên dữ liệu nhỏ, tín hiệu yếu có thể bị ép về 0 nhầm (statistical suppression).
print("\n=> Mạch tối thiểu tìm được gồm vài neuron; tăng lam sẽ làm mạch càng thưa.")
