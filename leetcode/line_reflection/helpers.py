def run_is_reflected(solution_class: type, points: list[list[int]]):
    implementation = solution_class()
    return implementation.is_reflected(points)


def assert_is_reflected(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
