def run_check_perfect_number(solution_class: type, num: int):
    implementation = solution_class()
    return implementation.check_perfect_number(num)


def assert_check_perfect_number(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
