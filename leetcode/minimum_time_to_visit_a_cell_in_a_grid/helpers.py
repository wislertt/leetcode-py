def run_minimum_time(solution_class: type, grid: list[list[int]]):
    implementation = solution_class()
    return implementation.minimum_time(grid)


def assert_minimum_time(result: int, expected: int) -> bool:
    assert result == expected
    return True
