# Tuần 03 · Bài 02: Số ngẫu nhiên có seed với NumPy.
# Mục tiêu: Tạo dữ liệu giả ngẫu nhiên tái lập được bằng default_rng(seed).
# Đầu vào: Seed (42) và kích thước mẫu n.
# Đầu ra: Hai dãy số sinh từ cùng seed (giống nhau) và một dãy seed khác.
# Cách chạy: python code/week03/02_numpy_random.py
# Lưu ý an toàn: Số ngẫu nhiên này không dùng cho bảo mật (dùng secrets nếu cần).

# Import NumPy với bí danh np, dùng cho tính toán số.
import numpy as np


def make_normal_samples(seed, n):
    """Sinh n số theo phân phối chuẩn, dùng seed cố định để tái lập."""
    # default_rng(seed) tạo bộ sinh ngẫu nhiên độc lập, tái lập được.
    rng = np.random.default_rng(seed)
    # normal(size=n) trả về mảng n số phân phối chuẩn chuẩn (mean 0, std 1).
    return rng.normal(size=n)


def main():
    n = 5

    # Cùng seed -> cùng dãy số (tái lập).
    a = make_normal_samples(42, n)
    b = make_normal_samples(42, n)
    print("Seed 42 lần 1:", np.round(a, 4))
    print("Seed 42 lần 2:", np.round(b, 4))
    print("Hai dãy giống nhau:", np.array_equal(a, b))

    # Seed khác -> dãy khác.
    c = make_normal_samples(7, n)
    print("Seed 7       :", np.round(c, 4))

    # Thống kê mô tả: trung bình và độ lệch chuẩn của mẫu.
    print("Trung bình (seed 42):", round(a.mean(), 4))
    print("Độ lệch chuẩn (seed 42):", round(a.std(), 4))


if __name__ == "__main__":
    main()
