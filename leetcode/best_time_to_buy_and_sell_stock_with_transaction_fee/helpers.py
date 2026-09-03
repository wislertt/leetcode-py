def run_max_profit(solution_class: type, prices: list[int], fee: int):
    implementation = solution_class()
    return implementation.max_profit(prices, fee)


def assert_max_profit(result: int, expected: int) -> bool:
    assert result == expected
    return True
