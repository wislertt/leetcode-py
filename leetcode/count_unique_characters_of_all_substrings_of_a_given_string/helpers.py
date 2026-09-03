def run_unique_letter_string(solution_class: type, s: str):
    implementation = solution_class()
    return implementation.unique_letter_string(s)


def assert_unique_letter_string(result: int, expected: int) -> bool:
    assert result == expected
    return True
