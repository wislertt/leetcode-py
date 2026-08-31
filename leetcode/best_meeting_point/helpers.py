def run_min_total_distance(solution_class: type, grid: list[list[int]]):
    implementation = solution_class()
    return implementation.min_total_distance(grid)


def assert_min_total_distance(result: int, expected: int) -> bool:
    assert result == expected
    return True
