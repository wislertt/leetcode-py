def run_largest_local(solution_class: type, grid: list[list[int]]):
    implementation = solution_class()
    return implementation.largest_local(grid)


def assert_largest_local(result: list[list[int]], expected: list[list[int]]) -> bool:
    assert result == expected
    return True
