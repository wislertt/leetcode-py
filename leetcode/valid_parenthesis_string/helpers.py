def run_check_valid_string(solution_class: type, s: str):
    implementation = solution_class()
    return implementation.check_valid_string(s)


def assert_check_valid_string(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
