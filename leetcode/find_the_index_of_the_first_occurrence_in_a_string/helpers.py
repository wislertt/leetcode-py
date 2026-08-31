def run_str_str(solution_class: type, haystack: str, needle: str):
    implementation = solution_class()
    return implementation.str_str(haystack, needle)


def assert_str_str(result: int, expected: int) -> bool:
    assert result == expected
    return True
