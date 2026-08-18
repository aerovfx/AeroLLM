# Tuần 06 · Bài 01: Các chế độ sửa kích hoạt (zero / mean / median / noise).
# Mục tiêu: So sánh tác động của các cách can thiệp khác nhau lên cùng một "neuron mạch".
# Đầu vào: Mô hình giả 2 lớp có một neuron ẩn quyết định nhãn A/B.
# Đầu ra: Logit difference (logit_A - logit_B) trước và sau mỗi phép sửa.
# Cách chạy: python 01_activation_editing.py
# An toàn: Chỉ chạy local trên mô hình giả; luôn so baseline sạch; seed cố định.

import numpy as np

rng = np.random.default_rng(9)
D, H = 6, 8
CIRCUIT_NEURON = 0          # neuron ẩn mang tín hiệu quyết định nhãn

# ---- Bước 1: mô hình giả ----
W1 = rng.standard_normal((D, H)) * 0.4
W1[:, CIRCUIT_NEURON] = rng.standard_normal(D) * 2.0   # neuron mạch nhạy với đầu vào
W2 = rng.standard_normal((H, 2)) * 0.3
W2[CIRCUIT_NEURON, 0] = 3.0     # neuron mạch đẩy mạnh logit nhãn A
W2[CIRCUIT_NEURON, 1] = -1.0


def forward(x, edit=None):
    """Tính logits. `edit` = hàm nhận hidden và trả hidden đã sửa (can thiệp)."""
    h = np.maximum(0.0, x @ W1)         # ReLU
    if edit is not None:
        h = edit(h)
    return h @ W2                       # logits 2 lớp


def logit_diff(logits):
    return float(logits[0] - logits[1])  # A - B


# ---- Bước 2: baseline và các phép sửa ----
# Tạo một batch đầu vào; lấy trung vị/trung bình của neuron mạch để dùng cho mean/median edit.
xs = rng.standard_normal((200, D))
hidden_all = np.maximum(0.0, xs @ W1)
mean_h = hidden_all.mean(axis=0)
median_h = np.median(hidden_all, axis=0)

x = rng.standard_normal(D)               # một mẫu để thí nghiệm
base = forward(x)
print("Baseline (sạch)  logit diff =", round(logit_diff(base), 3))

def edit_zero(h):
    h = h.copy(); h[CIRCUIT_NEURON] = 0.0; return h

def edit_mean(h):
    h = h.copy(); h[CIRCUIT_NEURON] = mean_h[CIRCUIT_NEURON]; return h

def edit_median(h):
    h = h.copy(); h[CIRCUIT_NEURON] = median_h[CIRCUIT_NEURON]; return h

def edit_noise(h):
    h = h.copy(); h[CIRCUIT_NEURON] += rng.standard_normal() * 2.0; return h

for name, fn in [("zero", edit_zero), ("mean", edit_mean),
                 ("median", edit_median), ("noise", edit_noise)]:
    out = forward(x, edit=fn)
    print(f"Edit {name:7s} -> logit diff = {logit_diff(out):+.3f}")

# ---- Bước 3: nhận xét ----
# zero/mean/median "tắt" neuron mạch khiến logit diff giảm mạnh (mất ưu thế nhãn A).
# noise làm nhiễu quanh baseline. So sánh các mức độ để thấy can thiệp nào "mạnh tay" nhất.
print("\n=> Mỗi chế độ sửa gây tác động khác nhau; cần baseline để đo độ lệch.")
