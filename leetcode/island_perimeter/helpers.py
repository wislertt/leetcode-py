def run_island_perimeter(solution_class: type, grid: list[list[int]]):
    implementation = solution_class()
    return implementation.island_perimeter(grid)


def assert_island_perimeter(result: int, expected: int) -> bool:
    assert result == expected
    return True
