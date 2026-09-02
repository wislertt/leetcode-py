def run_max_profit(solution_class: type, k: int, prices: list[int]):
    implementation = solution_class()
    return implementation.max_profit(k, prices)


def assert_max_profit(result: int, expected: int) -> bool:
    assert result == expected
    return True
