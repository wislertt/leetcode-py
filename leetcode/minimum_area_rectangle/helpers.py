def run_min_area_rect(solution_class: type, points: list[list[int]]):
    implementation = solution_class()
    return implementation.min_area_rect(points)


def assert_min_area_rect(result: int, expected: int) -> bool:
    assert result == expected
    return True
