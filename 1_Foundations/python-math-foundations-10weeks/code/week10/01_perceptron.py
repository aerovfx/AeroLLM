# Tuần 10 · Bài 01: Perceptron thủ công.
# Mục tiêu: Cài đặt perceptron (dot product + bias + ReLU) bằng NumPy.
# Đầu vào: Vector trọng số w, bias b, và một vài vector đầu vào giả.
# Đầu ra: Giá trị z (tổng có trọng số) và relu(z) cho từng đầu vào.
# Cách chạy: python code/week10/01_perceptron.py
# Lưu ý an toàn: Dữ liệu giả; không chứa trọng số model thật.

# Import NumPy với bí danh np.
import numpy as np


def perceptron(x, w, b):
    """Tính z = x·w + b rồi áp dụng ReLU: relu(z) = max(0, z).

    x: vector đầu vào; w: vector trọng số; b: bias (số vô hướng).
    """
    z = np.dot(x, w) + b   # Tổng có trọng số cộng bias.
    a = np.maximum(0, z)   # Hàm kích hoạt phi tuyến ReLU.
    return z, a


def main():
    # Trọng số và bias giả.
    w = np.array([0.5, -0.5])
    b = 0.2

    # Ba vector đầu vào giả để quan sát hiệu ứng của ReLU.
    inputs = [
        np.array([1.0, 1.0]),
        np.array([1.0, -1.0]),
        np.array([-1.0, -1.0]),
    ]

    # Duyệt từng đầu vào, tính z và a rồi in.
    for i, x in enumerate(inputs):
        z, a = perceptron(x, w, b)
        print(f"x{i + 1} = {x} -> z = {round(z, 3)}, relu(z) = {round(a, 3)}")

    # Giải thích phi tuyến: nếu bỏ ReLU, chồng nhiều tầng vẫn tuyến tính.
    print("\nReLU phá vỡ tính tuyến tính để model học ranh giới cong.")


if __name__ == "__main__":
    main()
