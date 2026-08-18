# Tuần 06 · Bài 03: Multi-hop RAG (truy xuất lặp hai vòng).
# Mục tiêu: Minh hoạ truy xuất nhiều vòng khi câu hỏi cần nối nhiều mảnh thông tin.
# Đầu vào: Kho văn bản giả + câu hỏi nhiều bước.
# Đầu ra: Kết quả truy xuất vòng 1 và vòng 2.
# Cách chạy: python 03_multi_hop.py
# Lưu ý an toàn: Multi-hop có thể lan truyền lỗi vòng đầu; đây là minh hoạ local.

import re


def tokenize(text):
    return re.findall(r"[a-z0-9]+", text.lower())


def retrieve(query, documents):
    """Truy xuất đơn giản theo số từ trùng lặp (lexical)."""
    scored = sorted(documents, key=lambda d: len(set(tokenize(query)) & set(tokenize(d))),
                    reverse=True)
    return scored[:2]


def extract_entity(text):
    """Rút một thực thể giả định từ câu (từ viết hoa). Đây là heuristic đơn giản."""
    for w in re.findall(r"[A-Z][a-zA-Z]+", text):
        return w
    return None


def main():
    documents = [
        "Acme Corp was acquired by Globex in 2023.",
        "The CEO of Globex is Alice Nguyen.",
        "Globex is headquartered in Hanoi.",
        "Alice Nguyen joined Globex in 2019.",
    ]
    question = "Who is the CEO of the company that acquired Acme Corp?"

    # Vòng 1: tìm ai đã mua Acme Corp.
    hop1 = retrieve("who acquired Acme Corp", documents)
    print("Vòng 1:", hop1)
    # Rút thực thể "Globex" từ kết quả vòng 1.
    entity = extract_entity(" ".join(hop1)) or "Globex"
    print("Thực thể rút ra:", entity)

    # Vòng 2: hỏi CEO của Globex.
    hop2 = retrieve(f"CEO of {entity}", documents)
    print("Vòng 2:", hop2)
    print("Câu trả lời (mock):", hop2[0] if hop2 else "không tìm thấy")


if __name__ == "__main__":
    main()
