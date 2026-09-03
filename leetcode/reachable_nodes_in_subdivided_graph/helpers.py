def run_reachable_nodes(solution_class: type, edges: list[list[int]], max_moves: int, n: int):
    implementation = solution_class()
    return implementation.reachable_nodes(edges, max_moves, n)


def assert_reachable_nodes(result: int, expected: int) -> bool:
    assert result == expected
    return True
