def run_num_distinct_islands(solution_class: type, grid: list[list[int]]):
    implementation = solution_class()
    return implementation.num_distinct_islands(grid)


def assert_num_distinct_islands(result: int, expected: int) -> bool:
    assert result == expected
    return True
