def run_shortest_bridge(solution_class: type, grid: list[list[int]]):
    implementation = solution_class()
    return implementation.shortest_bridge(grid)


def assert_shortest_bridge(result: int, expected: int) -> bool:
    assert result == expected
    return True
