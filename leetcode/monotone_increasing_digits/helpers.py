def run_monotone_increasing_digits(solution_class: type, n: int):
    implementation = solution_class()
    return implementation.monotone_increasing_digits(n)


def assert_monotone_increasing_digits(result: int, expected: int) -> bool:
    assert result == expected
    return True
