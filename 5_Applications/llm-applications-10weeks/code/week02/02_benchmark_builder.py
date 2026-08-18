# Tuần 02 · Bài 02: Sinh bộ benchmark tổng hợp có nhãn.
# Mục tiêu: Tự xây một benchmark nhỏ có metadata (độ khó, chủ đề) và baseline.
# Đầu vào: Mẫu câu hỏi định nghĩa sẵn (dữ liệu giả).
# Đầu ra: Danh sách câu hỏi có nhãn, thống kê theo nhóm, accuracy baseline.
# Cách chạy: python 02_benchmark_builder.py
# Lưu ý an toàn: Benchmark chỉ để học; không dùng để công bố so sánh mô hình thật.

import json
import random


def build_benchmark(seed=3):
    """Sinh bộ benchmark giả với 4 chủ đề x 5 câu, gán độ khó và đáp án.

    Trả về list dict; mỗi dict có id, topic, difficulty, prompt, choices, answer.
    """
    rng = random.Random(seed)
    topics = ["physics", "cooking", "travel", "programming"]
    templates = {
        "physics": "What happens when you drop an object?",
        "cooking": "What is the first step to boil pasta?",
        "travel": "What do you need to board a plane?",
        "programming": "What does a loop do?",
    }
    benchmark = []
    for topic in topics:
        for i in range(5):
            difficulty = "easy" if i < 3 else "hard"
            choices = [f"{topic} option {i}_{j}" for j in range(4)]
            answer = rng.randrange(4)
            benchmark.append({
                "id": f"{topic}-{i:02d}",
                "topic": topic,
                "difficulty": difficulty,
                "prompt": templates[topic],
                "choices": choices,
                "answer": answer,
            })
    return benchmark


def main():
    benchmark = build_benchmark()

    # Thống kê theo chủ đề để thấy phân bố (tránh benchmark lệch một chủ đề).
    by_topic = {}
    for item in benchmark:
        by_topic.setdefault(item["topic"], 0)
        by_topic[item["topic"]] += 1
    print("Phân bố theo chủ đề:", by_topic)

    # Baseline ngẫu nhiên = 1 / số lựa chọn (4).
    print("Baseline ngẫu nhiên:", 1 / 4)

    # Ghi ra JSON để bài nộp có file dữ liệu minh bạch, tái lập được.
    out = "benchmark_fake.json"
    with open(out, "w", encoding="utf-8") as f:
        json.dump(benchmark, f, ensure_ascii=False, indent=2)
    print(f"Đã ghi {len(benchmark)} câu vào {out}")


if __name__ == "__main__":
    main()
