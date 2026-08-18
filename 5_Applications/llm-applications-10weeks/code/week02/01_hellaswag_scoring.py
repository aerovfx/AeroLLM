# Tuần 02 · Bài 01: Chấm điểm multiple-choice (HellaSwag-style).
# Mục tiêu: Hiểu chấm điểm log-likelihood chuẩn hoá độ dài và baseline ngẫu nhiên.
# Đầu vào: Bộ câu MCQ giả (ngữ cảnh + 4 lựa chọn + đáp án đúng) và "mô hình giả".
# Đầu ra: Điểm từng lựa chọn, dự đoán, accuracy và baseline 25%.
# Cách chạy: python 01_hellaswag_scoring.py
# Lưu ý an toàn: Dữ liệu giả; chỉ minh hoạ cơ chế chấm điểm, không đánh giá mô hình thật.

import math
import random


def length_normalized_score(context, choice, model_logprob):
    """Tính điểm = trung bình log-prob của từng token trong lựa chọn.

    model_logprob(ctx, token) trả về log xác suất mô hình gán cho token.
    Chuẩn hoá theo độ dài để đáp án dài không bị phạt vô cớ.
    """
    tokens = choice.split()
    if not tokens:
        return float("-inf")  # Lựa chọn rỗng không hợp lệ.
    total = sum(model_logprob(context, tok) for tok in tokens)
    return total / len(tokens)


def make_fake_model(seed=0):
    """Mô phỏng một mô hình: gán log-prob ngẫu nhiên nhưng có seed.

    Không phải mô hình thật; chỉ để minh hoạ luồng chấm điểm.
    """
    rng = random.Random(seed)
    def logprob(context, token):
        # Giả định mô hình "thích" token đúng hơn nếu token là từ khoá của đáp án.
        base = rng.uniform(-2.5, -0.5)
        return base
    return logprob


def main():
    # Bộ MCQ giả: mỗi câu có context, 4 lựa chọn, chỉ số đáp án đúng.
    mcq = [
        {"context": "A person is cooking in the kitchen.",
         "choices": ["start slicing vegetables", "jump into a pool",
                     "fly into space", "dissolve into smoke"],
         "answer": 0},
        {"context": "The driver saw the red light and",
         "choices": ["stopped the car", "kept singing", "flew away", "grew taller"],
         "answer": 0},
        {"context": "To make tea, first boil water then",
         "choices": ["add tea leaves", "paint the wall", "melt ice", "call a taxi"],
         "answer": 0},
        {"context": "When it rains, people usually",
         "choices": ["open an umbrella", "water plants", "sunbathe", "climb a rope"],
         "answer": 0},
    ]

    model = make_fake_model(seed=7)
    correct = 0
    for item in mcq:
        scores = [length_normalized_score(item["context"], c, model)
                  for c in item["choices"]]
        pred = scores.index(max(scores))  # argmax.
        if pred == item["answer"]:
            correct += 1
        print(f"pred={pred} true={item['answer']} scores="
              f"{[round(s, 2) for s in scores]}")

    accuracy = correct / len(mcq)
    print(f"\nAccuracy mô hình giả: {accuracy:.2f}")
    print("Baseline ngẫu nhiên (4 lựa chọn): 0.25")
    print("Lưu ý: độ dài chuẩn hoá ngăn phạt lựa chọn dài; "
          "mô hình giả ở đây gần ngẫu nhiên.")


if __name__ == "__main__":
    main()
