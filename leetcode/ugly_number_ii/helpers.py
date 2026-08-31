def run_nth_ugly_number(solution_class: type, n: int):
    implementation = solution_class()
    return implementation.nth_ugly_number(n)


def assert_nth_ugly_number(result: int, expected: int) -> bool:
    assert result == expected
    return True
