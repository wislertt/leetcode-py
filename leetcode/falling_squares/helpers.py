def run_falling_squares(solution_class: type, positions: list[list[int]]):
    implementation = solution_class()
    return implementation.falling_squares(positions)


def assert_falling_squares(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
