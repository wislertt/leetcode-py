def run_find_max_fish(solution_class: type, grid: list[list[int]]):
    implementation = solution_class()
    return implementation.find_max_fish(grid)


def assert_find_max_fish(result: int, expected: int) -> bool:
    assert result == expected
    return True
