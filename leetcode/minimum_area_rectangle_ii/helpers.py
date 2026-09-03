def run_min_area_free_rect(solution_class: type, points: list[list[int]]):
    implementation = solution_class()
    return implementation.min_area_free_rect(points)


def assert_min_area_free_rect(result: float, expected: float) -> bool:
    assert abs(result - expected) < 1e-5
    return True
