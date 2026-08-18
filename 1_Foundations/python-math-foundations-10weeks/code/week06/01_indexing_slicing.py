# Tuần 06 · Bài 01: Indexing và slicing cho list và chuỗi.
# Mục tiêu: Truy cập phần tử bằng chỉ mục dương/âm; cắt lát start:stop:step.
# Đầu vào: Danh sách số và chuỗi giả.
# Đầu ra: Các phần tử và lát cắt được in ra.
# Cách chạy: python code/week06/01_indexing_slicing.py
# Lưu ý an toàn: Chỉ thao tác dữ liệu giả; lưu ý slicing chuỗi là chuỗi mới.


def main():
    data = [10, 20, 30, 40, 50]

    # Chỉ mục dương đếm từ đầu (0), chỉ mục âm đếm từ cuối (-1).
    print("Phần tử đầu:", data[0])
    print("Phần tử cuối:", data[-1])
    print("Phần tử thứ ba:", data[2])

    # Slicing data[start:stop:step]: lấy từ start đến trước stop.
    print("\nSlicing danh sách:")
    print("data[1:4]   =", data[1:4])     # [20, 30, 40] (stop=4 loại trừ).
    print("data[:3]    =", data[:3])      # Từ đầu đến trước chỉ mục 3.
    print("data[3:]    =", data[3:])      # Từ chỉ mục 3 đến hết.
    print("data[::2]   =", data[::2])     # Bước 2: phần tử vị trí 0, 2, 4.
    print("data[::-1]  =", data[::-1])    # Bước -1: đảo ngược danh sách.

    # Chuỗi cũng cắt lát được (theo ký tự).
    word = "python"
    print("\nSlicing chuỗi:")
    print("word[1:4] =", word[1:4])       # 'yth'.
    print("word[:2]  =", word[:2])        # 'py' (2 ký tự đầu).
    print("word[-2:] =", word[-2:])       # 'on' (2 ký tự cuối).

    # Thử chỉ mục ngoài phạm vi để quan sát IndexError.
    try:
        print(data[100])
    except IndexError as e:
        print("\nIndexError:", e)


if __name__ == "__main__":
    main()
