# Tuần 06 · Bài 02: Pipeline RAG (retrieve -> rerank -> generate) có trích nguồn.
# Mục tiêu: Lắp pipeline end-to-end với generator mock "grounded" trong context.
# Đầu vào: Kho văn bản giả + câu hỏi.
# Đầu ra: Câu trả lời + danh sách nguồn, hoặc "không tìm thấy".
# Cách chạy: python 02_rag_pipeline.py
# Lưu ý an toàn: Generator mock không phải mô hình thật; chỉ trả lời từ context.

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


def lexical_overlap(query, doc):
    return len(set(tokenize(query)) & set(tokenize(doc)))


def generate_grounded(query, contexts, threshold=1):
    """Generator mock: chỉ trả lời nếu context đủ trùng từ khoá với câu hỏi.

    Trả (answer, sources). Nếu không đủ bằng chứng -> "không tìm thấy".
    """
    best = []
    for score, doc in contexts:
        if lexical_overlap(query, doc) >= threshold:
            best.append((score, doc))
    if not best:
        return "Không tìm thấy câu trả lời trong tài liệu.", []
    answer = "Dựa trên tài liệu: " + best[0][1]
    sources = [doc for _, doc in best]
    return answer, sources


def main():
    documents = [
        "Refund policy allows returns within 30 days of purchase.",
        "Employees get 20 vacation days each calendar year.",
        "The office is open from 9am to 6pm on weekdays.",
        "Laptops are provided to all full-time employees.",
    ]
    vocab = sorted({w for d in documents for w in tokenize(d)})
    vectors = [to_vector(d, vocab) for d in documents]

    for query in ["How do I get a refund?",
                  "What laptops do employees get?",
                  "What is the capital of Mars?"]:
        q = to_vector(query, vocab)
        scored = sorted(((cosine(q, v), d) for v, d in zip(vectors, documents)),
                        key=lambda x: x[0], reverse=True)
        answer, sources = generate_grounded(query, scored[:2])
        print(f"Q: {query}")
        print(f"A: {answer}")
        print(f"Sources: {sources}\n")


if __name__ == "__main__":
    main()
