def run_count_sub_islands(solution_class: type, grid1: list[list[int]], grid2: list[list[int]]):
    implementation = solution_class()
    return implementation.count_sub_islands(grid1, grid2)


def assert_count_sub_islands(result: int, expected: int) -> bool:
    assert result == expected
    return True
