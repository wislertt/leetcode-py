def run_count_complete_components(solution_class: type, n: int, edges: list[list[int]]):
    implementation = solution_class()
    return implementation.count_complete_components(n, edges)


def assert_count_complete_components(result: int, expected: int) -> bool:
    assert result == expected
    return True
