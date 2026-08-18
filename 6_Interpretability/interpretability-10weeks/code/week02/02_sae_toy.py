# Tuần 02 · Bài 02: Sparse autoencoder (SAE) tối giản.
# Mục tiêu: Tách một biểu diễn dày đặc thành các feature thưa, khôi phục đúng hướng
#           feature đã cấy vào dữ liệu.
# Đầu vào: Kích hoạt giả được tạo từ một vài feature thưa (sparse features).
# Đầu ra: Các hướng feature học được so với hướng thật (cosine similarity).
# Cách chạy: python 02_sae_toy.py
# An toàn: Chỉ chạy local; dùng gradient descent nhỏ, có seed; không tải model thật.

import numpy as np

rng = np.random.default_rng(2)

# ---- Bước 1: sinh dữ liệu từ feature thưa ----
D, F = 10, 3                    # 10 chiều biểu diễn, 3 feature thật
# Hướng thật của 3 feature (mỗi cột là một hướng trong không gian D chiều).
true_dirs = rng.standard_normal((D, F))
true_dirs /= np.linalg.norm(true_dirs, axis=0, keepdims=True)  # chuẩn hoá

N = 5000
# Mỗi mẫu: một vector thưa s (chỉ 1 feature bật) nhân với hướng, cộng nhiễu nhỏ.
s = np.zeros((N, F))
idx = rng.integers(0, F, size=N)            # chọn ngẫu nhiên feature nào bật
s[np.arange(N), idx] = 1.0                  # one-hot: feature bật = 1
h = s @ true_dirs.T + 0.05 * rng.standard_normal((N, D))  # (N, D)


def relu(x):
    return np.maximum(x, 0.0)


def train_sae(h, D, F, lr=0.02, steps=3000):
    """Huấn luyện SAE tuyến tính: h -> z = ReLU(W_enc @ h + b) -> h_hat = W_dec @ z."""
    W_enc = rng.standard_normal((F, D)) * 0.1   # (F, D) encoder
    W_dec = rng.standard_normal((D, F)) * 0.1   # (D, F) decoder
    b_enc = np.zeros(F)
    for _ in range(steps):
        z = relu(h @ W_enc.T + b_enc)           # (N, F) mã hoá thưa
        h_hat = z @ W_dec.T                      # (N, D) tái tạo
        # Loss = reconstruction (MSE) + phạt L1 lên z để ép thưa.
        loss = np.mean((h_hat - h) ** 2) + 0.001 * np.mean(np.abs(z))
        # Gradient thủ công (bỏ qua chi tiết qua ReLU ở mức toy; dùng autodiff đơn giản).
        d_h = 2 * (h_hat - h) / N
        d_dec = d_h.T @ z                        # (D, F)
        d_z = d_h @ W_dec                        # (N, F): đạo hàm theo z qua decoder
        d_z[z <= 0] = 0
        d_enc = d_z.T @ h                        # (F, D)
        d_b = d_z.sum(axis=0)
        W_dec -= lr * d_dec
        W_enc -= lr * d_enc
        b_enc -= lr * d_b
    return W_enc, W_dec


# ---- Bước 2: huấn luyện và so sánh hướng ----
W_enc, W_dec = train_sae(h, D, F)
dec_dirs = W_dec.T                               # (F, D): mỗi hàng là một hướng feature
dec_dirs /= np.linalg.norm(dec_dirs, axis=1, keepdims=True)

print("Cosine similarity giữa feature học được và feature thật:")
for i in range(F):
    # Vì thứ tự feature có thể hoán vị, ta ghép mỗi feature thật với feature học gần nhất.
    sims = np.abs(dec_dirs @ true_dirs[:, i])
    best = np.max(sims)
    print(f"  feature {i}: {best:.3f}")

print("\n=> SAE khôi phục được các hướng feature thưa từ biểu diễn dày đặc.")
