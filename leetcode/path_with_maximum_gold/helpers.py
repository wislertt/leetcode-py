def run_get_maximum_gold(solution_class: type, grid: list[list[int]]):
    implementation = solution_class()
    return implementation.get_maximum_gold(grid)


def assert_get_maximum_gold(result: int, expected: int) -> bool:
    assert result == expected
    return True
