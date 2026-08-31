def run_is_convex(solution_class: type, points: list[list[int]]):
    implementation = solution_class()
    return implementation.is_convex(points)


def assert_is_convex(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
