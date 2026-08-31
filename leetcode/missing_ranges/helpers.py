def run_find_missing_ranges(solution_class: type, nums: list[int], lower: int, upper: int):
    implementation = solution_class()
    return implementation.find_missing_ranges(nums, lower, upper)


def assert_find_missing_ranges(result: list[list[int]], expected: list[list[int]]) -> bool:
    assert result == expected
    return True
