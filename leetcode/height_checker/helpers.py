def run_height_checker(solution_class: type, heights: list[int]):
    implementation = solution_class()
    return implementation.height_checker(heights)


def assert_height_checker(result: int, expected: int) -> bool:
    assert result == expected
    return True
