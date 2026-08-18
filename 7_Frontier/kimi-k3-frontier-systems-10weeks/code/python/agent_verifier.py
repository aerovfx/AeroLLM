"""Verifier-first toy environment inspired by Autonomous Execution Tasks."""

from dataclasses import dataclass


@dataclass
class TaskState:
    # Balance là trạng thái thật mà verifier kiểm tra, không dựa vào lời tự báo cáo.
    balance: int = 0
    # actions ghi lại chi phí tương tác để áp execution budget.
    actions: int = 0


def act(state: TaskState, amount: int) -> None:
    """Một tool action có side effect rõ ràng lên environment state."""
    # Mỗi lần gọi tool phải tăng action count trước khi thay đổi state.
    state.actions += 1
    # Toy action cộng amount; production environment cần validate schema/quyền.
    state.balance += amount


def verify(state: TaskState, target: int, budget: int) -> dict[str, object]:
    """Chấm final state và hard budget độc lập với câu trả lời của agent."""
    # Success chỉ đúng khi cả goal lẫn budget đều đạt.
    goal_ok = state.balance == target
    budget_ok = state.actions <= budget
    return {"goal_ok": goal_ok, "budget_ok": budget_ok, "reward": int(goal_ok and budget_ok)}


def main() -> None:
    state = TaskState()
    # Hai action đạt target 10 trong budget 3.
    act(state, 6)
    act(state, 4)
    result = verify(state, target=10, budget=3)
    assert result["reward"] == 1
    print(result)


if __name__ == "__main__":
    main()

