def run_max_count(solution_class: type, m: int, n: int, ops: list[list[int]]):
    implementation = solution_class()
    return implementation.max_count(m, n, ops)


def assert_max_count(result: int, expected: int) -> bool:
    assert result == expected
    return True
