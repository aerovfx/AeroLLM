# Tuần 04 · Bài 01: Activation maximization (cực đại hoá kích hoạt neuron).
# Mục tiêu: Tìm đầu vào khiến một neuron cụ thể "bật" mạnh nhất bằng gradient ascent,
#           và thấy đầu vào đó hội tụ về đặc trưng neuron thích.
# Đầu vào: Mạng nhỏ 2 lớp (input -> hidden -> neuron) với trọng số cố định.
# Đầu ra: Đầu vào tối ưu và độ tương đồng cosine của nó với đặc trưng thật.
# Cách chạy: python 01_activation_maximization.py
# An toàn: Chỉ chạy local trên mạng giả; ghi learning rate; cảnh báo hội tụ về nhiễu.

import numpy as np

rng = np.random.default_rng(5)
D_IN, D_HID = 8, 16

# ---- Bước 1: xây mạng ----
# W1 (D_IN -> D_HID), W2 (D_HID -> 1): neuron đơn lẻ cần khảo sát.
W1 = rng.standard_normal((D_IN, D_HID)) * 0.5
feature = rng.standard_normal(D_IN)          # đặc trưng mà neuron "thích"
feature /= np.linalg.norm(feature)
# Cột neuron được nối với đặc trưng feature qua W1, W2 để nó thật sự nhạy với feature.
W2 = rng.standard_normal(D_HID) * 0.1
W2[0] = 2.0                                  # neuron đọc mạnh một nơ-ron ẩn
W1[:, 0] = feature                            # nơ-ron ẩn đó nhạy với feature


def activation(x):
    """Kích hoạt của neuron mục tiêu (không cần phi tuyến ở lớp ra)."""
    hid = np.tanh(x @ W1)
    return float(hid @ W2)


# ---- Bước 2: gradient ascent trên đầu vào ----
def grad_ascent(lr=0.1, steps=400):
    x = rng.standard_normal(D_IN)             # khởi tạo ngẫu nhiên
    for _ in range(steps):
        # Đạo hàm: d(activation)/dx qua tanh.
        hid = np.tanh(x @ W1)
        d_hid = W2                               # d(act)/d(hid)
        d_tanh = 1.0 - hid ** 2                  # d(tanh)/d(pre-act)
        grad = (d_hid * d_tanh) @ W1.T           # d(act)/dx
        x = x + lr * grad
        x = x / (np.linalg.norm(x) + 1e-8)       # giữ norm ổn định, tránh bùng nổ
    return x


x_opt = grad_ascent()
sim = float(x_opt.dot(feature) / (np.linalg.norm(x_opt) * np.linalg.norm(feature)))

print("Đầu vào tối ưu (chuẩn hoá):", np.round(x_opt, 3))
print("Đặc trưng thật            :", np.round(feature, 3))
print("Cosine similarity với đặc trưng:", round(sim, 3))

# ---- Bước 3: nhận xét ----
# Đầu vào tối ưu xoay về hướng feature (cos gần 1): gradient ascent "tiết lộ" điều neuron thích.
# Trên LLM thật, tối ưu trực tiếp hay ra nhiễu, nên người ta thường kết hợp data sampling.
print("\n=> Activation maximization tiết lộ đặc trưng neuron thích, nhưng dễ kẹt ở nhiễu.")
