def run_max_distance(solution_class: type, grid: list[list[int]]):
    implementation = solution_class()
    return implementation.max_distance(grid)


def assert_max_distance(result: int, expected: int) -> bool:
    assert result == expected
    return True
