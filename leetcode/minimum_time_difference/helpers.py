def run_find_min_difference(solution_class: type, time_points: list[str]):
    implementation = solution_class()
    return implementation.find_min_difference(time_points)


def assert_find_min_difference(result: int, expected: int) -> bool:
    assert result == expected
    return True
