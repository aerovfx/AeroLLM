"""Tạo payload Kimi K3 multi-turn offline; không gọi mạng và không cần API key."""

from copy import deepcopy


def append_assistant_message(history: list[dict], assistant_message: dict) -> list[dict]:
    """Nối nguyên assistant message để giữ thinking/tool state qua nhiều lượt."""
    # Ba field này tạo nên trạng thái assistant mà model card yêu cầu giữ lại.
    required_fields = {"content", "reasoning_content", "tool_calls"}
    # Báo lỗi sớm nếu client đã vô tình chỉ lưu phần câu trả lời hiển thị.
    missing_fields = required_fields.difference(assistant_message)
    if missing_fields:
        raise ValueError(f"Assistant message thiếu field: {sorted(missing_fields)}")
    # Deep-copy tránh caller sửa nested tool calls sau khi history đã được tạo.
    updated_history = deepcopy(history)
    updated_history.append(deepcopy(assistant_message))
    return updated_history


def build_request(history: list[dict], effort: str = "high") -> dict:
    """Tạo request body có validation cho reasoning effort."""
    # Model card hiện công bố ba mức này; không gửi giá trị chưa được hỗ trợ.
    allowed_efforts = {"low", "high", "max"}
    if effort not in allowed_efforts:
        raise ValueError(f"reasoning_effort phải thuộc {sorted(allowed_efforts)}")
    # Payload chỉ là dict offline; caller có thể chuyển cho client tương thích sau review.
    return {"model": "kimi-k3", "messages": deepcopy(history), "reasoning_effort": effort}


def main() -> None:
    # Bắt đầu bằng một user turn không chứa credential hoặc dữ liệu nhạy cảm.
    history = [{"role": "user", "content": "Tính 7 × 8 và giải thích ngắn."}]
    # Mô phỏng object do API trả về; production phải lưu nguyên object thực tế.
    assistant_message = {
        "role": "assistant",
        "reasoning_content": "internal reasoning placeholder",
        "content": "7 × 8 = 56.",
        "tool_calls": [],
    }
    history = append_assistant_message(history, assistant_message)
    # Thêm lượt user tiếp theo sau khi preserved assistant state đã được nối.
    history.append({"role": "user", "content": "Nhân kết quả đó với 2."})
    request = build_request(history, effort="high")
    # Chỉ in metadata an toàn; tuyệt đối không log reasoning_content trong lab.
    print({"model": request["model"], "turns": len(request["messages"]), "effort": request["reasoning_effort"]})


if __name__ == "__main__":
    # Entry point chạy demo offline và không thực hiện network request.
    main()

