def run_trailing_zeroes(solution_class: type, n: int):
    implementation = solution_class()
    return implementation.trailing_zeroes(n)


def assert_trailing_zeroes(result: int, expected: int) -> bool:
    assert result == expected, f"Expected {expected}, got {result}"
    return True
