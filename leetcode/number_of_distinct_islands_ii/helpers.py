def run_num_distinct_islands_ii(solution_class: type, grid: list[list[int]]):
    implementation = solution_class()
    return implementation.num_distinct_islands_ii(grid)


def assert_num_distinct_islands_ii(result: int, expected: int) -> bool:
    assert result == expected
    return True
