def run_min_cost(solution_class: type, grid: list[list[int]]):
    implementation = solution_class()
    return implementation.min_cost(grid)


def assert_min_cost(result: int, expected: int) -> bool:
    assert result == expected
    return True
