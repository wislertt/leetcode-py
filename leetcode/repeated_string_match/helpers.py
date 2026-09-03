def run_repeated_string_match(solution_class: type, a: str, b: str):
    implementation = solution_class()
    return implementation.repeated_string_match(a, b)


def assert_repeated_string_match(result: int, expected: int) -> bool:
    assert result == expected
    return True
