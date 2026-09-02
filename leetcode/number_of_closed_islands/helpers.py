def run_closed_islands(solution_class: type, grid: list[list[int]]):
    implementation = solution_class()
    return implementation.closed_islands(grid)


def assert_closed_islands(result: int, expected: int) -> bool:
    assert result == expected
    return True
