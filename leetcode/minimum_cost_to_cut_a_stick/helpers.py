def run_min_cost(solution_class: type, n: int, cuts: list[int]):
    implementation = solution_class()
    return implementation.min_cost(n, cuts)


def assert_min_cost(result: int, expected: int) -> bool:
    assert result == expected
    return True
