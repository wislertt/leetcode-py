def run_count_range_sum(solution_class: type, nums: list[int], lower: int, upper: int):
    implementation = solution_class()
    return implementation.count_range_sum(nums, lower, upper)


def assert_count_range_sum(result: int, expected: int) -> bool:
    assert result == expected
    return True
