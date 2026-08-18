# Tuần 07 · Bài 02: Faithfulness (groundedness) heuristic.
# Mục tiêu: Kiểm tra câu trả lời có bám vào context không, không cần mô hình thật.
# Đầu vào: Câu trả lời và context (các đoạn văn).
# Đầu ra: Tỷ lệ "claim" được hỗ trợ và nhãn supported/unsupported.
# Cách chạy: python 02_faithfulness.py
# Lưu ý an toàn: Heuristic chỉ là xấp xỉ; production cần đánh giá con người/model judge.

import re


def split_claims(answer):
    """Tách câu trả lời thành các claim (câu con) đơn giản."""
    # Tách theo dấu câu; bỏ các mảnh rỗng.
    parts = [p.strip() for p in re.split(r"[.;]", answer) if p.strip()]
    return parts


def supported(claim, context):
    """Một claim được coi là 'hỗ trợ' nếu từ khoá chính xuất hiện trong context.

    Đây là heuristic từ vựng; không phải suy luận ngữ nghĩa thật.
    """
    tokens = set(re.findall(r"[a-z0-9]+", claim.lower()))
    # Bỏ các stopword đơn giản để chỉ so từ mang nghĩa.
    stopwords = {"the", "a", "an", "is", "are", "of", "to", "in", "and", "or"}
    tokens -= stopwords
    if not tokens:
        return True
    context_tokens = set(re.findall(r"[a-z0-9]+", context.lower()))
    return len(tokens & context_tokens) / len(tokens) >= 0.5


def faithfulness(answer, contexts):
    """Trả (tỷ lệ supported, danh sách (claim, bool))."""
    claims = split_claims(answer)
    if not claims:
        return 0.0, []
    context = " ".join(contexts)
    results = [(c, supported(c, context)) for c in claims]
    return sum(1 for _, ok in results if ok) / len(results), results


def main():
    contexts = [
        "Refund policy allows returns within 30 days of purchase.",
        "Coverage begins on the first day of the month following hire.",
    ]
    # Câu trả lời bám context (tốt) và câu bịa thêm (hallucination).
    good = "Refunds are allowed within 30 days. Coverage begins after hire."
    bad = "Refunds are allowed within 30 days. Employees get a free car."

    for name, answer in [("grounded", good), ("hallucinated", bad)]:
        ratio, results = faithfulness(answer, contexts)
        print(f"{name}: faithfulness={ratio:.2f}")
        for claim, ok in results:
            print(f"  [{'OK' if ok else 'X'}] {claim}")


if __name__ == "__main__":
    main()
