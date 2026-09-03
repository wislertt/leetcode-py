def run_shortest_path_length(solution_class: type, graph: list[list[int]]):
    implementation = solution_class()
    return implementation.shortest_path_length(graph)


def assert_shortest_path_length(result: int, expected: int) -> bool:
    assert result == expected
    return True
