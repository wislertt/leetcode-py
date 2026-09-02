def run_clear_digits(solution_class: type, s: str):
    implementation = solution_class()
    return implementation.clear_digits(s)


def assert_clear_digits(result: str, expected: str) -> bool:
    assert result == expected
    return True
