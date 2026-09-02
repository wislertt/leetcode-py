def run_min_operations(solution_class: type, grid: list[list[int]], x: int):
    implementation = solution_class()
    return implementation.min_operations(grid, x)


def assert_min_operations(result: int, expected: int) -> bool:
    assert result == expected
    return True
