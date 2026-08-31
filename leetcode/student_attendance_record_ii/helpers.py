def run_check_record(solution_class: type, n: int):
    implementation = solution_class()
    return implementation.check_record(n)


def assert_check_record(result: int, expected: int) -> bool:
    assert result == expected
    return True
