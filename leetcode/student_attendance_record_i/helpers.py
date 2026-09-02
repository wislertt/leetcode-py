def run_check_record(solution_class: type, s: str):
    implementation = solution_class()
    return implementation.check_record(s)


def assert_check_record(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
