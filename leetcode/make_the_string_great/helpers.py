def run_make_good(solution_class: type, s: str):
    implementation = solution_class()
    return implementation.make_good(s)


def assert_make_good(result: str, expected: str) -> bool:
    assert result == expected
    return True
