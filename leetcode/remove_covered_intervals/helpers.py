def run_remove_covered_intervals(solution_class: type, intervals: list[list[int]]):
    implementation = solution_class()
    return implementation.remove_covered_intervals(intervals)


def assert_remove_covered_intervals(result: int, expected: int) -> bool:
    assert result == expected
    return True
