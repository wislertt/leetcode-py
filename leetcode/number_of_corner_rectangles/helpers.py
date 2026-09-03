def run_count_corner_rectangles(solution_class: type, grid: list[list[int]]):
    implementation = solution_class()
    return implementation.count_corner_rectangles(grid)


def assert_count_corner_rectangles(result: int, expected: int) -> bool:
    assert result == expected
    return True
