def run_change(solution_class: type, amount: int, coins: list[int]):
    implementation = solution_class()
    return implementation.change(amount, coins)


def assert_change(result: int, expected: int) -> bool:
    assert result == expected
    return True
