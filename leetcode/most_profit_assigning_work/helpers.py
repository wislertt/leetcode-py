def run_max_profit_assignment(
    solution_class: type, difficulty: list[int], profit: list[int], worker: list[int]
):
    implementation = solution_class()
    return implementation.max_profit_assignment(difficulty, profit, worker)


def assert_max_profit_assignment(result: int, expected: int) -> bool:
    assert result == expected
    return True
