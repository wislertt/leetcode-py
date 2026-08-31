def run_least_bricks(solution_class: type, wall: list[list[int]]):
    implementation = solution_class()
    return implementation.least_bricks(wall)


def assert_least_bricks(result: int, expected: int) -> bool:
    assert result == expected
    return True
