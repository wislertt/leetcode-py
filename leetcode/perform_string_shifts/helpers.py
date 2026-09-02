def run_string_shift(solution_class: type, s: str, shift: list[list[int]]):
    implementation = solution_class()
    return implementation.string_shift(s, shift)


def assert_string_shift(result: str, expected: str) -> bool:
    assert result == expected
    return True
