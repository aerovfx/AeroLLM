# Tuần 01 · Bài 02: Softmax ổn định, log-prob và perplexity.
# Mục tiêu: Hiểu cách tính log-likelihood/perplexity và vì sao cần softmax ổn định số.
# Đầu vào: Vector logit giả và danh sách xác suất giả.
# Đầu ra: Phân phối softmax (tổng = 1), NLL và perplexity.
# Cách chạy: python 02_calibration.py
# Lưu ý an toàn: Chỉ là minh hoạ toán học; không dùng perplexity làm "điểm thông minh".

import math


def softmax_stable(logits):
    """Softmax ổn định số: trừ max trước khi exp để tránh tràn số.

    Nếu logit lớn (vd 1000), exp(1000) tràn float; trừ max giữ exp <= 1.
    """
    m = max(logits)                 # Tìm max để dịch chuyển toàn bộ logit.
    exps = [math.exp(z - m) for z in logits]
    total = sum(exps)
    if total == 0:                  # Phòng thủ: không để chia cho 0.
        n = len(logits)
        return [1.0 / n] * n        # Phân phối đều khi mọi giá trị âm vô cùng.
    return [e / total for e in exps]


def nll_and_perplexity(probs):
    """Tính negative log-likelihood trung bình và perplexity.

    probs là xác suất mô hình gán cho token đúng tại mỗi vị trí.
    """
    # Lọc các xác suất hợp lệ để tránh log(0) hoặc log(âm).
    probs = [p for p in probs if 0 < p <= 1]
    if not probs:
        return 0.0, 1.0
    nll = -sum(math.log(p) for p in probs) / len(probs)
    return nll, math.exp(nll)


def main():
    # Softmax ổn định so với softmax ngây thơ khi logit lớn.
    logits_big = [1000.0, 1001.0, 1002.0]
    probs = softmax_stable(logits_big)
    print("softmax(stable) của logit lớn:", [round(p, 4) for p in probs])
    print("Tổng phân phối:", round(sum(probs), 10))  # phải bằng 1.

    # Perplexity: xác suất đúng càng cao -> perplexity càng thấp.
    good = [0.9, 0.8, 0.85]   # mô hình tự tin đúng.
    bad = [0.2, 0.1, 0.15]    # mô hình phân vân nhiều.
    for name, ps in [("tự tin", good), ("phân vân", bad)]:
        nll, ppl = nll_and_perplexity(ps)
        print(f"{name}: NLL={nll:.3f}, PPL={ppl:.3f}")

    # Lưu ý: perplexity phụ thuộc đơn vị token; không so sánh chéo tokenizer.


if __name__ == "__main__":
    main()
