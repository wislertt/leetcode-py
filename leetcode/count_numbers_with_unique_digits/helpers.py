def run_count_numbers_with_unique_digits(solution_class: type, n: int):
    implementation = solution_class()
    return implementation.count_numbers_with_unique_digits(n)


def assert_count_numbers_with_unique_digits(result: int, expected: int) -> bool:
    assert result == expected
    return True
