def run_rectangle_area(solution_class: type, rectangles: list[list[int]]):
    implementation = solution_class()
    return implementation.rectangle_area(rectangles)


def assert_rectangle_area(result: int, expected: int) -> bool:
    assert result == expected
    return True
