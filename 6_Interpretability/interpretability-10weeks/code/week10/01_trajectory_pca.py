# Tuần 10 · Bài 01: Quỹ đạo không gian trạng thái qua PCA (common space).
# Mục tiêu: Chiếu quỹ đạo của các token qua các tầng xuống 2D, fit PCA MỘT lần trên toàn bộ
#           dữ liệu ghép để có hệ toạ độ chung, và thấy token sai ngữ pháp "văng" ra xa.
# Đầu vào: Quỹ đạo giả của 3 token (him, her, và "round" sai ngữ pháp) qua 5 tầng.
# Đầu ra: Toạ độ 2D của mỗi token ở tầng cuối, và khoảng cách giữa các cụm.
# Cách chạy: python 01_trajectory_pca.py
# An toàn: Chỉ chạy local; cảnh báo "variance != relevance" của PCA; seed cố định.

import numpy as np

rng = np.random.default_rng(17)
D, L = 10, 5          # 10 chiều, 5 tầng
N_PER = 30            # số câu mỗi token

valid_dir = rng.standard_normal(D); valid_dir /= np.linalg.norm(valid_dir)
invalid_dir = rng.standard_normal(D); invalid_dir /= np.linalg.norm(invalid_dir)


def trajectory(kind):
    """Trả về (N_PER, L, D): quỹ đạo qua L tầng của một loại token."""
    traj = np.zeros((N_PER, L, D))
    for i in range(N_PER):
        h = 0.1 * rng.standard_normal(D)
        for l in range(L):
            if kind == "him":
                h = h + valid_dir + 0.05 * rng.standard_normal(D)
            elif kind == "her":
                h = h + valid_dir - 0.05 * rng.standard_normal(D)
            else:  # "round": sai ngữ pháp, đi theo hướng khác và nhiễu loạn
                h = h + invalid_dir + 0.3 * rng.standard_normal(D)
            traj[i, l] = h
    return traj


traj = {"him": trajectory("him"), "her": trajectory("her"), "round": trajectory("round")}

# ---- Bước 1: ghép toàn bộ vector (mọi token x mọi tầng x mọi câu) rồi fit PCA MỘT lần ----
all_vecs = np.concatenate([t.reshape(-1, D) for t in traj.values()], axis=0)
mean = all_vecs.mean(axis=0)
Xc = all_vecs - mean
U, S, Vt = np.linalg.svd(Xc, full_matrices=False)   # SVD cho hệ toạ độ chung
P2 = Vt[:2].T                                       # (D, 2): chiếu xuống 2D


def project(t):
    return (t - mean) @ P2                            # chiếu mọi điểm về chung 2 trục


# ---- Bước 2: vẽ (in) toạ độ 2D ở tầng cuối ----
print("Toạ độ 2D (PC1, PC2) ở tầng cuối — trung bình mỗi token:")
last = {}
for k in traj:
    pts = project(traj[k][:, -1, :])                  # (N_PER, 2) ở tầng cuối
    last[k] = pts.mean(axis=0)
    print(f"  {k:6s}: {np.round(last[k], 2)}")

d_valid = np.linalg.norm(last["him"] - last["her"])
d_bad = np.linalg.norm(last["round"] - (last["him"] + last["her"]) / 2)
print(f"\nKhoảng cách him-her (cùng nhóm đúng): {d_valid:.2f}")
print(f"Khoảng cách round -> nhóm đúng          : {d_bad:.2f}")

# ---- Bước 3: nhận xét ----
# him/her gần nhau (cùng ngữ pháp chuẩn), round tách xa (mô hình xử lý đầu vào bất thường).
# Lưu ý: PCA coi phương sai lớn = quan trọng, nhưng điều đó không phải lúc nào cũng đúng.
print("\n=> Trajectory là 'phim' trực quan, nhưng chỉ là điểm khởi đầu, không phải kết luận.")
