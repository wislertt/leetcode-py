def run_max_score(solution_class: type, s: str):
    implementation = solution_class()
    return implementation.max_score(s)


def assert_max_score(result: int, expected: int) -> bool:
    assert result == expected
    return True
