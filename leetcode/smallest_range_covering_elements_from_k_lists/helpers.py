def run_smallest_range(solution_class: type, nums: list[list[int]]):
    implementation = solution_class()
    return implementation.smallest_range(nums)


def assert_smallest_range(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
