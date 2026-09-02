def run_min_deletions(solution_class: type, s: str):
    implementation = solution_class()
    return implementation.min_deletions(s)


def assert_min_deletions(result: int, expected: int) -> bool:
    assert result == expected
    return True
