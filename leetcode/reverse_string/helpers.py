def run_reverse_string(solution_class: type, s: list[str]):
    s_copy = s.copy()
    implementation = solution_class()
    implementation.reverse_string(s_copy)
    return s_copy


def assert_reverse_string(result: list[str], expected: list[str]) -> bool:
    assert result == expected
    return True
