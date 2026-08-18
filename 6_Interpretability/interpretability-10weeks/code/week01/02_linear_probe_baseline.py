# Tuần 01 · Bài 02: Linear probe và baseline — vì sao mô hình tuyến tính "dễ hiểu" hơn.
# Mục tiêu: So sánh một mô hình tuyến tính (diễn giải được) với một mô hình phi tuyến
#           (hộp đen) bằng cách học một "probe" hồi quy tuyến tính trên cả hai.
# Đầu vào: Dữ liệu giả y = f(x) + nhiễu, sinh có seed.
# Đầu ra: Hệ số học được và R^2 của probe trên mỗi mô hình.
# Cách chạy: python 02_linear_probe_baseline.py
# An toàn: Chỉ chạy local; không tải dữ liệu/mô hình thật; seed cố định.

import numpy as np

rng = np.random.default_rng(0)

# ---- Bước 1: sinh dữ liệu ----
n = 200
x = np.linspace(-3, 3, n)

# Mô hình A (tuyến tính): y = 2.5*x + 1.0. Hệ số 2.5 mang nghĩa trực tiếp.
# Mô hình B (phi tuyến): y = sin(3*x). Không có một hệ số đơn nào "giải thích" được nó.
noise = rng.standard_normal(n) * 0.3
y_linear = 2.5 * x + 1.0 + noise
y_nonlinear = np.sin(3 * x) + noise


def fit_linear_probe(X, y):
    """Hồi quy tuyến tính dạng y = w * x + b bằng nghiệm bình phương tối thiểu (closed form)."""
    A = np.column_stack([X, np.ones_like(X)])   # thêm cột bias
    w, b = np.linalg.lstsq(A, y, rcond=None)[0]  # giải A @ [w, b] = y
    y_hat = w * X + b
    ss_res = np.sum((y - y_hat) ** 2)           # tổng bình phương phần dư
    ss_tot = np.sum((y - y.mean()) ** 2)        # tổng bình phương toàn phần
    r2 = 1 - ss_res / ss_tot                    # hệ số xác định
    return w, b, r2


# ---- Bước 2: fit probe lên cả hai mô hình ----
w1, b1, r2_1 = fit_linear_probe(x, y_linear)
w2, b2, r2_2 = fit_linear_probe(x, y_nonlinear)

print("Mô hình tuyến tính: hệ số học được w =", round(w1, 3),
      "(thật = 2.5), R^2 =", round(r2_1, 3))
print("Mô hình phi tuyến  : hệ số học được w =", round(w2, 3),
      "(không có ý nghĩa), R^2 =", round(r2_2, 3))

# ---- Bước 3: nhận xét ----
# Probe tuyến tính khớp tốt mô hình A và hệ số w xấp xỉ hệ số thật -> "diễn giải được".
# Với mô hình B, probe tuyến tính không khớp (R^2 thấp) vì quan hệ là phi tuyến.
# Đây chính là trực giác cốt lõi: diễn giải cơ chế khó vì mạng là một hàm phi tuyến xếp chồng.
print("\n=> Mô hình tuyến tính có thể tóm bằng một hệ số; hộp đen phi tuyến thì không.")
