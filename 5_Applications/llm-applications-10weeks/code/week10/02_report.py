# Tuần 10 · Bài 02: Tổng hợp metric và in báo cáo đánh giá.
# Mục tiêu: Gom các metric (retrieval + faithfulness) thành báo cáo tái lập được.
# Đầu vào: Kết quả giả định của pipeline trên golden set.
# Đầu ra: Bảng metric tổng hợp và vài mẫu lỗi.
# Cách chạy: python 02_report.py
# Lưu ý an toàn: Báo cáo phải tái lập được (seed + lệnh chạy), không trang trí số.

import math


def recall_at_k(retrieved, relevant, k):
    if not relevant:
        return 1.0
    return len(set(retrieved[:k]) & set(relevant)) / len(relevant)


def mrr(cases):
    """Mean Reciprocal Rank trên danh sách (retrieved, relevant)."""
    total = 0.0
    for retrieved, relevant in cases:
        for i, doc in enumerate(retrieved, start=1):
            if doc in relevant:
                total += 1.0 / i
                break
    return total / len(cases) if cases else 0.0


def faithfulness(answer, context):
    """Tỷ lệ claim được hỗ trợ (heuristic từ vựng, xem week07)."""
    import re
    claims = [p.strip() for p in re.split(r"[.;]", answer) if p.strip()]
    if not claims:
        return 0.0
    ctx_tokens = set(re.findall(r"[a-z0-9]+", context.lower()))
    ok = 0
    for c in claims:
        tokens = set(re.findall(r"[a-z0-9]+", c.lower())) - {"the", "a", "an", "is", "of", "to", "in"}
        if tokens and len(tokens & ctx_tokens) / len(tokens) >= 0.5:
            ok += 1
    return ok / len(claims)


def main():
    # Golden set giả: (retrieved, relevant, answer, context).
    golden = [
        (["d1", "d2", "d3"], {"d1"}, "Refunds are allowed within 30 days.",
         "Refund policy allows returns within 30 days of purchase."),
        (["d3", "d1", "d2"], {"d1", "d2"}, "Returns within 30 days and coverage after hire.",
         "Returns within 30 days. Coverage begins after hire."),
        (["d4", "d5", "d6"], {"d1"}, "No answer found.", ""),
    ]
    k = 3
    recall = sum(recall_at_k(r, rel, k) for r, rel, _, _ in golden) / len(golden)
    mr = mrr([(r, rel) for r, rel, _, _ in golden])
    faith = sum(faithfulness(ans, ctx) for _, _, ans, ctx in golden) / len(golden)

    print("=== Báo cáo đánh giá (golden set giả) ===")
    print(f"recall@{k} = {recall:.3f}")
    print(f"MRR = {mr:.3f}")
    print(f"faithfulness = {faith:.3f}")
    print("Mẫu lỗi: câu 3 không tìm thấy nguồn đúng (retrieval miss).")
    print("Lưu ý: chạy lại với cùng seed để tái lập.")


if __name__ == "__main__":
    main()
