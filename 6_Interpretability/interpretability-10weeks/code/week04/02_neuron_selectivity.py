# Tuần 04 · Bài 02: Tính chọn lọc neuron — logistic regression vs t-test.
# Mục tiêu: Đo xem một neuron có phản ứng khác biệt giữa hai nhóm mẫu không, bằng hai công cụ
#           thống kê trả lời hai câu hỏi khác nhau.
# Đầu vào: Kích hoạt giả của một neuron trên hai nhóm (A: danh từ riêng, B: khác).
# Đầu ra: Hệ số logistic, accuracy, và t-test (t, p-value).
# Cách chạy: python 02_neuron_selectivity.py
# An toàn: Chỉ chạy local; p-value thấp không đồng nghĩa quan trọng nhân quả.

import numpy as np

rng = np.random.default_rng(6)
n = 200

# ---- Bước 1: sinh kích hoạt ----
# Nhóm A (nhãn 1): neuron kích hoạt mạnh hơn. Nhóm B (nhãn 0): kích hoạt yếu hơn.
a = rng.normal(loc=3.0, scale=1.0, size=n)   # nhóm A
b = rng.normal(loc=1.0, scale=1.0, size=n)   # nhóm B
X = np.concatenate([a, b])
y = np.concatenate([np.ones(n), np.zeros(n)])


def sigmoid(z):
    z = np.clip(z, -50, 50)
    return 1.0 / (1.0 + np.exp(-z))


def logistic_fit(X, y, lr=0.1, steps=2000):
    """Hồi quy logistic đơn biến: p(y=1|x) = sigmoid(w*x + b)."""
    w, b = 0.0, 0.0
    for _ in range(steps):
        z = w * X + b
        grad_w = np.mean((sigmoid(z) - y) * X)
        grad_b = np.mean(sigmoid(z) - y)
        w -= lr * grad_w
        b -= lr * grad_b
    return w, b


def t_test(group_a, group_b):
    """Kiểm định t hai mẫu độc lập (phương sai không bằng nhau — Welch)."""
    ma, mb = group_a.mean(), group_b.mean()
    va, vb = group_a.var(ddof=1), group_b.var(ddof=1)
    na, nb = len(group_a), len(group_b)
    se = np.sqrt(va / na + vb / nb)
    t = (ma - mb) / se
    # p-value hai phía dùng xấp xỉ chuẩn (hợp lệ vì n lớn).
    from statistics import NormalDist
    p = 2 * (1 - NormalDist().cdf(abs(t)))
    return t, p


# ---- Bước 2: chạy hai công cụ ----
w_coef, bias = logistic_fit(X, y)          # lưu ý: không ghi đè mảng `a`, `b` ở trên
pred = (sigmoid(w_coef * X + bias) >= 0.5).astype(float)
acc = float(np.mean(pred == y))
t_stat, p = t_test(a, b)

print("Logistic regression: w =", round(w_coef, 3), "| accuracy =", round(acc, 3))
print("t-test             : t =", round(t_stat, 3), "| p-value =", round(p, 6))

# ---- Bước 3: nhận xét ----
# Logistic cho biết neuron phân tách nhóm tốt đến đâu (accuracy).
# t-test cho biết khác biệt trung bình có ý nghĩa thống kê không (p-value).
# Cả hai "đồng ý" khi tín hiệu mạnh; khi nhiễu lớn, chúng có thể bất đồng.
print("\n=> Logistic đo năng lực phân tách; t-test đo ý nghĩa thống kê của khác biệt trung bình.")
