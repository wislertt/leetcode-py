def run_min_changes(solution_class: type, s: str):
    implementation = solution_class()
    return implementation.min_changes(s)


def assert_min_changes(result: int, expected: int) -> bool:
    assert result == expected
    return True
