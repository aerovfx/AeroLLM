# Tuần 08 · Bài 01: Tích vô hướng, tổ hợp tuyến tính và nhân ma trận.
# Mục tiêu: Tính dot product, tổ hợp tuyến tính có trọng số, nhân ma trận.
# Đầu vào: Các vector và ma trận giả khai báo trong code.
# Đầu ra: Kết quả từng phép toán.
# Cách chạy: python code/week08/01_vector_matrix.py
# Lưu ý an toàn: Chỉ tính toán trên dữ liệu giả; kiểm tra kích thước trước khi nhân.

# Import NumPy với bí danh np.
import numpy as np


def dot_product(x, w):
    """Tính tích vô hướng x·w = tổng x_i * w_i."""
    # np.dot tính tích vô hướng cho hai vector 1 chiều cùng độ dài.
    return np.dot(x, w)


def linear_combination(w1, w2, b, x1, x2):
    """Tính tổ hợp tuyến tính w1*x1 + w2*x2 + b."""
    return w1 * x1 + w2 * x2 + b


def main():
    # Hai vector cùng độ dài 2.
    x = np.array([1.0, 2.0])
    w = np.array([0.5, -0.5])

    # Tích vô hướng = 1*0.5 + 2*(-0.5) = -0.5.
    print("Tích vô hướng x·w =", dot_product(x, w))

    # Tổ hợp tuyến tính: 0.5*1 + (-0.5)*2 + 1.0 = 0.0.
    print("Tổ hợp tuyến tính =", linear_combination(0.5, -0.5, 1.0, 1.0, 2.0))

    # Nhân ma trận A(2x3) với B(3x2) -> kết quả 2x2.
    A = np.array([[1, 2, 3], [4, 5, 6]])   # shape (2, 3).
    B = np.array([[7, 8], [9, 10], [11, 12]])  # shape (3, 2).
    C = A @ B   # Toán tử @ là nhân ma trận trong Python 3.5+.
    print("\nA @ B =")
    print(C)

    # Kiểm tra quy tắc kích thước: in shape kết quả.
    print("shape của kết quả:", C.shape)  # (2, 2).

    # Thử nhân sai kích thước và bắt lỗi để quan sát thông báo.
    try:
        wrong = np.array([[1, 2]]) @ np.array([[1, 2]])
        print(wrong)
    except ValueError as e:
        print("\nLỗi kích thước ma trận:", e)


if __name__ == "__main__":
    main()
