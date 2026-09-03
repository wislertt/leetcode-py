def run_make_largest_special(solution_class: type, s: str):
    implementation = solution_class()
    return implementation.make_largest_special(s)


def assert_make_largest_special(result: str, expected: str) -> bool:
    assert result == expected
    return True
