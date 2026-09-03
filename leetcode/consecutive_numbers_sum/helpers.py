def run_consecutive_numbers_sum(solution_class: type, n: int):
    implementation = solution_class()
    return implementation.consecutive_numbers_sum(n)


def assert_consecutive_numbers_sum(result: int, expected: int) -> bool:
    assert result == expected
    return True
