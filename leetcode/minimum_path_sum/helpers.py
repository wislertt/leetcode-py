def run_min_path_sum(solution_class: type, grid: list[list[int]]):
    implementation = solution_class()
    return implementation.min_path_sum(grid)


def assert_min_path_sum(result: int, expected: int) -> bool:
    assert result == expected
    return True
