def run_swim_in_water(solution_class: type, grid: list[list[int]]):
    implementation = solution_class()
    return implementation.swim_in_water(grid)


def assert_swim_in_water(result: int, expected: int) -> bool:
    assert result == expected
    return True
