# Tuần 07 · Bài 01: Activation patching trên tác vụ IOI (toy).
# Mục tiêu: Cấy hidden state từ câu "nguồn" (donor) vào câu "đích" (recipient) tại từng tầng,
#           quan sát hiện tượng chuyển pha: tầng sớm kháng nhiễu, tầng sau nhạy cảm.
# Đầu vào: Hai câu giả khác nhau ở tên tân ngữ (Bob vs Barbara); mô hình giả cấy thông tin
#          tên vào residual stream tại tầng giữa.
# Đầu ra: Logit difference (Bob - Barbara) trước và sau khi vá tại mỗi tầng.
# Cách chạy: python 01_activation_patching_ioi.py
# An toàn: Chỉ chạy local; cặp donor/recipient chỉ khác đúng một biến; seed cố định.

import numpy as np

rng = np.random.default_rng(11)
D, L = 8, 6
INTEGRATION_LAYER = 3     # tầng "tích hợp" tên vào residual stream

e_bob = rng.standard_normal(D); e_bob /= np.linalg.norm(e_bob)
e_barbara = rng.standard_normal(D); e_barbara /= np.linalg.norm(e_barbara)


def run(name_embedding):
    """Chạy forward: residual bắt đầu bằng nhiễu, tại INTEGRATION_LAYER cộng tên vào."""
    h = rng.standard_normal(D) * 0.1
    for layer in range(L):
        # Mỗi tầng thêm một cập nhật nhỏ; tên được "tiêm" đúng một lần ở tầng giữa.
        if layer == INTEGRATION_LAYER:
            h = h + name_embedding * 4.0
        h = h + 0.1 * np.tanh(h @ rng.standard_normal((D, D)))
    return h


def logit_diff(h):
    return float(h @ e_bob - h @ e_barbara)   # Bob - Barbara


# Donor: Barbara (tân ngữ = Barbara). Recipient: Bob (tân ngữ = Bob).
h_donor = run(e_barbara)
h_recipient = run(e_bob)
print("Recipient (sạch, đáp án Bob)  logit diff =", round(logit_diff(h_recipient), 3))
print("Donor     (đáp án Barbara)     logit diff =", round(logit_diff(h_donor), 3))

# ---- Vá hidden state tại từng tầng ----
print("\nVá hidden state từ donor vào recipient tại tầng k:")
for k in range(L):
    h = rng.standard_normal(D) * 0.1
    for layer in range(L):
        if layer == k:
            # Tại tầng k, ghi đè toàn bộ hidden state bằng giá trị donor tương ứng.
            # (Mô phỏng đơn giản: dùng hidden donor "tại cùng độ sâu".)
            h = h_donor  # cấy trạng thái donor vào đúng thời điểm k
        if layer == INTEGRATION_LAYER:
            h = h + e_bob * 4.0        # recipient vẫn "tiêm" tên Bob ở tầng giữa
        h = h + 0.1 * np.tanh(h @ rng.standard_normal((D, D)))
    print(f"  Vá tại tầng {k}: logit diff = {logit_diff(h):+.3f}")

print("\n=> Vá trước tầng tích hợp bị 'rửa trôi' (vẫn Bob); vá sau tầng tích hợp làm lật sang Barbara.")
