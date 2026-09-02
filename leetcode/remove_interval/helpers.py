def run_remove_interval(solution_class: type, intervals: list[list[int]], to_be_removed: list[int]):
    implementation = solution_class()
    return implementation.remove_interval(intervals, to_be_removed)


def assert_remove_interval(result: list[list[int]], expected: list[list[int]]) -> bool:
    assert result == expected
    return True
