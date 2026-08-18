# Tuần 05 · Bài 02: Vẽ biểu đồ với Matplotlib.
# Mục tiêu: Vẽ biểu đồ đường/chấm có nhãn; tạo lưới subplot; lưu file.
# Đầu vào: Dữ liệu x, y giả khai báo trong code.
# Đầu ra: File chart.png (và hiển thị nếu chạy ở môi trường có GUI).
# Cách chạy: python code/week05/02_plotting.py
# Lưu ý an toàn: Chỉ vẽ dữ liệu giả; không ghi đè file quan trọng (đặt tên rõ).

# Import matplotlib.pyplot để vẽ biểu đồ.
import matplotlib
# Dùng backend Agg (không cần màn hình) để chạy được trên server/Colab không GUI.
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def main():
    # Dữ liệu giả: y = 2x cho x từ 1 đến 5.
    x = [1, 2, 3, 4, 5]
    y = [2 * i for i in x]

    # Tạo lưới 1 hàng x 2 cột biểu đồ con.
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

    # Biểu đồ trái: đường với chấm đánh dấu.
    ax1.plot(x, y, marker="o", color="tab:blue")
    ax1.set_title("Đường y = 2x")   # Tiêu đề biểu đồ.
    ax1.set_xlabel("x")             # Nhãn trục hoành.
    ax1.set_ylabel("y")             # Nhãn trục tung.

    # Biểu đồ phải: chấm rời (scatter) với dữ liệu khác.
    xs = [1, 2, 3, 4, 5]
    ys = [3, 1, 4, 2, 5]
    ax2.scatter(xs, ys, color="tab:red")
    ax2.set_title("Chấm rời")
    ax2.set_xlabel("x")
    ax2.set_ylabel("y")

    # Dàn đều bố cục để nhãn không bị chồng nhau.
    fig.tight_layout()

    # Lưu biểu đồ ra file PNG rồi in đường dẫn.
    fig.savefig("chart.png", dpi=100)
    print("Đã lưu biểu đồ: chart.png")


if __name__ == "__main__":
    main()
