def run_min_reorder(solution_class: type, n: int, connections: list[list[int]]):
    implementation = solution_class()
    return implementation.min_reorder(n, connections)


def assert_min_reorder(result: int, expected: int) -> bool:
    assert result == expected
    return True
