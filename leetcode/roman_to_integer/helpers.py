def run_roman_to_int(solution_class: type, s: str):
    implementation = solution_class()
    return implementation.roman_to_int(s)


def assert_roman_to_int(result: int, expected: int) -> bool:
    assert result == expected
    return True
