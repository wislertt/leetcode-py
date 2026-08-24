def run_get_food(solution_class: type, grid: list[list[str]]):
    import copy

    grid_copy = copy.deepcopy(grid)
    implementation = solution_class()
    return implementation.get_food(grid_copy)


def assert_get_food(result: int, expected: int) -> bool:
    assert result == expected
    return True
