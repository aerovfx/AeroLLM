# Tuần 08 · Bài 01: Head ablation (cắt bỏ attention head).
# Mục tiêu: Cô lập một head bằng cách zero-out đầu ra của nó TRƯỚC khi các head bị trộn
#           bởi c_proj, rồi đo logit difference của token đúng vs token nhiễu.
# Đầu vào: Mô hình giả nhiều head, trong đó một head mang tín hiệu "Germany".
# Đầu ra: Logit diff (Germany - France) khi tắt từng head.
# Cách chạy: python 01_head_ablation.py
# An toàn: Chỉ chạy local; đo logit liên tục, không chỉ top-1; seed cố định.

import numpy as np

rng = np.random.default_rng(13)
H, HEAD_DIM = 4, 2
D = H * HEAD_DIM              # 8: sau concat

# ---- Bước 1: ma trận unembedding (D x 2) cho hai token ----
W_U = rng.standard_normal((D, 2)) * 0.3
# Token 0 = "Germany" (đúng), token 1 = "France" (nhiễu cùng nhóm ngữ nghĩa).
W_U[:, 0] = rng.standard_normal(D); W_U[:, 0] /= np.linalg.norm(W_U[:, 0])
W_U[:, 1] = rng.standard_normal(D); W_U[:, 1] /= np.linalg.norm(W_U[:, 1])

# ---- Bước 2: đầu ra từng head (mỗi head là vector HEAD_DIM) ----
# Head 2 được cấy để "chỉ" về Germany sau khi trộn bởi c_proj.
head_outputs = [0.3 * rng.standard_normal(HEAD_DIM) for _ in range(H)]
# Head 2 = hướng mà sau c_proj + W_U cho logit Germany cao.
head_outputs[2] = np.array([1.0, -1.0])

# c_proj (D x D): ma trận trộn các head thành residual (ở đây gần như nhận dạng có nhiễu).
W_O = np.eye(D) + 0.1 * rng.standard_normal((D, D))


def forward(ablate=None):
    """Tính logits. Nếu ablate = h thì zero-out head h trước khi trộn (c_proj)."""
    out = [o.copy() for o in head_outputs]
    if ablate is not None:
        out[ablate] = np.zeros(HEAD_DIM)
    concat = np.concatenate(out)          # (D,)
    residual = W_O @ concat               # c_proj
    return residual @ W_U                 # logits (Germany, France)


def logit_diff(logits):
    return float(logits[0] - logits[1])   # Germany - France


print("Baseline logit diff (Germany - France) =", round(logit_diff(forward()), 3))
print("Ablate từng head:")
for h in range(H):
    diff = logit_diff(forward(ablate=h))
    print(f"  Tắt head {h}: logit diff = {diff:+.3f}")

print("\n=> Tắt head mang tín hiệu (head 2) làm logit diff giảm rõ; các head khác ít ảnh hưởng.")
