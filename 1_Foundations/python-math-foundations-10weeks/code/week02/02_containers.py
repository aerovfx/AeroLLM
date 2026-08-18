# Tuần 02 · Bài 02: list và dict.
# Mục tiêu: Dùng list (dãy có thứ tự) và dict (khóa -> giá trị), truy cập phần tử.
# Đầu vào: Danh sách điểm và thông tin sinh viên giả.
# Đầu ra: In các phần tử truy cập theo chỉ mục và theo khóa.
# Cách chạy: python code/week02/02_containers.py
# Lưu ý an toàn: Dữ liệu giả; không dùng thông tin người thật.


def main():
    # list: dãy có thứ tự, truy cập bằng chỉ mục bắt đầu từ 0.
    scores = [8, 9, 7, 10]

    # Truy cập phần tử đầu (chỉ mục 0) và phần tử cuối (chỉ mục -1).
    print("Điểm đầu:", scores[0])
    print("Điểm cuối:", scores[-1])

    # len() trả về số phần tử trong list.
    print("Số môn:", len(scores))

    # Thêm phần tử vào list rồi in lại.
    scores.append(6)   # append thêm vào cuối list.
    print("Sau khi thêm:", scores)

    # dict: ánh xạ khóa -> giá trị; truy cập bằng khóa.
    student = {"name": "An", "age": 21, "score": 8.5}
    print("\nTên:", student["name"])
    print("Tuổi:", student["age"])

    # Lặp qua các cặp khóa/giá trị của dict bằng items().
    print("Toàn bộ thông tin:")
    for key, value in student.items():
        print(f"  {key} = {value}")


if __name__ == "__main__":
    main()
