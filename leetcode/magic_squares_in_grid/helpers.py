def run_num_magic_squares_inside(solution_class: type, grid: list[list[int]]):
    implementation = solution_class()
    return implementation.num_magic_squares_inside(grid)


def assert_num_magic_squares_inside(result: int, expected: int) -> bool:
    assert result == expected
    return True
