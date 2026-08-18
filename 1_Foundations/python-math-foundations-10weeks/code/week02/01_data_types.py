# Tuần 02 · Bài 01: Các kiểu dữ liệu cơ bản.
# Mục tiêu: Khai báo và kiểm tra kiểu int/float/str/bool bằng type().
# Đầu vào: Các giá trị giả khai báo sẵn trong code.
# Đầu ra: In giá trị và kiểu của từng biến.
# Cách chạy: python code/week02/01_data_types.py
# Lưu ý an toàn: Dữ liệu giả; không chứa thông tin cá nhân thật.


def main():
    # Khai báo các biến thuộc 4 kiểu cơ bản.
    age = 21            # int: số nguyên.
    height = 1.75       # float: số thực.
    name = "An"         # str: chuỗi ký tự.
    is_student = True   # bool: đúng/sai.

    # In từng biến kèm kiểu bằng type(...).__name__ để gọn tên kiểu.
    print(f"age = {age}, kiểu = {type(age).__name__}")
    print(f"height = {height}, kiểu = {type(height).__name__}")
    print(f"name = {name}, kiểu = {type(name).__name__}")
    print(f"is_student = {is_student}, kiểu = {type(is_student).__name__}")

    # Phép toán số học: so sánh phép chia / và // (lấy nguyên).
    print("\nPhép toán số học:")
    print("17 / 5  =", 17 / 5)    # Chia thường luôn ra float.
    print("17 // 5 =", 17 // 5)   # Chia lấy nguyên.
    print("17 % 5  =", 17 % 5)    # Chia lấy dư.

    # Thứ tự ưu tiên: * / trước + -; dùng ngoặc để rõ ý.
    print("\nThứ tự ưu tiên:")
    print("2 + 3 * 4   =", 2 + 3 * 4)     # 14 (nhân trước).
    print("(2 + 3) * 4 =", (2 + 3) * 4)   # 20 (ngoặc trước).


if __name__ == "__main__":
    main()
