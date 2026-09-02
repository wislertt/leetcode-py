def run_is_match(solution_class: type, s: str, p: str):
    implementation = solution_class()
    return implementation.is_match(s, p)


def assert_is_match(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
