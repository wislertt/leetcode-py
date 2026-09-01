def run_interchangeable_rectangles(solution_class: type, rectangles: list[list[int]]):
    implementation = solution_class()
    return implementation.interchangeable_rectangles(rectangles)


def assert_interchangeable_rectangles(result: int, expected: int) -> bool:
    assert result == expected
    return True
