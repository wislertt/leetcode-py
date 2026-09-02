def run_max_width_of_vertical_area(solution_class: type, points: list[list[int]]):
    implementation = solution_class()
    return implementation.max_width_of_vertical_area(points)


def assert_max_width_of_vertical_area(result: int, expected: int) -> bool:
    assert result == expected
    return True
