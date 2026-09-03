def run_rotated_digits(solution_class: type, n: int):
    implementation = solution_class()
    return implementation.rotated_digits(n)


def assert_rotated_digits(result: int, expected: int) -> bool:
    assert result == expected
    return True
