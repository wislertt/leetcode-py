def run_find_nth_digit(solution_class: type, n: int):
    implementation = solution_class()
    return implementation.find_nth_digit(n)


def assert_find_nth_digit(result: int, expected: int) -> bool:
    assert result == expected
    return True
