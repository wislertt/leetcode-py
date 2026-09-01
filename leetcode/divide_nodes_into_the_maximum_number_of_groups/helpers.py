def run_magnificent_sets(solution_class: type, n: int, edges: list[list[int]]):
    implementation = solution_class()
    return implementation.magnificent_sets(n, edges)


def assert_magnificent_sets(result: int, expected: int) -> bool:
    assert result == expected
    return True
