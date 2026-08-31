def run_shortest_alternating_paths(
    solution_class: type, n: int, red_edges: list[list[int]], blue_edges: list[list[int]]
):
    implementation = solution_class()
    return implementation.shortest_alternating_paths(n, red_edges, blue_edges)


def assert_shortest_alternating_paths(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
