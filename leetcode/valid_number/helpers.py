def run_is_number(solution_class: type, s: str):
    implementation = solution_class()
    return implementation.is_number(s)


def assert_is_number(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
