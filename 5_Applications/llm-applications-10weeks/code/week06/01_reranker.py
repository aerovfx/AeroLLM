# Tuần 06 · Bài 01: Re-ranking (MMR + lexical rerank).
# Mục tiêu: Sắp xếp lại top-k để cân bằng độ liên quan và độ đa dạng.
# Đầu vào: Kết quả similarity (score, text) và query.
# Đầu ra: Thứ tự mới sau re-rank.
# Cách chạy: python 01_reranker.py
# Lưu ý an toàn: Re-rank chỉ đổi thứ tự, không kiểm chứng tính đúng của nội dung.

import math
import re


def tokenize(text):
    return set(re.findall(r"[a-z0-9]+", text.lower()))


def cosine(a, b):
    dot = sum(x * y for x, y in zip(a, b))
    na = math.sqrt(sum(x * x for x in a))
    nb = math.sqrt(sum(y * y for y in b))
    return dot / (na * nb) if na and nb else 0.0


def lexical_sim(a, b):
    """Độ tương đồng từ vựng bằng Jaccard (giao/hợp của tập từ)."""
    ta, tb = tokenize(a), tokenize(b)
    if not ta or not tb:
        return 0.0
    return len(ta & tb) / len(ta | tb)


def mmr(query, docs, lambda_param=0.5, top=3):
    """Maximum Marginal Relevance: chọn lặp lại đoạn tốt nhất.

    lambda_param cân bằng: 1 = chỉ relevance, 0 = chỉ diversity.
    docs là list (similarity_score, text) đã sắp giảm theo score.
    """
    remaining = list(docs)
    selected = []
    while remaining and len(selected) < top:
        best = None
        best_score = float("-inf")
        for i, (sim_q, text) in enumerate(remaining):
            # Phạt nếu text giống các đoạn đã chọn (giảm trùng lặp).
            redundancy = max([lexical_sim(text, s[1]) for s in selected],
                             default=0.0)
            score = lambda_param * sim_q - (1 - lambda_param) * redundancy
            if score > best_score:
                best_score = score
                best = i
        selected.append(remaining.pop(best))
    return selected


def main():
    query = "how to get a refund"
    # Top-4 thô theo similarity; chú ý có 3 đoạn gần trùng về refund.
    docs = [
        (0.90, "refund policy allows returns within 30 days"),
        (0.88, "returns are accepted within 30 days of purchase"),
        (0.86, "you can return items in the first month"),
        (0.50, "office hours are 9am to 6pm"),
    ]
    print("Trước re-rank (top 4):")
    for s, t in docs:
        print(f"  [{s}] {t}")

    print("\nSau MMR (lambda=0.5):")
    for s, t in mmr(query, docs, lambda_param=0.5, top=3):
        print(f"  [{s:.3f}] {t}")


if __name__ == "__main__":
    main()
