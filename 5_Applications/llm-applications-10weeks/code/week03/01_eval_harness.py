# Tuần 03 · Bài 01: Eval harness tối giản với nhiều model giả.
# Mục tiêu: Tách dataset / model / metric thành ba tầng độc lập và so sánh baseline.
# Đầu vào: Dataset giả (input, label, category) và 3 model giả.
# Đầu ra: Accuracy của từng model qua cùng một harness.
# Cách chạy: python 01_eval_harness.py
# Lưu ý an toàn: Dữ liệu giả; harness không gọi mô hình thật hay mạng.

import random


def make_dataset(n=200, seed=11):
    """Sinh dataset phân loại giả: label 0/1, category 'a' hoặc 'b'.

    Quy tắc ẩn: category 'a' thiên về label 1 nhiều hơn 'b'.
    """
    rng = random.Random(seed)
    data = []
    for i in range(n):
        category = "a" if rng.random() < 0.5 else "b"
        # Xác suất label=1 phụ thuộc category để heuristic có tín hiệu thật.
        p1 = 0.7 if category == "a" else 0.3
        label = 1 if rng.random() < p1 else 0
        data.append({"input": i, "label": label, "category": category})
    return data


def model_random(item):
    """Baseline ngẫu nhiên: đoán 0/1 với xác suất 50/50."""
    return random.randint(0, 1)


def model_majority(item):
    """Baseline đa số: luôn đoán nhãn phổ biến nhất (giả định là 0)."""
    return 0


def model_heuristic(item):
    """Heuristic đơn giản: dùng category để đoán label.

    Không nhìn label thật; chỉ dùng đặc trưng input -> không rò rỉ đáp án.
    """
    return 1 if item["category"] == "a" else 0


def run_harness(dataset, model_fn):
    """Chạy model qua dataset, trả accuracy. Đây là tầng metric."""
    if not dataset:
        return 0.0
    correct = sum(1 for item in dataset if model_fn(item) == item["label"])
    return correct / len(dataset)


def main():
    random.seed(5)  # Seed cho model_random để tái lập.
    data = make_dataset()
    models = [("random", model_random),
              ("majority", model_majority),
              ("heuristic", model_heuristic)]
    for name, fn in models:
        acc = run_harness(data, fn)
        print(f"{name}: accuracy={acc:.3f}")


if __name__ == "__main__":
    main()
