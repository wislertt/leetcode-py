def run_min_end(solution_class: type, n: int, x: int):
    implementation = solution_class()
    return implementation.min_end(n, x)


def assert_min_end(result: int, expected: int) -> bool:
    assert result == expected
    return True
