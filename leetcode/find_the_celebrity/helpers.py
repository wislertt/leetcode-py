def run_find_celebrity(solution_class: type, graph: list[list[int]]):
    implementation = solution_class()
    # The knows API is backed by the graph only via injection
    implementation.graph = graph
    return implementation.find_celebrity(len(graph))


def assert_find_celebrity(result: int, expected: int) -> bool:
    assert result == expected
    return True
