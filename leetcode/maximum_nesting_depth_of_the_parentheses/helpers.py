def run_max_depth(solution_class: type, s: str):
    implementation = solution_class()
    return implementation.max_depth(s)


def assert_max_depth(result: int, expected: int) -> bool:
    assert result == expected
    return True
