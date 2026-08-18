"""Minh hoạ Quantile Balancing (QB) từ Appendix C của Kimi K3 report."""

import numpy as np


def loads(assignments: np.ndarray, expert_count: int) -> np.ndarray:
    """Đếm số token được gán vào mỗi expert."""
    # bincount cần minlength để vẫn giữ expert có tải bằng 0.
    return np.bincount(assignments.ravel(), minlength=expert_count)


def quantile_balance(scores: np.ndarray, top_k: int, steps: int = 8) -> tuple[np.ndarray, np.ndarray]:
    """Alternating coordinate updates cho expert bias ở toy batch."""
    token_count, expert_count = scores.shape
    # Bài lab yêu cầu target load nguyên để kết quả dễ kiểm tra.
    assert (token_count * top_k) % expert_count == 0
    target = token_count * top_k // expert_count
    # beta là expert threshold trong Appendix C; routing dùng scores - beta.
    beta = np.zeros(expert_count)
    for _ in range(steps):
        # Sort giảm dần từng token và lấy phần tử thứ k+1 làm alpha cutoff.
        token_margins = np.sort(scores - beta[None, :], axis=1)[:, ::-1]
        alpha = token_margins[:, top_k]
        # Sort giảm dần từng expert; phần tử target+1 là coordinate minimizer.
        expert_margins = np.sort(scores - alpha[:, None], axis=0)[::-1, :]
        beta = expert_margins[target]
    # argsort giảm dần và lấy top_k expert sau khi trừ bias.
    assignments = np.argsort(scores - beta[None, :], axis=1)[:, ::-1][:, :top_k]
    return assignments, beta


def main() -> None:
    rng = np.random.default_rng(3)
    # Cộng bias lớn vào expert 0 để cố ý tạo routing mất cân bằng.
    scores = rng.normal(size=(128, 8))
    scores[:, 0] += 2.0
    plain = np.argsort(scores, axis=1)[:, ::-1][:, :2]
    balanced, beta = quantile_balance(scores, top_k=2)
    print("Top-k loads:", loads(plain, 8))
    print("QB loads:   ", loads(balanced, 8))
    print("Thresholds:", np.round(beta, 3))


if __name__ == "__main__":
    main()

