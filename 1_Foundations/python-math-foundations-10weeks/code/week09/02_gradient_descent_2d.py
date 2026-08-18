# Tuần 09 · Bài 02: Gradient descent hai chiều (2D) và dynamic learning rate.
# Mục tiêu: Cài đặt GD cho f(x, y) = x^2 + y^2, so sánh LR cố định và động.
# Đầu vào: Điểm khởi tạo (x, y), learning rate ban đầu, số epoch.
# Đầu ra: Điểm hội tụ (gần gốc toạ độ) cho hai cách chọn learning rate.
# Cách chạy: python code/week09/02_gradient_descent_2d.py
# Lưu ý an toàn: Chỉ tính toán trên hàm toán giả; giới hạn số epoch.


def f(x, y):
    """Hàm hai biến f(x, y) = x^2 + y^2, cực tiểu tại (0, 0)."""
    return x * x + y * y


def grad(x, y):
    """Trả về gradient (đạo hàm riêng) theo x và y: (2x, 2y)."""
    return 2 * x, 2 * y


def gd_2d(x, y, eta0, epochs, dynamic=False):
    """Chạy GD 2D, trả về (x, y) cuối và danh sách giá trị hàm f theo epoch.

    dynamic=True dùng learning rate giảm dần eta = eta0 / (1 + t/10).
    Hệ số /10 làm LR giảm từ từ để không chậm lại quá sớm.
    """
    losses = []
    # Lặp t từ 0 đến epochs-1 để tính learning rate động.
    for t in range(epochs):
        eta = eta0 / (1 + t / 10) if dynamic else eta0  # Chọn LR theo chế độ.
        gx, gy = grad(x, y)     # Tính gradient tại điểm hiện tại.
        x = x - eta * gx        # Cập nhật x ngược hướng gradient.
        y = y - eta * gy        # Cập nhật y ngược hướng gradient.
        losses.append(f(x, y))  # Lưu giá trị hàm để theo dõi hội tụ.
    return x, y, losses


def main():
    epochs = 50

    # Learning rate cố định.
    x1, y1, _ = gd_2d(3.0, 4.0, 0.1, epochs, dynamic=False)
    print("LR cố định -> x =", round(x1, 5), ", y =", round(y1, 5))

    # Learning rate động (giảm dần theo epoch, bước lớn lúc đầu nhỏ dần).
    x2, y2, losses = gd_2d(3.0, 4.0, 0.4, epochs, dynamic=True)
    print("LR động    -> x =", round(x2, 5), ", y =", round(y2, 5))

    # In vài giá trị loss để thấy xu hướng giảm dần.
    print("Loss động (epoch 0, 10, 30, 49):",
          round(losses[0], 4), round(losses[10], 4),
          round(losses[30], 4), round(losses[49], 4))


if __name__ == "__main__":
    main()
