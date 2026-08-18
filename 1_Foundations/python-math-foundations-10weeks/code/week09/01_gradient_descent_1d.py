# Tuần 09 · Bài 01: Gradient descent một chiều (1D).
# Mục tiêu: Cài đặt GD cho f(x) = (x - 0.5)^2, so sánh learning rate.
# Đầu vào: Điểm khởi tạo x, learning rate eta, số epoch.
# Đầu ra: Giá trị x hội tụ và cảnh báo phân kỳ khi learning rate lớn.
# Cách chạy: python code/week09/01_gradient_descent_1d.py
# Lưu ý an toàn: Giới hạn số epoch và phát hiện NaN/inf để dừng sớm.

# Import math để kiểm tra giá trị hữu hạn.
import math


def f(x):
    """Hàm mất mát f(x) = (x - 0.5)^2, cực tiểu tại x = 0.5."""
    return (x - 0.5) ** 2


def df(x):
    """Đạo hàm f'(x) = 2*(x - 0.5)."""
    return 2 * (x - 0.5)


def gradient_descent_1d(x_start, eta, epochs):
    """Chạy GD 1D, trả về (x cuối, lịch sử x, có phân kỳ không)."""
    x = x_start
    history = [x]  # Lưu giá trị x ban đầu để theo dõi hội tụ.
    # Lặp đúng số epoch; mỗi vòng cập nhật x ngược hướng đạo hàm.
    for _ in range(epochs):
        x = x - eta * df(x)
        history.append(x)
        # Dừng sớm nếu giá trị không hữu hạn (NaN/inf) hoặc bùng nổ quá ngưỡng.
        # Ngưỡng 1e6 giúp phát hiện phân kỳ (giá trị tiến ra vô cùng) trước khi tràn số.
        if not math.isfinite(x) or abs(x) > 1e6:
            return x, history, True
    return x, history, False


def main():
    epochs = 30

    # Learning rate vừa phải: hội tụ về 0.5.
    x_ok, _, diverged = gradient_descent_1d(2.0, 0.1, epochs)
    print("eta=0.1 -> x =", round(x_ok, 5), "(kỳ vọng ~0.5)")

    # Learning rate quá lớn: nhảy quá đà và phân kỳ.
    x_big, _, diverged = gradient_descent_1d(2.0, 1.5, epochs)
    print("eta=1.5 -> x =", x_big, "| phân kỳ:", diverged)

    # Learning rate quá nhỏ: hội tụ chậm, cần nhiều epoch hơn.
    x_small, _, _ = gradient_descent_1d(2.0, 0.001, epochs)
    print("eta=0.001 -> x =", round(x_small, 5), "(còn xa 0.5 sau", epochs, "epoch)")


if __name__ == "__main__":
    main()
