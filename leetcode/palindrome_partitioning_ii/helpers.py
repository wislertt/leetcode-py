def run_min_cut(solution_class: type, s: str):
    implementation = solution_class()
    return implementation.min_cut(s)


def assert_min_cut(result: int, expected: int) -> bool:
    assert result == expected
    return True
