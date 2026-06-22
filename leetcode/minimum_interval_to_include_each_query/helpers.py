def run_min_interval(solution_class: type, intervals: list[list[int]], queries: list[int]):
    implementation = solution_class()
    return implementation.min_interval(intervals, queries)


def assert_min_interval(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
