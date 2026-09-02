def run_is_rectangle_cover(solution_class: type, rectangles: list[list[int]]):
    implementation = solution_class()
    return implementation.is_rectangle_cover(rectangles)


def assert_is_rectangle_cover(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
