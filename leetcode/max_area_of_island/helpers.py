def run_max_area_of_island(solution_class: type, grid: list[list[int]]):
    implementation = solution_class()
    return implementation.max_area_of_island(grid)


def assert_max_area_of_island(result: int, expected: int) -> bool:
    assert result == expected
    return True
