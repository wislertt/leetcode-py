def run_max_difference(solution_class: type, s: str):
    implementation = solution_class()
    return implementation.max_difference(s)


def assert_max_difference(result: int, expected: int) -> bool:
    assert result == expected
    return True
