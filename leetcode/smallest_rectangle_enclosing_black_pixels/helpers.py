def run_min_area(solution_class: type, image: list[list[str]], x: int, y: int):
    implementation = solution_class()
    return implementation.min_area(image, x, y)


def assert_min_area(result: int, expected: int) -> bool:
    assert result == expected
    return True
