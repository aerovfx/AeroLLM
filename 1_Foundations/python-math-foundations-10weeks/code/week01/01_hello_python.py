# Tuần 01 · Bài 01: Chào và in phiên bản Python.
# Mục tiêu: Chạy script Python đầu tiên, in chuỗi và phiên bản Python.
# Đầu vào: Không cần đầu vào.
# Đầu ra: Hai dòng in ra màn hình (lời chào + phiên bản Python).
# Cách chạy: python code/week01/01_hello_python.py
# Lưu ý an toàn: Chỉ chạy local/Colab; không chứa secret/token.

# Import module sys từ thư viện chuẩn để đọc thông tin phiên bản Python.
import sys


def main():
    # In một chuỗi chào đơn giản ra màn hình.
    print("Xin chào từ Python!")

    # sys.version là chuỗi mô tả phiên bản + ngày build + trình biên dịch.
    print("Phiên bản Python:", sys.version.split()[0])


# Điểm vào chương trình: chỉ chạy main() khi file được chạy trực tiếp,
# không chạy khi file bị import như một module.
if __name__ == "__main__":
    main()
