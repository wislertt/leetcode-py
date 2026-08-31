def run_num_enclaves(solution_class: type, grid: list[list[int]]):
    implementation = solution_class()
    return implementation.num_enclaves(grid)


def assert_num_enclaves(result: int, expected: int) -> bool:
    assert result == expected
    return True
