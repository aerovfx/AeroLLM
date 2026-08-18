# Tuần 08 · Bài 01: Bias và fairness metrics (demographic parity + counterfactual).
# Mục tiêu: Đo chênh lệch dự đoán giữa các nhóm và qua cặp prompt đối xứng.
# Đầu vào: Dữ liệu dự đoán giả theo nhóm; cặp prompt counterfactual.
# Đầu ra: Demographic parity difference và chênh lệch counterfactual.
# Cách chạy: python 01_bias_metrics.py
# Lưu ý an toàn: Dữ liệu giả; kết luận về nhóm người thật cần dữ liệu đại diện.

def demographic_parity(preds_by_group):
    """Tính chênh lệch tỷ lệ dự đoán dương giữa hai nhóm.

    preds_by_group: dict {group: list[0/1]}. Giá trị gần 0 = ít lệch.
    """
    rates = {}
    for group, preds in preds_by_group.items():
        if not preds:
            rates[group] = 0.0  # Nhóm không có dữ liệu -> không thể kết luận.
            continue
        rates[group] = sum(preds) / len(preds)
    groups = list(rates.keys())
    if len(groups) < 2:
        return 0.0, rates
    return abs(rates[groups[0]] - rates[groups[1]]), rates


def counterfactual_gap(pairs):
    """So sánh đầu ra của các cặp prompt chỉ khác thuộc tính nhạy cảm.

    pairs: list[(score_a, score_b)]. Trả chênh lệch trung bình tuyệt đối.
    """
    if not pairs:
        return 0.0
    return sum(abs(a - b) for a, b in pairs) / len(pairs)


def main():
    # Dữ liệu giả: nhóm A được dự đoán dương nhiều hơn nhóm B.
    preds = {"A": [1, 1, 1, 0, 1], "B": [0, 1, 0, 0, 1]}
    diff, rates = demographic_parity(preds)
    print("Tỷ lệ dự đoán dương:", rates)
    print("Demographic parity difference:", round(diff, 3))

    # Cặp counterfactual giả: (điểm mô hình cho "he", cho "she").
    pairs = [(0.8, 0.5), (0.7, 0.6), (0.9, 0.4)]
    gap = counterfactual_gap(pairs)
    print("Counterfactual gap trung bình:", round(gap, 3))


if __name__ == "__main__":
    main()
