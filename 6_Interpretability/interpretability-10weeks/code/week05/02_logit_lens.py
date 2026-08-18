# Tuần 05 · Bài 02: Logit lens — soi dự đoán token ở từng tầng.
# Mục tiêu: Nhân hidden state của mỗi tầng với ma trận unembedding W_U để xem "model đang
#           nghĩ token gì" trước khi tới tầng cuối.
# Đầu vào: Hidden state giả của một token qua 4 tầng, và ma trận unembedding giả.
# Đầu ra: Token có logit cao nhất tại mỗi tầng.
# Cách chạy: python 02_logit_lens.py
# An toàn: Chỉ chạy local; dùng biểu diễn giả; logit lens là giả định, không phải chân lý.

import numpy as np

rng = np.random.default_rng(8)
D, V = 12, 6       # 12 chiều ẩn, 6 token từ vựng
LAYERS = 4

# ---- Bước 1: ma trận unembedding W_U (D x V) ----
# Mỗi cột là "hướng đọc" của một token trong không gian ẩn.
W_U = rng.standard_normal((D, V))

# ---- Bước 2: hidden state của token tại mỗi tầng ----
# Token mục tiêu là token số 3. Ta "cấy" để càng sâu hidden state càng thẳng hàng với W_U[:, 3].
target = W_U[:, 3].copy()
target /= np.linalg.norm(target)
h = [rng.standard_normal(D)]                 # tầng 0: nhiễu, chưa có dự đoán
for layer in range(1, LAYERS):
    # Mỗi tầng đẩy hidden state về phía hướng token mục tiêu một phần.
    h.append(h[-1] + 0.6 * target + 0.1 * rng.standard_normal(D))


def top_token(hidden):
    logits = hidden @ W_U                      # (V,)
    return int(np.argmax(logits)), logits


print("Logit lens theo tầng:")
for layer in range(LAYERS):
    tok, logits = top_token(h[layer])
    print(f"  Layer {layer}: token dự đoán = {tok} (logits = {np.round(logits, 2)})")

# ---- Bước 3: nhận xét ----
# Tầng đầu chưa rõ (token ngẫu nhiên), càng sâu dự đoán càng hội tụ về token mục tiêu (3).
# Đây là "phim tư duy" của model, nhưng dựa trên giả định W_U đọc được ý nghĩa từ mọi tầng.
print("\n=> Dự đoán 'hiện dần' qua các tầng; tầng đầu là nhiễu, tầng cuối tự tin.")
