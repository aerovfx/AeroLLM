# Tuần 10 · Bài 02: Forward/backward bằng autograd của PyTorch.
# Mục tiêu: Huấn luyện hồi quy tuyến tính y = 3x + 1 bằng gradient descent.
# Đầu vào: Dữ liệu giả (x, y) theo quan hệ y = 3x + 1.
# Đầu ra: Tham số w, b hội tụ về ~3 và ~1; loss giảm dần.
# Cách chạy: python code/week10/02_linear_regression_pytorch.py
# Lưu ý an toàn: Chạy trên CPU; dữ liệu giả; ghi seed để tái lập.

# Import PyTorch với bí danh torch.
import torch

# Cố định seed để kết quả tái lập được giữa các lần chạy.
torch.manual_seed(0)


def main():
    # Dữ liệu giả: y = 3x + 1 (khớp đúng quan hệ tuyến tính).
    x = torch.tensor([[1.0], [2.0], [3.0], [4.0]])
    y = torch.tensor([[4.0], [7.0], [10.0], [13.0]])

    # Tham số cần học; requires_grad=True để autograd tính đạo hàm.
    w = torch.tensor([[0.0]], requires_grad=True)
    b = torch.tensor([0.0], requires_grad=True)

    eta = 0.01   # Learning rate.
    epochs = 300

    # Vòng lặp huấn luyện: forward -> loss -> backward -> cập nhật.
    for epoch in range(epochs):
        # Forward pass: dự đoán tuyến tính y_hat = x @ w + b.
        y_hat = x @ w + b

        # Loss MSE: trung bình bình phương sai số.
        loss = ((y_hat - y) ** 2).mean()

        # Backward pass: tính gradient của loss theo w và b.
        loss.backward()

        # Cập nhật tham số trong no_grad để không tính đạo hàm cho bước cập nhật.
        with torch.no_grad():
            w -= eta * w.grad   # Cập nhật trọng số.
            b -= eta * b.grad   # Cập nhật bias.

        # Xoá gradient để bước sau không cộng dồn gradient cũ.
        w.grad.zero_()
        b.grad.zero_()

        # In loss mỗi 50 epoch để thấy xu hướng giảm.
        if epoch % 50 == 0:
            print(f"epoch {epoch:3d} | loss = {loss.item():.5f}")

    # In tham số cuối cùng, kỳ vọng w ~ 3 và b ~ 1.
    print("\nw =", round(w.item(), 3), "(kỳ vọng ~3)")
    print("b =", round(b.item(), 3), "(kỳ vọng ~1)")


if __name__ == "__main__":
    main()
