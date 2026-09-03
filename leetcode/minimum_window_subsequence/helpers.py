def run_min_window(solution_class: type, s1: str, s2: str):
    implementation = solution_class()
    return implementation.min_window(s1, s2)


def assert_min_window(result: str, expected: str) -> bool:
    assert result == expected
    return True
