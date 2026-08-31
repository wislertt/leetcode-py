def run_eventual_safe_nodes(solution_class: type, graph: list[list[int]]):
    implementation = solution_class()
    return implementation.eventual_safe_nodes(graph)


def assert_eventual_safe_nodes(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
