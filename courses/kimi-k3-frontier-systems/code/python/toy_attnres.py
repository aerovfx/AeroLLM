"""Toy full Attention Residuals: attention trên các biểu diễn theo chiều sâu."""

import numpy as np


def rms_norm(x: np.ndarray, eps: float = 1e-6) -> np.ndarray:
    """RMS-normalize vector cuối để magnitude không chi phối attention."""
    # Mean square được tính trên hidden dimension cuối cùng.
    return x / np.sqrt(np.mean(np.square(x), axis=-1, keepdims=True) + eps)


def attention_residual(sources: np.ndarray, pseudo_query: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Trộn embedding/layer outputs bằng learned pseudo-query."""
    # Mỗi row của sources là một depth source; RMSNorm tạo keys ổn định hơn.
    keys = rms_norm(sources)
    # Dot product cho một logit trên mỗi source trong chiều sâu.
    logits = keys @ pseudo_query
    # Softmax biến logits thành trọng số tổng bằng 1.
    stable_logits = logits - np.max(logits)
    weights = np.exp(stable_logits) / np.exp(stable_logits).sum()
    # Values là sources gốc, đúng tinh thần Eq. (8–9) trong report.
    mixed = (weights[:, None] * sources).sum(axis=0)
    return mixed, weights


def main() -> None:
    rng = np.random.default_rng(11)
    # Bốn source mô phỏng embedding và ba block outputs, hidden size 8.
    sources = rng.normal(size=(4, 8))
    pseudo_query = rng.normal(size=8)
    mixed, weights = attention_residual(sources, pseudo_query)
    # Hai invariant quan trọng: đúng hidden shape và weights được chuẩn hoá.
    assert mixed.shape == (8,)
    assert np.isclose(weights.sum(), 1.0, atol=1e-6)
    print("depth weights:", weights)
    print("mixed representation:", mixed)


if __name__ == "__main__":
    main()
