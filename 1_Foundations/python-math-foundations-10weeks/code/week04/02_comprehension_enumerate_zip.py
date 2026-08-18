# Tuần 04 · Bài 02: List comprehension, enumerate và zip.
# Mục tiêu: Biến đổi danh sách bằng comprehension; duyệt có chỉ mục và ghép dãy.
# Đầu vào: Danh sách tên và điểm giả.
# Đầu ra: Danh sách bình phương, cặp (vị trí, tên), cặp (tên, điểm).
# Cách chạy: python code/week04/02_comprehension_enumerate_zip.py
# Lưu ý an toàn: Chỉ thao tác trên dữ liệu giả trong bộ nhớ.


def main():
    # List comprehension: tạo danh sách bình phương của 0..4.
    squares = [x * x for x in range(5)]
    print("Bình phương 0..4:", squares)

    # Comprehension có điều kiện: chỉ lấy bình phương của số chẵn.
    even_squares = [x * x for x in range(10) if x % 2 == 0]
    print("Bình phương số chẵn:", even_squares)

    # enumerate: trả về cặp (chỉ mục, phần tử).
    names = ["An", "Bình", "Châu"]
    print("\nVị trí - tên:")
    for i, name in enumerate(names):
        print(f"  {i}: {name}")

    # zip: ghép từng phần tử tương ứng của hai dãy.
    scores = [8.5, 7.0, 9.0]
    print("Tên - điểm:")
    for name, score in zip(names, scores):
        print(f"  {name}: {score}")


if __name__ == "__main__":
    main()
