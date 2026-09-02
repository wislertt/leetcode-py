def run_add_digits(solution_class: type, num: int):
    implementation = solution_class()
    return implementation.add_digits(num)


def assert_add_digits(result: int, expected: int) -> bool:
    assert result == expected
    return True
