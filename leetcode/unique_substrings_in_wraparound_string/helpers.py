def run_find_substring_in_wrapround_string(solution_class: type, s: str):
    implementation = solution_class()
    return implementation.find_substring_in_wrapround_string(s)


def assert_find_substring_in_wrapround_string(result: int, expected: int) -> bool:
    assert result == expected
    return True
