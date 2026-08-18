# Tuần 05 · Bài 02: Vector store in-memory với cosine search.
# Mục tiêu: Xây vector store đơn giản: add(vector, payload) và search(query, k).
# Đầu vào: Vector giả + payload (văn bản).
# Đầu ra: Top-k vector gần nhất theo cosine kèm payload.
# Cách chạy: python 02_vector_store.py
# Lưu ý an toàn: Đây là brute-force (O(N*D)); chỉ dùng tập nhỏ để học.

import math


class VectorStore:
    """Lưu vector + payload trong bộ nhớ, tìm kiếm chính xác bằng cosine."""

    def __init__(self):
        self.vectors = []   # list[list[float]]
        self.payloads = []  # list[dict]

    def add(self, vector, payload):
        """Thêm một vector kèm payload. Validate độ dài khớp không gian."""
        if not vector:
            raise ValueError("vector không được rỗng")
        if self.vectors and len(vector) != len(self.vectors[0]):
            raise ValueError("vector phải cùng số chiều")
        self.vectors.append(list(vector))
        self.payloads.append(payload)

    def search(self, query, k=3):
        """Trả top-k (score, payload) theo cosine similarity giảm dần."""
        if not self.vectors:
            return []
        k = min(k, len(self.vectors))  # Không lấy quá số vector hiện có.
        scored = []
        for i, v in enumerate(self.vectors):
            scored.append((self._cosine(query, v), i))
        scored.sort(key=lambda x: x[0], reverse=True)
        return [(score, self.payloads[i]) for score, i in scored[:k]]

    @staticmethod
    def _cosine(a, b):
        dot = sum(x * y for x, y in zip(a, b))
        na = math.sqrt(sum(x * x for x in a))
        nb = math.sqrt(sum(y * y for y in b))
        return dot / (na * nb) if na and nb else 0.0


def main():
    store = VectorStore()
    # Vector giả 3 chiều; payload chứa văn bản + nguồn để trích dẫn.
    store.add([1.0, 0.0, 0.0], {"text": "refund policy", "source": "policy"})
    store.add([0.9, 0.1, 0.0], {"text": "return within 30 days", "source": "policy"})
    store.add([0.0, 1.0, 0.0], {"text": "office hours 9-6", "source": "ops"})
    store.add([0.0, 0.0, 1.0], {"text": "laptop for employees", "source": "it"})

    query = [1.0, 0.0, 0.0]  # gần chủ đề refund.
    for score, payload in store.search(query, k=2):
        print(f"[{score:.3f}] {payload['text']} (source={payload['source']})")


if __name__ == "__main__":
    main()
