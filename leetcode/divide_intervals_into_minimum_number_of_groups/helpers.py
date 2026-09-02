def run_min_groups(solution_class: type, intervals: list[list[int]]):
    implementation = solution_class()
    return implementation.min_groups(intervals)


def assert_min_groups(result: int, expected: int) -> bool:
    assert result == expected
    return True
