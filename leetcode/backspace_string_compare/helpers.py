def run_backspace_compare(solution_class: type, s: str, t: str):
    implementation = solution_class()
    return implementation.backspace_compare(s, t)


def assert_backspace_compare(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
