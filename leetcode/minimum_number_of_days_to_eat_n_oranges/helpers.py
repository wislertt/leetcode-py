def run_min_days(solution_class: type, n: int):
    implementation = solution_class()
    return implementation.min_days(n)


def assert_min_days(result: int, expected: int) -> bool:
    assert result == expected
    return True
