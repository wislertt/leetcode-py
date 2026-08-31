def run_shift_grid(solution_class: type, grid: list[list[int]], k: int):
    implementation = solution_class()
    return implementation.shift_grid(grid, k)


def assert_shift_grid(result: list[list[int]], expected: list[list[int]]) -> bool:
    assert result == expected
    return True
