def run_find_min_arrow_shots(solution_class: type, points: list[list[int]]):
    implementation = solution_class()
    return implementation.find_min_arrow_shots(points)


def assert_find_min_arrow_shots(result: int, expected: int) -> bool:
    assert result == expected
    return True
