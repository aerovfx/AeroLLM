"""Ước lượng bộ nhớ weights; không phải capacity planner cho production."""


def weight_memory_tb(total_parameters: float, bits_per_weight: float) -> float:
    """Đổi số tham số và số bit mỗi weight thành TB thập phân."""
    # Mỗi weight chiếm bits_per_weight / 8 byte.
    total_bytes = total_parameters * bits_per_weight / 8
    # Dùng TB thập phân để con số dễ đối chiếu với thông số ổ đĩa/network.
    return total_bytes / 1_000_000_000_000


def main() -> None:
    # Report công bố 2.8T tổng tham số; đây là toàn bộ weights, không phải 104B activated.
    parameters = 2.8e12
    # So sánh lower bound lý thuyết; runtime còn cần metadata, cache và workspace.
    for bits in (16, 8, 4):
        memory = weight_memory_tb(parameters, bits)
        print(f"{bits:>2}-bit weights: at least {memory:.2f} TB")

    # 104B activated mô tả compute mỗi token, không làm biến mất weights chưa được chọn.
    activated_fraction = 104e9 / parameters
    print(f"Activated fraction per token: {activated_fraction:.2%}")


if __name__ == "__main__":
    # Chỉ chạy demo khi gọi file trực tiếp; import không tạo side effect.
    main()

