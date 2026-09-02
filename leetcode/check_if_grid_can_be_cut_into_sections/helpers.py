def run_check_valid_cuts(solution_class: type, n: int, rectangles: list[list[int]]):
    implementation = solution_class()
    return implementation.check_valid_cuts(n, rectangles)


def assert_check_valid_cuts(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
