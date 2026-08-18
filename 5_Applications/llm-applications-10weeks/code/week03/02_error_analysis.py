# Tuần 03 · Bài 02: Bootstrap confidence interval và error buckets.
# Mục tiêu: Ước lượng khoảng tin cậy 95% cho accuracy và nhóm lỗi theo nguyên nhân.
# Đầu vào: Danh sách dự đoán đúng/sai (dữ liệu giả).
# Đầu ra: CI bootstrap và bảng error bucket.
# Cách chạy: python 02_error_analysis.py
# Lưu ý an toàn: Bootstrap chỉ ước lượng phương sai lấy mẫu, không bù dữ liệu lệch.

import random
import statistics


def bootstrap_ci(correct_flags, n_iter=1000, seed=9):
    """Tính khoảng tin cậy 95% của accuracy bằng bootstrap.

    Mỗi lần lặp lấy mẫu có hoàn lại rồi tính accuracy; lấy phân vị 2.5/97.5.
    """
    rng = random.Random(seed)
    n = len(correct_flags)
    if n == 0:
        return (0.0, 0.0)
    accs = []
    for _ in range(n_iter):
        # choices() có hoàn lại -> mô phỏng phân phối lấy mẫu.
        sample = [rng.choice(correct_flags) for _ in range(n)]
        accs.append(sum(sample) / n)
    lo = sorted(accs)[int(0.025 * n_iter)]
    hi = sorted(accs)[int(0.975 * n_iter)]
    return (lo, hi)


def error_buckets(predictions):
    """Nhóm lỗi theo category. Mỗi prediction có 'label','pred','category'.

    Chỉ nhóm các mẫu sai; trả Counter theo category.
    """
    from collections import Counter
    buckets = Counter()
    for p in predictions:
        if p["pred"] != p["label"]:
            buckets[p["category"]] += 1
    return buckets


def main():
    random.seed(2)
    # Sinh 300 dự đoán giả; category 'a' khó hơn nên sai nhiều hơn.
    predictions = []
    for i in range(300):
        cat = "a" if random.random() < 0.5 else "b"
        # Mô phỏng model: đúng 80% với 'b', chỉ 60% với 'a'.
        correct = random.random() < (0.8 if cat == "b" else 0.6)
        label = random.randint(0, 1)
        pred = label if correct else 1 - label
        predictions.append({"label": label, "pred": pred, "category": cat})

    correct_flags = [1 if p["label"] == p["pred"] else 0 for p in predictions]
    acc = sum(correct_flags) / len(correct_flags)
    lo, hi = bootstrap_ci(correct_flags)
    print(f"Accuracy={acc:.3f}, 95% CI=[{lo:.3f}, {hi:.3f}]")

    buckets = error_buckets(predictions)
    print("Error buckets (theo category):", dict(buckets))
    # Từ bucket lớn nhất -> biết nên cải thiện dữ liệu/model cho nhóm nào.


if __name__ == "__main__":
    main()
