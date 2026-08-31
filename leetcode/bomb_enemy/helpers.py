def run_max_killed_enemies(solution_class: type, grid: list[list[str]]):
    implementation = solution_class()
    return implementation.max_killed_enemies(grid)


def assert_max_killed_enemies(result: int, expected: int) -> bool:
    assert result == expected
    return True
