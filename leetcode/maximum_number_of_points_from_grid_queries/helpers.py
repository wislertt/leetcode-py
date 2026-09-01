def run_max_points(solution_class: type, grid: list[list[int]], queries: list[int]):
    implementation = solution_class()
    return implementation.max_points(grid, queries)


def assert_max_points(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
