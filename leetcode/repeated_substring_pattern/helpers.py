def run_repeated_substring_pattern(solution_class: type, s: str):
    implementation = solution_class()
    return implementation.repeated_substring_pattern(s)


def assert_repeated_substring_pattern(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
