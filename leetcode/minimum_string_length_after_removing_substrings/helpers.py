def run_min_length(solution_class: type, s: str):
    implementation = solution_class()
    return implementation.min_length(s)


def assert_min_length(result: int, expected: int) -> bool:
    assert result == expected
    return True
