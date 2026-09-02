def run_count_digit_one(solution_class: type, n: int):
    implementation = solution_class()
    return implementation.count_digit_one(n)


def assert_count_digit_one(result: int, expected: int) -> bool:
    assert result == expected
    return True
