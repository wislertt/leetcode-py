def run_confusing_number(solution_class: type, n: int):
    implementation = solution_class()
    return implementation.confusing_number(n)


def assert_confusing_number(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
