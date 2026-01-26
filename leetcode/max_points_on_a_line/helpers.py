def run_max_points(solution_class: type, points: list[list[int]]):
    implementation = solution_class()
    return implementation.max_points(points)


def assert_max_points(result: int, expected: int) -> bool:
    assert result == expected
    return True
