def run_min_steps(solution_class: type, n: int):
    implementation = solution_class()
    return implementation.min_steps(n)


def assert_min_steps(result: int, expected: int) -> bool:
    assert result == expected
    return True
