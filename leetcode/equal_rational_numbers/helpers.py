def run_is_rational_equal(solution_class: type, s: str, t: str):
    implementation = solution_class()
    return implementation.is_rational_equal(s, t)


def assert_is_rational_equal(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
