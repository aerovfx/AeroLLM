# Tuần 09 · Bài 01: Median replacement và ripple-rate experiment.
# Mục tiêu: Thay nhóm neuron hoạt động mạnh nhất bằng trung vị tầng, quét tỷ lệ p để thấy
#           "hiệu ứng ngưỡng": phần lớn tín hiệu do một nhóm rất nhỏ neuron mang.
# Đầu vào: Kích hoạt MLP giả (500 neuron), trong đó ~1% neuron mang tín hiệu mạnh.
# Đầu ra: Logit change khi thay top-p% neuron bằng trung vị, với nhiều giá trị p.
# Cách chạy: python 01_median_replacement.py
# An toàn: Chỉ chạy local; ghi rõ cách chọn top-p (theo giá trị tuyệt đối); seed cố định.

import numpy as np

rng = np.random.default_rng(15)
K = 500
CORE = [10, 77, 150, 233, 410]   # 5 neuron "lõi" (~1%) mang tín hiệu quyết định

# ---- Bước 1: sinh kích hoạt ----
a = 0.05 * rng.standard_normal(K)          # nền nhiễu
for i in CORE:
    a[i] = rng.uniform(50, 90)             # neuron lõi có giá trị rất lớn

# Readout: logit = tổng kích hoạt (đơn giản; neuron lõi chi phối hoàn toàn).
def logit(act):
    return float(act.sum())

baseline = logit(a)
median = float(np.median(a))
print(f"Baseline logit = {baseline:.1f} | trung vị tầng = {median:.3f}")


def median_replace(act, p_percent):
    """Thay top-p% neuron (theo giá trị tuyệt đối) bằng trung vị tầng."""
    out = act.copy()
    k = int(np.ceil(p_percent / 100.0 * len(act)))
    top_idx = np.argsort(np.abs(out))[-k:]     # k neuron có |giá trị| lớn nhất
    out[top_idx] = median
    return out


# ---- Bước 2: ripple-rate experiment ----
print("\nTỷ lệ p | logit sau thay | logit change")
for p in [0.2, 0.5, 1.0, 2.0, 5.0, 10.0, 20.0, 50.0, 90.0]:
    new_logit = logit(median_replace(a, p))
    print(f"  {p:5.1f}% | {new_logit:13.1f} | {new_logit - baseline:+10.1f}")

# ---- Bước 3: nhận xét ----
# p nhỏ (0.2-1%) mới có biến thiên lớn (dần loại bỏ từng neuron lõi).
# Từ ~1% trở lên, toàn bộ neuron lõi đã bị thay -> logit về gần 0 và gần như không đổi thêm.
print("\n=> Một khi đã vô hiệu hoá 'nhóm lõi', thay thêm hàng trăm neuron cũng không đổi thêm.")
