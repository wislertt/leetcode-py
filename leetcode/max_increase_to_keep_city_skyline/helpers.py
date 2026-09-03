def run_max_increase_keeping_skyline(solution_class: type, grid: list[list[int]]):
    implementation = solution_class()
    return implementation.max_increase_keeping_skyline(grid)


def assert_max_increase_keeping_skyline(result: int, expected: int) -> bool:
    assert result == expected
    return True
