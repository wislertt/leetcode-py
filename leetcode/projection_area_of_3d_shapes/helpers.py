def run_projection_area(solution_class: type, grid: list[list[int]]):
    implementation = solution_class()
    return implementation.projection_area(grid)


def assert_projection_area(result: int, expected: int) -> bool:
    assert result == expected
    return True
