# Tuần 03 · Bài 01: Cosine similarity và ma trận tương đồng.
# Mục tiêu: Đo độ tương đồng hướng giữa các vector nhúng và đối chiếu với nhúng ngẫu nhiên
#           để thấy nguy cơ "ảo giác diễn giải".
# Đầu vào: Nhúng giả có cấu trúc ngữ nghĩa cấy sẵn (động vật vs thành phố).
# Đầu ra: Ma trận cosine similarity (làm tròn) cho nhúng thật và nhúng ngẫu nhiên.
# Cách chạy: python 01_cosine_similarity.py
# An toàn: Chỉ chạy local; chuẩn hoá vector để tránh chia 0; seed cố định.

import numpy as np

rng = np.random.default_rng(3)

# ---- Bước 1: tạo nhúng có cấu trúc ----
D = 8
words = ["dog", "cat", "wolf", "paris", "london", "rome"]
# Hai "tâm cụm": động vật và thành phố, cộng nhiễu nhỏ để mỗi từ lệch quanh tâm.
animal_center = rng.standard_normal(D)
city_center = rng.standard_normal(D)
emb = {}
for w in words:
    center = animal_center if w in ("dog", "cat", "wolf") else city_center
    emb[w] = center + 0.1 * rng.standard_normal(D)


def normalize(v):
    n = np.linalg.norm(v)
    return v / n if n > 1e-12 else v   # tránh chia cho 0


def cosine(a, b):
    return float(np.dot(normalize(a), normalize(b)))


def similarity_matrix(words, embs):
    """Trả về ma trận cosine similarity giữa các từ theo thứ tự words."""
    M = np.zeros((len(words), len(words)))
    for i, wi in enumerate(words):
        for j, wj in enumerate(words):
            M[i, j] = cosine(embs[wi], embs[wj])
    return M


# ---- Bước 2: tính và in ----
print("Nhúng có cấu trúc (động vật vs thành phố):")
print(np.round(similarity_matrix(words, emb), 2))

# Đối chứng: nhúng ngẫu nhiên cùng kích thước.
emb_rand = {w: rng.standard_normal(D) for w in words}
print("\nNhúng ngẫu nhiên (baseline):")
print(np.round(similarity_matrix(words, emb_rand), 2))

# ---- Bước 3: nhận xét ----
# Nhúng có cấu trúc cho similarity cao trong cùng cụm, thấp giữa hai cụm.
# Nhúng ngẫu nhiên cũng tạo ra vài giá trị khá cao — tín hiệu giả nếu ta vội kết luận.
print("\n=> Cần baseline ngẫu nhiên trước khi tin một 'cụm' trên heatmap là có nghĩa.")
