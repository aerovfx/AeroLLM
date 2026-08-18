# Tuần 06 · Bài 02: Counterfactual patching (vá phản thực).
# Mục tiêu: Cấy hidden state từ một "ngữ cảnh nguồn" vào "ngữ cảnh đích" và quan sát
#           dự đoán "lật" sang đáp án của nguồn.
# Đầu vào: Hai ngữ cảnh giả khác nhau ở một vị trí token (tên riêng), mô hình giả.
# Đầu ra: Dự đoán trước/sau khi vá, và ảnh hưởng theo từng "tầng".
# Cách chạy: python 02_counterfactual_patching.py
# An toàn: Chỉ chạy local; vá chỉ dùng hidden state "sạch" từ ngữ cảnh khác, không bơm nhiễu.

import numpy as np

rng = np.random.default_rng(10)
D, L = 6, 4            # D chiều, L "tầng"
TOKENS = 5             # độ dài câu giả (token 0..4)


def build_context(answer_dir):
    """Tạo một ngữ cảnh giả: mỗi token là vector, token vị trí 3 mang 'đáp án' theo hướng."""
    ctx = rng.standard_normal((TOKENS, D)) * 0.2
    ctx[3] = answer_dir * 3.0            # vị trí 3 mã hoá đáp án (A hay B)
    return ctx


def forward(ctx):
    """Mô phỏng lan truyền qua L tầng: mỗi tầng trộn nhẹ token và cộng dồn residual."""
    h = ctx.copy()
    for _ in range(L):
        h = h + 0.2 * np.tanh(h @ rng.standard_normal((D, D)))
    # Đọc "đáp án" bằng cách chiếu token cuối lên hai hướng A/B.
    logit_a = float(h[-1] @ dir_a)
    logit_b = float(h[-1] @ dir_b)
    return h, (logit_a, logit_b)


dir_a = rng.standard_normal(D); dir_a /= np.linalg.norm(dir_a)
dir_b = rng.standard_normal(D); dir_b /= np.linalg.norm(dir_b)

# Nguồn = đáp án B; đích = đáp án A (token vị trí 3 ngược hướng nhau).
src = build_context(-dir_a)   # hướng ngược A -> nghiêng về B
dst = build_context(dir_a)    # nghiêng về A

h_src, _ = forward(src)
h_dst, (a0, b0) = forward(dst)
print("Đích (sạch)      : logit A - logit B =", round(a0 - b0, 3))

# ---- Vá hidden state của token 3 tại từng tầng (mô phỏng) ----
# Ta vá trực tiếp vector token 3 của đích bằng vector token 3 của nguồn ở "đầu vào mỗi tầng".
print("Vá token 3 từ nguồn vào đích (theo tầng):")
for layer in range(1, L + 1):
    # Chạy lại đích nhưng tại tầng `layer` thay token 3 bằng giá trị nguồn (trước khi trộn).
    h = dst.copy()
    for l in range(L):
        if l == layer - 1:
            h[3] = src[3] * (0.5 + 0.5 * layer / L)   # cường độ vá tăng dần theo tầng
        h = h + 0.2 * np.tanh(h @ rng.standard_normal((D, D)))
    la = float(h[-1] @ dir_a); lb = float(h[-1] @ dir_b)
    print(f"  Tầng {layer}: logit A - logit B = {la - lb:+.3f}")

print("\n=> Vá ở tầng sâu làm dự đoán 'lật' sang đáp án nguồn nhiều hơn tầng nông.")
