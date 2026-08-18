# Tuần 07 · Bài 01: Metric retrieval (recall@k, precision@k, MRR, nDCG).
# Mục tiêu: Đo chất lượng xếp hạng của retriever bằng metric chuẩn.
# Đầu vào: Danh sách kết quả xếp hạng và tập nguồn đúng cho từng câu hỏi.
# Đầu ra: recall@k, precision@k, MRR, nDCG trung bình.
# Cách chạy: python 01_retrieval_metrics.py
# Lưu ý an toàn: Metric retrieval chỉ đo xếp hạng, không đo tính đúng của câu trả lời.

import math


def recall_at_k(retrieved, relevant, k):
    """Tỷ lệ nguồn đúng xuất hiện trong k kết quả đầu."""
    if not relevant:
        return 1.0  # Không có nguồn đúng -> định nghĩa tránh chia 0.
    top = retrieved[:k]
    return len(set(top) & set(relevant)) / len(relevant)


def precision_at_k(retrieved, relevant, k):
    """Tỷ lệ kết quả đầu là nguồn đúng."""
    if k <= 0:
        return 0.0
    top = retrieved[:k]
    return len(set(top) & set(relevant)) / k


def reciprocal_rank(retrieved, relevant):
    """1 / hạng của nguồn đúng đầu tiên; 0 nếu không tìm thấy."""
    for i, doc in enumerate(retrieved, start=1):
        if doc in relevant:
            return 1.0 / i
    return 0.0


def dcg_at_k(retrieved, relevant, k):
    """Discounted Cumulative Gain: nguồn đúng ở vị trí đầu được trọng số cao."""
    retrieved = list(retrieved)  # Chấp nhận list hoặc set.
    gain = 0.0
    for i, doc in enumerate(retrieved[:k], start=1):
        if doc in relevant:
            gain += 1.0 / math.log2(i + 1)  # giảm dần theo vị trí.
    return gain


def ndcg_at_k(retrieved, relevant, k):
    """nDCG: dcg thực tế / dcg lý tưởng (mọi nguồn đúng nằm đầu)."""
    ideal = dcg_at_k(list(relevant), relevant, k)
    if ideal == 0:
        return 0.0
    return dcg_at_k(retrieved, relevant, k) / ideal


def main():
    # Mỗi câu hỏi có danh sách kết quả (retrieved) và tập nguồn đúng (relevant).
    cases = [
        {"retrieved": ["d1", "d2", "d3"], "relevant": {"d1"}},
        {"retrieved": ["d3", "d1", "d2"], "relevant": {"d1", "d2"}},
        {"retrieved": ["d4", "d5", "d6"], "relevant": {"d1"}},
    ]
    k = 3
    recall = sum(recall_at_k(c["retrieved"], c["relevant"], k) for c in cases) / len(cases)
    precision = sum(precision_at_k(c["retrieved"], c["relevant"], k) for c in cases) / len(cases)
    mrr = sum(reciprocal_rank(c["retrieved"], c["relevant"]) for c in cases) / len(cases)
    ndcg = sum(ndcg_at_k(c["retrieved"], c["relevant"], k) for c in cases) / len(cases)

    print(f"recall@{k} = {recall:.3f}")
    print(f"precision@{k} = {precision:.3f}")
    print(f"MRR = {mrr:.3f}")
    print(f"nDCG@{k} = {ndcg:.3f}")


if __name__ == "__main__":
    main()
