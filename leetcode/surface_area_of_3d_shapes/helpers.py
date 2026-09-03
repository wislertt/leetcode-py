def run_surface_area(solution_class: type, grid: list[list[int]]):
    implementation = solution_class()
    return implementation.surface_area(grid)


def assert_surface_area(result: int, expected: int) -> bool:
    assert result == expected
    return True
