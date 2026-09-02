def run_original_digits(solution_class: type, s: str):
    implementation = solution_class()
    return implementation.original_digits(s)


def assert_original_digits(result: str, expected: str) -> bool:
    assert result == expected
    return True
