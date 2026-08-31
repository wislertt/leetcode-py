def run_cherry_pickup(solution_class: type, grid: list[list[int]]):
    implementation = solution_class()
    return implementation.cherry_pickup(grid)


def assert_cherry_pickup(result: int, expected: int) -> bool:
    assert result == expected
    return True
