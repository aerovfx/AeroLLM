# Tuần 05 · Bài 01: Chunking (fixed + recursive) với overlap và metadata.
# Mục tiêu: Hiểu cách cắt văn bản thành chunk, giữ overlap và gán metadata.
# Đầu vào: Văn bản giả dài.
# Đầu ra: Danh sách chunk kèm metadata (id, source, start).
# Cách chạy: python 01_chunker.py
# Lưu ý an toàn: Chunk quá nhỏ làm mất ngữ cảnh; đây chỉ là minh hoạ local.

import re


def fixed_chunks(text, chunk_size=200, overlap=40, source="doc.txt"):
    """Cắt theo số ký tự cố định, giữ overlap giữa các chunk.

    Mỗi chunk có metadata để truy ngược vị trí và nguồn.
    """
    if not text:
        return []
    chunks = []
    step = chunk_size - overlap
    if step <= 0:
        raise ValueError("chunk_size phải lớn hơn overlap")
    start = 0
    i = 0
    while start < len(text):
        end = min(start + chunk_size, len(text))
        chunks.append({
            "id": f"{source}#{i}",
            "source": source,
            "start": start,
            "text": text[start:end],
        })
        i += 1
        # Khi đã chạm cuối văn bản thì dừng, tránh vòng lặp vô hạn.
        if end == len(text):
            break
        start += step
    return chunks


def recursive_chunks(text, max_chars=200, overlap=40):
    """Cắt ưu tiên theo dấu phân cách: đoạn (\n\n) -> câu -> từ.

    Đơn giản hoá: tách theo đoạn rồi cắt cố định trong từng đoạn.
    """
    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
    chunks = []
    for p in paragraphs:
        chunks.extend(fixed_chunks(p, chunk_size=max_chars, overlap=overlap))
    return chunks


def main():
    text = (
        "Our company provides health insurance to all full-time employees. "
        "Coverage begins on the first day of the month following hire.\n\n"
        "Remote work is allowed up to three days per week with manager approval. "
        "Employees must track their time in the internal system.\n\n"
        "Annual performance reviews occur every December. Salary adjustments "
        "are communicated in January."
    )
    fixed = fixed_chunks(text, chunk_size=120, overlap=30)
    print(f"Fixed chunking -> {len(fixed)} chunks:")
    for c in fixed:
        print(f"  {c['id']} [{c['start']}:{c['start']+len(c['text'])}] "
              f"{c['text'][:50]}...")

    rec = recursive_chunks(text, max_chars=120, overlap=30)
    print(f"\nRecursive chunking -> {len(rec)} chunks (tôn trọng ranh giới đoạn).")


if __name__ == "__main__":
    main()
