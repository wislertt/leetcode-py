def run_largest_island(solution_class: type, grid: list[list[int]]):
    implementation = solution_class()
    return implementation.largest_island(grid)


def assert_largest_island(result: int, expected: int) -> bool:
    assert result == expected
    return True
