# Tuần 04 · Bài 02: Retriever top-k trên kho văn bản giả.
# Mục tiêu: Cài retriever nhận query -> trả top-k đoạn văn kèm điểm tương đồng.
# Đầu vào: Kho văn bản giả và câu hỏi.
# Đầu ra: Top-k đoạn liên quan nhất (kèm điểm).
# Cách chạy: python 02_retriever.py
# Lưu ý an toàn: Retrieval trả tài liệu, không kiểm chứng đúng/sai nội dung.

import math
import re


def tokenize(text):
    return re.findall(r"[a-z0-9]+", text.lower())


def to_vector(text, vocab):
    tokens = tokenize(text)
    return [tokens.count(w) for w in vocab]


def cosine(a, b):
    dot = sum(x * y for x, y in zip(a, b))
    na = math.sqrt(sum(x * x for x in a))
    nb = math.sqrt(sum(y * y for y in b))
    return dot / (na * nb) if na and nb else 0.0


def build_retriever(documents):
    """Trả hàm retrieve(query, k) dùng bag-of-words + cosine.

    Vocabulary được xây từ toàn bộ kho để mọi văn bản dùng chung không gian.
    """
    vocab = sorted({w for d in documents for w in tokenize(d)})
    vectors = [to_vector(d, vocab) for d in documents]
    def retrieve(query, k=3):
        q = to_vector(query, vocab)
        scored = [(cosine(q, v), i) for i, v in enumerate(vectors)]
        scored.sort(key=lambda x: x[0], reverse=True)  # giảm dần theo độ tương đồng.
        return [(score, documents[i]) for score, i in scored[:k]]
    return retrieve


def main():
    documents = [
        "Our refund policy allows returns within 30 days of purchase.",
        "Employees get 20 vacation days each calendar year.",
        "The office is open from 9am to 6pm on weekdays.",
        "Laptops are provided to all full-time employees.",
        "Reimbursement for travel requires an approved form.",
        "The cafeteria serves lunch between 11am and 2pm.",
    ]
    retrieve = build_retriever(documents)
    for query in ["How do I get a refund?",
                  "What are the office hours?",
                  "Do employees get laptops?"]:
        print(f"Query: {query}")
        for score, doc in retrieve(query, k=2):
            print(f"  [{score:.3f}] {doc}")
        print()


if __name__ == "__main__":
    main()
