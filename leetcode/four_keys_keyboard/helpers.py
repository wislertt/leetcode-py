def run_max_a(solution_class: type, n: int):
    implementation = solution_class()
    return implementation.max_a(n)


def assert_max_a(result: int, expected: int) -> bool:
    assert result == expected
    return True
