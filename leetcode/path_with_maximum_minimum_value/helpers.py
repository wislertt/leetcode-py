def run_maximum_minimum_path(solution_class: type, grid: list[list[int]]):
    implementation = solution_class()
    return implementation.maximum_minimum_path(grid)


def assert_maximum_minimum_path(result: int, expected: int) -> bool:
    assert result == expected
    return True
