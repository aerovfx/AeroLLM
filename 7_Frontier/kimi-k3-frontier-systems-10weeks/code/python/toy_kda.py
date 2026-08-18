"""Toy KDA recurrence theo Eq. (1) và lower-bounded decay theo Eq. (5)."""

import numpy as np


def bounded_decay(logit: np.ndarray, g_min: float = -5.0) -> np.ndarray:
    """Ánh xạ decay logit sang retention alpha nằm trong (exp(g_min), 1)."""
    # Sigmoid giới hạn giá trị trong (0, 1); nhân g_min âm tạo log-decay trong (g_min, 0).
    log_decay = g_min / (1.0 + np.exp(-logit))
    # Exponential chuyển log-decay thành retention factor dương.
    return np.exp(log_decay)


def kda_step(state: np.ndarray, q: np.ndarray, k: np.ndarray,
             value: np.ndarray, alpha: np.ndarray,
             beta: float) -> tuple[np.ndarray, np.ndarray]:
    """Cập nhật state ma trận và đọc output cho một token, một head."""
    # Diag(alpha) làm quên độc lập theo từng channel của key.
    decayed_state = np.diag(alpha) @ state
    # Ma trận (I - beta * k k^T) áp dụng delta-rule correction.
    correction = np.eye(k.size) - beta * np.outer(k, k)
    # outer(k, value) ghi cặp key–value mới vào recurrent state.
    new_state = correction @ decayed_state + beta * np.outer(k, value)
    # Report dùng S_t^T q_t để đọc output sau khi đã ghi token hiện tại.
    output = new_state.T @ q
    return new_state, output


def main() -> None:
    # Seed cố định giúp lab tái lập được.
    rng = np.random.default_rng(7)
    # Toy head có key dimension 4 và value dimension 3.
    state = np.zeros((4, 3))
    q_raw, k_raw = rng.normal(size=4), rng.normal(size=4)
    q, k = q_raw / np.linalg.norm(q_raw), k_raw / np.linalg.norm(k_raw)
    value = rng.normal(size=3)
    alpha = bounded_decay(rng.normal(size=4))
    beta = float(1.0 / (1.0 + np.exp(-rng.normal())))
    new_state, output = kda_step(state, q, k, value, alpha, beta)
    # Assertion bắt lỗi shape trước khi học viên mở rộng sang chuỗi nhiều token.
    assert new_state.shape == (4, 3) and output.shape == (3,)
    # Lower bound là tính chất cần kiểm chứng của parameterization.
    assert np.all(alpha > np.exp(-5.0)) and np.all(alpha < 1)
    print("alpha:", alpha)
    print("output:", output)


if __name__ == "__main__":
    main()
