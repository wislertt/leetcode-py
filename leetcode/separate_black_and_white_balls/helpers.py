def run_minimum_steps(solution_class: type, s: str):
    implementation = solution_class()
    return implementation.minimum_steps(s)


def assert_minimum_steps(result: int, expected: int) -> bool:
    assert result == expected
    return True
