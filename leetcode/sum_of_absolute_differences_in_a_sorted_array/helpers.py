def run_get_sum_absolute_differences(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.get_sum_absolute_differences(nums)


def assert_get_sum_absolute_differences(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
