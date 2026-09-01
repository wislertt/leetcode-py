def run_minimum_obstacles(solution_class: type, grid: list[list[int]]):
    implementation = solution_class()
    return implementation.minimum_obstacles(grid)


def assert_minimum_obstacles(result: int, expected: int) -> bool:
    assert result == expected
    return True
