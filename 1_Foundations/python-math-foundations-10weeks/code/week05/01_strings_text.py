# Tuần 05 · Bài 01: f-string và xử lý văn bản.
# Mục tiêu: Nội suy chuỗi bằng f-string; đọc file local và đếm tần suất từ.
# Đầu vào: File data.txt do người học tự tạo (vài dòng văn bản giả).
# Đầu ra: Chuỗi f-string và 5 từ phổ biến nhất.
# Cách chạy: python code/week05/01_strings_text.py
# Lưu ý an toàn: Chỉ đọc file local; không đọc file hệ thống; đóng file bằng with.


def read_words(path):
    """Đọc file văn bản và trả về danh sách từ đã làm sạch (chữ thường).

    Dùng context manager `with` để file tự đóng dù có lỗi xảy ra.
    """
    # open(path, encoding="utf-8") đọc file dưới dạng chuỗi UTF-8.
    with open(path, encoding="utf-8") as f:
        text = f.read()  # Đọc toàn bộ nội dung file.

    # lower() chuyển chữ thường; split() tách theo khoảng trắng thành các từ.
    return text.lower().split()


def count_words(words):
    """Trả về dict đếm số lần xuất hiện của từng từ."""
    counts = {}  # Khởi tạo dict rỗng.
    # Duyệt từng từ; get(word, 0) trả về 0 nếu từ chưa có trong dict.
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts


def main():
    # f-string: chèn giá trị biến vào chuỗi.
    name, score = "An", 8.5
    print(f"{name} đạt {score} điểm")

    # Thử xử lý một chuỗi mẫu không cần file.
    sample = "  Xin Chào Các Bạn  "
    print("Làm sạch:", sample.strip().lower().split())

    # Đọc file data.txt (nếu thiếu file thì in hướng dẫn, không crash).
    path = "data.txt"
    try:
        words = read_words(path)
    except FileNotFoundError:
        print(f"Không tìm thấy {path}. Hãy tạo file này trước khi chạy.")
        return

    # Đếm tần suất và in 5 từ phổ biến nhất theo thứ tự giảm dần.
    counts = count_words(words)
    top = sorted(counts.items(), key=lambda kv: kv[1], reverse=True)[:5]
    print("5 từ phổ biến nhất:")
    for word, freq in top:
        print(f"  {word}: {freq}")


if __name__ == "__main__":
    main()
