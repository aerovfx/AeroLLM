# Tuần 08 · Bài 02: Head patching trong IOI (toy).
# Mục tiêu: Thay vì zero-out, ta VÁ đầu ra của một head bằng giá trị lấy từ ngữ cảnh khác,
#           để tìm head nào "mang" thông tin tên (quan hệ IOI).
# Đầu vào: Hai ngữ cảnh giả (donor: Barbara, recipient: Bob) và mô hình nhiều head.
# Đầu ra: Logit diff (Bob - Barbara) khi vá từng head từ donor.
# Cách chạy: python 02_head_patching_ioi.py
# An toàn: Chỉ chạy local; vá dùng giá trị sạch từ ngữ cảnh khác; seed cố định.

import numpy as np

rng = np.random.default_rng(14)
H, HEAD_DIM = 5, 2
D = H * HEAD_DIM

e_bob = rng.standard_normal(HEAD_DIM); e_bob /= np.linalg.norm(e_bob)
e_barbara = rng.standard_normal(HEAD_DIM); e_barbara /= np.linalg.norm(e_barbara)

# Head 3 là head "tên": đầu ra của nó = embedding tên (Bob hoặc Barbara).
# Các head khác là nhiễu nền cố định.
NAME_HEAD = 3
def head_outputs(name_embedding):
    outs = [0.2 * rng.standard_normal(HEAD_DIM) for _ in range(H)]
    outs[NAME_HEAD] = name_embedding * 3.0
    return outs

W_O = np.eye(D) + 0.1 * rng.standard_normal((D, D))
# Unembedding: đọc tên từ residual.
W_U = np.zeros((D, 2))
W_U[NAME_HEAD * HEAD_DIM:(NAME_HEAD + 1) * HEAD_DIM, 0] = e_bob
W_U[NAME_HEAD * HEAD_DIM:(NAME_HEAD + 1) * HEAD_DIM, 1] = e_barbara


def forward(outs, patch_head=None, patch_value=None):
    outs = [o.copy() for o in outs]
    if patch_head is not None:
        outs[patch_head] = patch_value.copy()
    concat = np.concatenate(outs)
    residual = W_O @ concat
    logits = residual @ W_U       # (Bob, Barbara)
    return float(logits[0] - logits[1])


donor_outs = head_outputs(e_barbara)
recip_outs = head_outputs(e_bob)

print("Recipient (Bob)   logit diff =", round(forward(recip_outs), 3))
print("Vá từng head bằng giá trị từ donor (Barbara):")
for h in range(H):
    diff = forward(recip_outs, patch_head=h, patch_value=donor_outs[h])
    print(f"  Vá head {h}: logit diff = {diff:+.3f}")

print("\n=> Vá head 'tên' (head 3) làm dự đoán lật sang Barbara; head nhiễu không đổi gì.")
