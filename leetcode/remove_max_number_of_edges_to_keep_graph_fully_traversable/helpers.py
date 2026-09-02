def run_max_num_edges_to_remove(solution_class: type, n: int, edges: list[list[int]]):
    implementation = solution_class()
    return implementation.max_num_edges_to_remove(n, edges)


def assert_max_num_edges_to_remove(result: int, expected: int) -> bool:
    assert result == expected
    return True
