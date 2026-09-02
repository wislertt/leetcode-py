def run_minimum_length(solution_class: type, s: str):
    implementation = solution_class()
    return implementation.minimum_length(s)


def assert_minimum_length(result: int, expected: int) -> bool:
    assert result == expected
    return True
