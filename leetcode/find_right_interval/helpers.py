def run_find_right_interval(solution_class: type, intervals: list[list[int]]):
    implementation = solution_class()
    return implementation.find_right_interval(intervals)


def assert_find_right_interval(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
