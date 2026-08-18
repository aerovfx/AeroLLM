# Tuần 03 · Bài 02: Số học vector (analogy) và trục ngữ nghĩa tuyến tính.
# Mục tiêu: Kiểm chứng king - man + woman ~ queen, và dựng một "trục ngữ nghĩa" để
#           chiếu mọi vector lên đó.
# Đầu vào: Nhúng giả có cấu trúc giới tính + hoàng tộc cấy sẵn.
# Đầu ra: Token gần nhất với kết quả phép analogy, và toạ độ chiếu theo trục.
# Cách chạy: python 02_analogy_arithmetic.py
# An toàn: Chỉ chạy local; analogy là "soft-coded", không phải quy luật cứng của model.

import numpy as np

rng = np.random.default_rng(4)
D = 10

# ---- Bước 1: dựng nhúng có hai trục ngữ nghĩa vuông góc ----
axis_gender = rng.standard_normal(D)   # trục "nam -> nữ"
axis_gender /= np.linalg.norm(axis_gender)
axis_royal = rng.standard_normal(D)    # trục "thường dân -> hoàng tộc"
# Làm hai trục gần trực giao để cấu trúc rõ ràng (Gram-Schmidt).
axis_royal -= axis_royal.dot(axis_gender) * axis_gender
axis_royal /= np.linalg.norm(axis_royal)

# Toạ độ (gender, royal) của từng từ; noise nhỏ để không quá "sạch".
coords = {
    "king":   (0.0, 1.0),
    "queen":  (1.0, 1.0),
    "man":    (0.0, 0.0),
    "woman":  (1.0, 0.0),
}
emb = {}
for w, (g, r) in coords.items():
    emb[w] = g * axis_gender + r * axis_royal + 0.05 * rng.standard_normal(D)


def normalize(v):
    n = np.linalg.norm(v)
    return v / n if n > 1e-12 else v


def nearest(query, exclude=None):
    """Trả về từ có cosine similarity cao nhất với query (loại trừ các từ trong exclude)."""
    best, best_sim = None, -2.0
    for w, v in emb.items():
        if exclude and w in exclude:
            continue
        sim = float(normalize(query).dot(normalize(v)))
        if sim > best_sim:
            best, best_sim = w, sim
    return best, best_sim


# ---- Bước 2: phép analogy ----
query = emb["king"] - emb["man"] + emb["woman"]
answer, sim = nearest(query, exclude=["king", "man", "woman"])
print("king - man + woman ~ ? ->", answer, f"(cos = {sim:.3f})", "| đáp án mong đợi: queen")

# ---- Bước 3: dựng trục ngữ nghĩa và chiếu ----
u = normalize(emb["woman"] - emb["man"])   # trục "nam -> nữ"
print("\nToạ độ chiếu lên trục giới tính (nam -> nữ):")
for w, v in emb.items():
    print(f"  {w:6s}: {float(normalize(v).dot(u)):+.3f}")

# ---- Bước 4: nhận xét ----
# Kết quả analogy gần "queen" và chiếu theo trục tách rõ man/king (âm) khỏi woman/queen (dương).
# Đây chỉ là quan hệ hình học "mềm" của không gian nhúng, không phải quy luật logic của model.
print("\n=> Trục ngữ nghĩa tuyến tính cho phép đo 'toạ độ theo khái niệm' một cách gọn gàng.")
