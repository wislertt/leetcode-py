def run_minimum_effort_path(solution_class: type, heights: list[list[int]]):
    implementation = solution_class()
    return implementation.minimum_effort_path(heights)


def assert_minimum_effort_path(result: int, expected: int) -> bool:
    assert result == expected
    return True
