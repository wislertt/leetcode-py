def run_largest_triangle_area(solution_class: type, points: list[list[int]]):
    implementation = solution_class()
    return implementation.largest_triangle_area(points)


def assert_largest_triangle_area(result: float, expected: float) -> bool:
    assert abs(result - expected) < 1e-05
    return True
