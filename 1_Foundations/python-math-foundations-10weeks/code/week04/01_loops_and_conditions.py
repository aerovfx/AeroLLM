# Tuần 04 · Bài 01: Vòng lặp for và câu lệnh if/elif/else.
# Mục tiêu: Duyệt range/list, rẽ nhánh theo điều kiện, gán nhãn đạt/không đạt.
# Đầu vào: Danh sách điểm giả.
# Đầu ra: Nhãn đạt/không đạt và bảng cửu chương.
# Cách chạy: python code/week04/01_loops_and_conditions.py
# Lưu ý an toàn: Vòng lặp có điều kiện dừng rõ ràng; không có vòng lặp vô hạn.


def label_scores(scores):
    """Trả về danh sách nhãn 'đạt'/'không đạt' theo ngưỡng 5."""
    labels = []  # Khởi tạo danh sách kết quả rỗng.
    # Duyệt từng điểm trong danh sách scores.
    for score in scores:
        if score >= 5:
            labels.append("đạt")       # Nhánh if: điểm >= 5.
        else:
            labels.append("không đạt")  # Nhánh else: điểm < 5.
    return labels


def multiplication_table(n):
    """In bảng cửu chương của n (từ 1 đến 10)."""
    # range(1, 11) sinh 1..10 (dừng trước 11).
    for i in range(1, 11):
        print(f"{n} x {i:2d} = {n * i}")


def main():
    scores = [8, 4, 7, 3, 9]

    # In nhãn cho từng điểm bằng cách lặp và gọi nhãn.
    labels = label_scores(scores)
    for score, label in zip(scores, labels):
        print(f"Điểm {score}: {label}")

    # In bảng cửu chương của 7.
    print("\nBảng cửu chương 7:")
    multiplication_table(7)


if __name__ == "__main__":
    main()
