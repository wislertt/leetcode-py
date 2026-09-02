def run_minimum_deletions(solution_class: type, s: str):
    implementation = solution_class()
    return implementation.minimum_deletions(s)


def assert_minimum_deletions(result: int, expected: int) -> bool:
    assert result == expected
    return True
