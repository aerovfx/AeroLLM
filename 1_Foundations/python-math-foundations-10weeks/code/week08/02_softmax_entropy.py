# Tuần 08 · Bài 02: Softmax, entropy và cross-entropy.
# Mục tiêu: Cài đặt softmax ổn định số; tính entropy và cross-entropy.
# Đầu vào: Vector logits giả và phân phối xác suất giả.
# Đầu ra: Phân phối softmax (tổng = 1), entropy, cross-entropy.
# Cách chạy: python code/week08/02_softmax_entropy.py
# Lưu ý an toàn: Trừ max trước khi lấy mũ; thêm epsilon tránh log(0).

# Import NumPy với bí danh np.
import numpy as np


def softmax(z):
    """Trả về phân phối xác suất từ vector logits z, tổng các phần tử = 1.

    Trừ max(z) để ổn định số: tránh e^z tràn (overflow) khi z lớn.
    """
    z = z - np.max(z)      # Dịch logits để giá trị lớn nhất thành 0.
    e = np.exp(z)          # Lấy mũ từng phần tử.
    return e / e.sum()     # Chuẩn hoá để tổng bằng 1.


def entropy(p):
    """Tính entropy H(p) = -sum(p_i * log(p_i)) với epsilon tránh log(0)."""
    eps = 1e-12            # Số dương rất nhỏ, tránh log(0).
    return -np.sum(p * np.log(p + eps))


def cross_entropy(p, q):
    """Tính cross-entropy H(p, q) = -sum(p_i * log(q_i))."""
    eps = 1e-12
    return -np.sum(p * np.log(q + eps))


def main():
    # Softmax biến logits thành phân phối xác suất.
    logits = np.array([2.0, 1.0, 0.0])
    probs = softmax(logits)
    print("Softmax:", np.round(probs, 4))
    print("Tổng xác suất:", round(probs.sum(), 6))  # Bằng 1.

    # Entropy: phân phối đều -> entropy lớn; phân phối chắc chắn -> nhỏ.
    uniform = np.array([1 / 3, 1 / 3, 1 / 3])
    certain = np.array([1.0, 0.0, 0.0])
    print("\nEntropy (đều):", round(entropy(uniform), 4))
    print("Entropy (chắc chắn):", round(entropy(certain), 4))

    # Cross-entropy giữa nhãn one-hot và xác suất dự đoán.
    y_true = np.array([1.0, 0.0, 0.0])       # Nhãn đúng: lớp 0.
    y_pred = softmax(np.array([1.5, 0.2, 0.1]))  # Dự đoán của model.
    print("Cross-entropy:", round(cross_entropy(y_true, y_pred), 4))


if __name__ == "__main__":
    main()
