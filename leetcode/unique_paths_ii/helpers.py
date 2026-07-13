def run_unique_paths_with_obstacles(solution_class: type, grid: list[list[int]]):
    implementation = solution_class()
    return implementation.unique_paths_with_obstacles(grid)


def assert_unique_paths_with_obstacles(result: int, expected: int) -> bool:
    assert result == expected
    return True
