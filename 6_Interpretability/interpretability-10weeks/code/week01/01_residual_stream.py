# Tuần 01 · Bài 01: Mô phỏng residual stream.
# Mục tiêu: Người học thấy một vector token "dịch chuyển" qua từng block Transformer,
#           và hiểu residual stream là dòng trạng thái được cập nhật cộng dồn.
# Đầu vào: Không cần file ngoài; embedding và trọng số được sinh ngẫu nhiên có seed.
# Đầu ra: Khoảng cách (L2) giữa embedding đầu và vector sau mỗi block, in ra màn hình.
# Cách chạy: python 01_residual_stream.py
# An toàn: Chỉ chạy local trên mảng giả; không tải mô hình thật; seed cố định để tái lập.

import numpy as np

# ---- Tham số cấu hình (đổi được để thí nghiệm) ----
VOCAB = 8        # số token giả (chỉ số 0..VOCAB-1)
DIM = 6          # số chiều embedding
N_BLOCKS = 4     # số block giả lập residual stream
SEED = 0         # seed cố định để tái lập kết quả
rng = np.random.default_rng(SEED)

# ---- Bước 1: tạo bảng embedding E (VOCAB x DIM) ----
# Mỗi hàng là vector ban đầu của một token trước khi vào mạng.
E = rng.standard_normal((VOCAB, DIM))

# Câu giả lập: "0 1 2 3" (4 token liên tiếp).
tokens = np.array([0, 1, 2, 3])
h = E[tokens].copy()          # (4, DIM): residual stream ban đầu
h0 = h.copy()                 # giữ lại để đo độ dịch chuyển

print("Residual stream ban đầu (token 0):", np.round(h0[0], 3))

# ---- Bước 2: mô phỏng từng block ----
# Một block thật = h + Attention(h) + MLP(h). Ở đây ta dùng hai phép cập nhật đơn giản
# nhưng cùng "hình dạng" phép cộng residual để minh hoạ ý tưởng.
for block in range(N_BLOCKS):
    # (a) "Attention" giả: trung bình có trọng số mềm (softmax theo khoảng cách chỉ số).
    #     Ma trận trọng số W_att cho biết token i nhìn token j bao nhiêu.
    raw = -np.abs(np.subtract.outer(np.arange(len(tokens)), np.arange(len(tokens))))
    attn = np.exp(raw) / np.exp(raw).sum(axis=1, keepdims=True)  # (4,4) chuẩn hoá hàng
    attn_update = attn @ h                                       # (4, DIM)

    # (b) "MLP" giả: một phép phi tuyến đơn giản (tanh) để tạo cập nhật không tuyến tính.
    mlp_update = np.tanh(h @ rng.standard_normal((DIM, DIM)))

    # (c) Cập nhật residual: cộng dồn vào dòng trạng thái.
    h = h + 0.3 * attn_update + 0.3 * mlp_update

    # Đo độ dịch chuyển trung bình so với trạng thái ban đầu.
    drift = np.linalg.norm(h - h0, axis=1).mean()
    print(f"Block {block + 1}: drift trung bình = {drift:.3f}")

# ---- Bước 3: nhận xét ----
# Giá trị drift tăng dần cho thấy token được "làm giàu" ngữ cảnh qua từng block.
print("\nVector token 0 sau mọi block:", np.round(h[0], 3))
print("=> Residual stream cho phép thông tin tích luỹ dần thay vì thay thế hoàn toàn.")
