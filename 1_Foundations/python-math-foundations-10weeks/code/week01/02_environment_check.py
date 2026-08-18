# Tuần 01 · Bài 02: Kiểm tra môi trường Python.
# Mục tiêu: In phiên bản Python, nền tảng và kiểm tra module có sẵn.
# Đầu vào: Không cần đầu vào.
# Đầu ra: Bảng thông tin môi trường in ra màn hình.
# Cách chạy: python code/week01/02_environment_check.py
# Lưu ý an toàn: Chỉ đọc thông tin môi trường; không kết nối mạng, không secret.

# sys cung cấp thông tin phiên bản và nền tảng đang chạy.
import sys
# platform cung cấp tên hệ điều hành và kiến trúc máy.
import platform


def check_optional_modules():
    """Thử import các module hay dùng và báo có/không.

    Dùng try/except để không làm script dừng khi thiếu một module tuỳ chọn.
    """
    # Danh sách module cần kiểm tra: tên import -> mô tả ngắn.
    modules = {
        "numpy": "NumPy (tính toán số)",
        "matplotlib": "Matplotlib (vẽ biểu đồ)",
        "torch": "PyTorch (học sâu)",
    }
    # Duyệt từng cặp (tên, mô tả) trong dictionary modules.
    for name, desc in modules.items():
        try:
            # __import__ thử nạp module; nếu lỗi thì rơi vào except.
            __import__(name)
            print(f"  [OK]   {name:12s} — {desc}")
        except ImportError:
            # ImportError xảy ra khi module chưa được cài đặt.
            print(f"  [THIẾU] {name:12s} — {desc} (cài: pip install {name})")


def main():
    # In tiêu đề của bảng kiểm tra.
    print("=== KIỂM TRA MÔI TRƯỜNG PYTHON ===")

    # In phiên bản Python (phần đầu của sys.version).
    print("Phiên bản Python :", sys.version.split()[0])

    # In hệ điều hành và kiến trúc máy (ví dụ macOS-14-arm64).
    print("Nền tảng         :", platform.platform())

    # Kiểm tra các module tuỳ chọn thường dùng.
    print("Module tuỳ chọn  :")
    check_optional_modules()


if __name__ == "__main__":
    main()
