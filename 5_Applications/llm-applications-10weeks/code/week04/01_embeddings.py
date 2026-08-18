# Tuần 04 · Bài 01: Embedding mock (bag-of-words) và cosine similarity.
# Mục tiêu: Hiểu embedding và cosine similarity mà không cần mô hình/API thật.
# Đầu vào: Các câu văn bản giả.
# Đầu ra: Vector bag-of-words chuẩn hoá và độ tương đồng cosine.
# Cách chạy: python 01_embeddings.py
# Lưu ý an toàn: Bag-of-words chỉ để minh hoạ luồng; không dùng cho production.

import math
import re


def tokenize(text):
    """Tách từ đơn giản: chữ thường, bỏ dấu câu.

    Dùng regex để lấy các chuỗi chữ cái/số; không cần thư viện NLP.
    """
    return re.findall(r"[a-z0-9]+", text.lower())


def bag_of_words(texts):
    """Xây vector bag-of-words cho danh sách văn bản.

    Trả (vocab, vectors) với vocab là danh sách từ và vectors là list[dict].
    """
    vocab = sorted({w for t in texts for w in tokenize(t)})
    vectors = []
    for t in texts:
        counts = {}
        for w in tokenize(t):
            counts[w] = counts.get(w, 0) + 1
        vectors.append(counts)
    return vocab, vectors


def to_dense(vocab, counts):
    """Chuyển dict đếm từ thành vector dày theo thứ tự vocab."""
    return [counts.get(w, 0) for w in vocab]


def cosine(a, b):
    """Tính cosine similarity giữa hai vector số.

    Xử lý vector rỗng/zero để tránh chia cho 0.
    """
    dot = sum(x * y for x, y in zip(a, b))
    na = math.sqrt(sum(x * x for x in a))
    nb = math.sqrt(sum(y * y for y in b))
    if na == 0 or nb == 0:
        return 0.0
    return dot / (na * nb)


def main():
    docs = [
        "the cat sat on the mat",
        "the dog sat on the log",
        "cats and dogs are pets",
        "a rocket flies into space",
    ]
    vocab, bow = bag_of_words(docs)
    dense = [to_dense(vocab, c) for c in bow]
    query = "cat on mat"
    q = to_dense(vocab, {w: tokenize(query).count(w) for w in tokenize(query)})
    for i, d in enumerate(docs):
        print(f"cosine(query, doc{i}) = {cosine(q, dense[i]):.3f}  | {d}")


if __name__ == "__main__":
    main()
