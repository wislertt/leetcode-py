def run_shortest_distance(solution_class: type, grid: list[list[int]]):
    implementation = solution_class()
    return implementation.shortest_distance(grid)


def assert_shortest_distance(result: int, expected: int) -> bool:
    assert result == expected
    return True
