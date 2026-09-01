def run_final_prices(solution_class: type, prices: list[int]):
    implementation = solution_class()
    return implementation.final_prices(prices)


def assert_final_prices(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
