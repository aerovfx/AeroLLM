# Tuần 08 · Bài 02: Threat model (risk = likelihood x impact).
# Mục tiêu: Liệt kê tài sản, tác nhân, rủi ro và chấm điểm để xếp hạng ưu tiên.
# Đầu vào: Bảng rủi ro giả định cho ứng dụng RAG nội bộ.
# Đầu ra: Điểm rủi ro và danh sách xếp hạng.
# Cách chạy: python 02_threat_model.py
# Lưu ý an toàn: Threat model là tài liệu sống; cập nhật khi hệ thống thay đổi.

def score_risk(likelihood, impact):
    """Nhân likelihood (1-5) với impact (1-5) ra điểm rủi ro 1-25."""
    return likelihood * impact


def main():
    # Mỗi rủi ro: (mô tả, tác nhân, likelihood 1-5, impact 1-5, biện pháp).
    risks = [
        ("Hallucination ngoài ngữ cảnh", "lỗi hệ thống", 4, 3,
         "chỉ trả lời từ context + kiểm tra groundedness"),
        ("Prompt injection đọc dữ liệu khác", "kẻ tấn công", 3, 5,
         "lọc input + cô lập context khỏi chỉ thị hệ thống"),
        ("Rò rỉ dữ liệu nhạy cảm", "kẻ tấn công", 2, 5,
         "chỉ dùng dữ liệu giả + mask PII"),
        ("Retrieval sai nguồn", "lỗi hệ thống", 4, 3,
         "re-rank + ngưỡng similarity + trích nguồn"),
    ]
    scored = []
    for desc, actor, lik, imp, mit in risks:
        s = score_risk(lik, imp)
        scored.append((s, desc, actor, lik, imp, mit))

    # Sắp xếp giảm dần để ưu tiên rủi ro cao nhất.
    scored.sort(key=lambda x: x[0], reverse=True)
    print("Xếp hạng rủi ro (điểm giảm dần):")
    for s, desc, actor, lik, imp, mit in scored:
        print(f"  [{s:2d}] {desc} (actor={actor}, L={lik}, I={imp}) -> {mit}")


if __name__ == "__main__":
    main()
