def run_buy_choco(solution_class: type, prices: list[int], money: int):
    implementation = solution_class()
    return implementation.buy_choco(prices, money)


def assert_buy_choco(result: int, expected: int) -> bool:
    assert result == expected
    return True
