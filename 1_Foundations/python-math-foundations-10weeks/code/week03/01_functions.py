# Tuần 03 · Bài 01: Định nghĩa và gọi hàm.
# Mục tiêu: Viết hàm có tham số, return và docstring; hiểu scope.
# Đầu vào: Các giá trị giả truyền vào khi gọi hàm.
# Đầu ra: Kết quả trả về của từng hàm.
# Cách chạy: python code/week03/01_functions.py
# Lưu ý an toàn: Không đặt secret làm giá trị mặc định của tham số.


def double(x):
    """Trả về gấp đôi của x (số)."""
    # Tham số x chỉ tồn tại bên trong hàm (scope cục bộ).
    return x * 2


def average(scores):
    """Trả về trung bình cộng của danh sách scores; danh sách rỗng -> 0.0."""
    # Bảo vệ trường hợp danh sách rỗng để tránh chia cho 0.
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


def max_of(scores):
    """Trả về phần tử lớn nhất của danh sách không rỗng (không dùng max())."""
    # Nếu danh sách rỗng, báo lỗi rõ ràng thay vì trả giá trị sai.
    if not scores:
        raise ValueError("Danh sách rỗng, không có giá trị lớn nhất.")
    best = scores[0]  # Khởi tạo ứng viên lớn nhất là phần tử đầu.
    # Duyệt phần còn lại; nếu gặp phần tử lớn hơn thì cập nhật best.
    for s in scores[1:]:
        if s > best:
            best = s
    return best


def main():
    # Gọi hàm double với đối số 5.
    print("double(5) =", double(5))

    # Gọi average với danh sách bình thường và danh sách rỗng.
    print("average([8, 9, 7]) =", average([8, 9, 7]))
    print("average([]) =", average([]))

    # Gọi max_of; giá trị trả về không dùng hàm max() có sẵn.
    print("max_of([3, 9, 2]) =", max_of([3, 9, 2]))

    # In docstring của hàm double bằng help().
    print("\nhelp(double):")
    help(double)


if __name__ == "__main__":
    main()
