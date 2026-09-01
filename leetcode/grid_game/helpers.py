def run_grid_game(solution_class: type, grid: list[list[int]]):
    implementation = solution_class()
    return implementation.grid_game(grid)


def assert_grid_game(result: int, expected: int) -> bool:
    assert result == expected
    return True
