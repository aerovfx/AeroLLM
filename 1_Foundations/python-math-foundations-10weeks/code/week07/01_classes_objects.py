# Tuần 07 · Bài 01: Class và đối tượng trong Python.
# Mục tiêu: Định nghĩa lớp với __init__, tạo đối tượng, truy cập thuộc tính.
# Đầu vào: Tên và điểm giả khi khởi tạo đối tượng.
# Đầu ra: In thuộc tính và phương thức của từng đối tượng.
# Cách chạy: python code/week07/01_classes_objects.py
# Lưu ý an toàn: Dữ liệu giả; không lưu thông tin nhạy cảm vào thuộc tính.


class Student:
    """Lớp mô tả một sinh viên với tên và điểm."""

    # __init__ là phương thức khởi tạo, chạy khi tạo đối tượng mới.
    def __init__(self, name, score):
        self.name = name    # Thuộc tính name của đối tượng.
        self.score = score  # Thuộc tính score của đối tượng.

    def passed(self):
        """Trả về True nếu điểm >= 5 (đạt)."""
        # self trỏ tới chính đối tượng đang gọi phương thức.
        return self.score >= 5


def main():
    # Tạo hai đối tượng Student từ cùng một lớp.
    s1 = Student("An", 8.5)
    s2 = Student("Bình", 4.0)

    # Truy cập thuộc tính bằng dấu chấm.
    print(f"{s1.name} — điểm {s1.score}, đạt: {s1.passed()}")
    print(f"{s2.name} — điểm {s2.score}, đạt: {s2.passed()}")

    # Kiểm tra kiểu của đối tượng.
    print("Kiểu của s1:", type(s1).__name__)


if __name__ == "__main__":
    main()
