def run_intersection_size_two(solution_class: type, intervals: list[list[int]]):
    implementation = solution_class()
    return implementation.intersection_size_two(intervals)


def assert_intersection_size_two(result: int, expected: int) -> bool:
    assert result == expected
    return True
