# Tuần 01 · Bài 01: Metric phân loại và bẫy class imbalance.
# Mục tiêu: Hiểu accuracy/precision/recall/F1 và vì sao accuracy gây hiểu lầm khi dữ liệu lệch.
# Đầu vào: Tập nhãn thật và nhãn dự đoán (dữ liệu giả, sinh có seed).
# Đầu ra: Confusion matrix, accuracy, precision/recall/F1 và baseline đa số.
# Cách chạy: python 01_metrics.py
# Lưu ý an toàn: Chỉ chạy local trên dữ liệu giả; không liên quan dữ liệu thật.

import random


def confusion_matrix(y_true, y_pred):
    """Đếm TP/TN/FP/FN cho bài toán nhị phân (nhãn 0/1).

    Trả về dict để dễ đọc; tránh dùng chỉ số lồng nhau gây nhầm.
    """
    tp = tn = fp = fn = 0
    # Duyệt từng cặp nhãn; zip dừng ở chuỗi ngắn hơn để tránh lỗi độ dài lệch.
    for t, p in zip(y_true, y_pred):
        if t == 1 and p == 1:
            tp += 1
        elif t == 0 and p == 0:
            tn += 1
        elif t == 0 and p == 1:
            fp += 1
        elif t == 1 and p == 0:
            fn += 1
    return {"TP": tp, "TN": tn, "FP": fp, "FN": fn}


def metrics(cm):
    """Tính accuracy, precision, recall, F1 từ confusion matrix.

    Xử lý chia cho 0: nếu mẫu số bằng 0 thì trả 0.0 (không crash).
    """
    tp, tn, fp, fn = cm["TP"], cm["TN"], cm["FP"], cm["FN"]
    total = tp + tn + fp + fn
    accuracy = (tp + tn) / total if total else 0.0
    precision = tp / (tp + fp) if (tp + fp) else 0.0
    recall = tp / (tp + fn) if (tp + fn) else 0.0
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) else 0.0
    return {"accuracy": accuracy, "precision": precision,
            "recall": recall, "f1": f1}


def main():
    # Seed cố định để kết quả tái lập được giữa các lần chạy.
    random.seed(42)
    n = 1000
    # Dữ liệu lệch nặng: 90% nhãn 0, 10% nhãn 1.
    y_true = [1 if random.random() < 0.10 else 0 for _ in range(n)]

    # Model A: đoán đúng 80% nhãn 0 nhưng chỉ đúng 20% nhãn 1.
    y_pred_a = []
    for t in y_true:
        if t == 0:
            y_pred_a.append(0 if random.random() < 0.80 else 1)
        else:
            y_pred_a.append(1 if random.random() < 0.20 else 0)

    # Model B (baseline đa số): luôn đoán 0.
    y_pred_b = [0] * n

    for name, y_pred in [("Model A", y_pred_a), ("Baseline đa số", y_pred_b)]:
        cm = confusion_matrix(y_true, y_pred)
        m = metrics(cm)
        print(f"{name}: accuracy={m['accuracy']:.3f} "
              f"precision={m['precision']:.3f} "
              f"recall={m['recall']:.3f} f1={m['f1']:.3f}")

    # Kết luận quan trọng: baseline đa số có accuracy ~90% dù không học gì,
    # nhưng recall với lớp 1 = 0 -> F1 = 0. Accuracy một mình là bẫy.


if __name__ == "__main__":
    main()
