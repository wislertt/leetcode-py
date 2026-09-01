def run_maximum_safeness_factor(solution_class: type, grid: list[list[int]]):
    implementation = solution_class()
    return implementation.maximum_safeness_factor(grid)


def assert_maximum_safeness_factor(result: int, expected: int) -> bool:
    assert result == expected
    return True
