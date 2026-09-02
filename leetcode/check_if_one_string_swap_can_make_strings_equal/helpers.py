def run_are_almost_equal(solution_class: type, s1: str, s2: str):
    implementation = solution_class()
    return implementation.are_almost_equal(s1, s2)


def assert_are_almost_equal(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
