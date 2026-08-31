def run_minimize_error(solution_class: type, prices: list[str], target: int):
    implementation = solution_class()
    return implementation.minimize_error(prices, target)


def assert_minimize_error(result: str, expected: str) -> bool:
    assert result == expected
    return True
