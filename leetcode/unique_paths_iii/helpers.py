def run_unique_paths_iii(solution_class: type, grid: list[list[int]]):
    implementation = solution_class()
    return implementation.unique_paths_iii(grid)


def assert_unique_paths_iii(result: int, expected: int) -> bool:
    assert result == expected
    return True
