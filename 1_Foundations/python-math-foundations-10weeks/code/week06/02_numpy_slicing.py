# Tuần 06 · Bài 02: Slicing mảng NumPy nhiều chiều.
# Mục tiêu: Cắt hàng/cột/khối của mảng 2D; phân biệt view và copy.
# Đầu vào: Mảng 3x4 sinh bằng arange/reshape.
# Đầu ra: Các hàng, cột, khối con và kết quả kiểm tra view/copy.
# Cách chạy: python code/week06/02_numpy_slicing.py
# Lưu ý an toàn: Sửa view sẽ đổi mảng gốc; dùng .copy() khi cần bản sao.

# Import NumPy với bí danh np.
import numpy as np


def main():
    # Tạo mảng 0..11 rồi đổi hình thành 3 hàng x 4 cột.
    arr = np.arange(12).reshape(3, 4)
    print("Mảng arr (3x4):")
    print(arr)

    # Cắt theo trục: arr[hang, cot]. ':' nghĩa là lấy toàn bộ trục đó.
    print("\nHàng 0   :", arr[0, :])    # Toàn bộ hàng 0.
    print("Cột 1    :", arr[:, 1])      # Toàn bộ cột 1.

    # Cắt một khối 2x2: hàng 0..1 (loại trừ 2), cột 1..2 (loại trừ 3).
    block = arr[0:2, 1:3]
    print("\nKhối 2x2 :")
    print(block)

    # Slicing NumPy trả về view (không sao chép dữ liệu).
    view = arr[0:2, 0:2]
    view[0, 0] = 999          # Sửa view sẽ đổi cả mảng gốc.
    print("\nSau khi sửa view[0,0]=999, arr:")
    print(arr)

    # Dùng .copy() để có bản sao độc lập, không ảnh hưởng mảng gốc.
    copy = arr[0:2, 0:2].copy()
    copy[0, 0] = -1
    print("arr[0,0] sau khi sửa copy:", arr[0, 0], "(không đổi)")


if __name__ == "__main__":
    main()
