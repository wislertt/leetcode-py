def run_profitable_schemes(
    solution_class: type, n: int, min_profit: int, group: list[int], profit: list[int]
):
    implementation = solution_class()
    return implementation.profitable_schemes(n, min_profit, group, profit)


def assert_profitable_schemes(result: int, expected: int) -> bool:
    assert result == expected
    return True
