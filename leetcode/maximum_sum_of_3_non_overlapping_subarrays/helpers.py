def run_max_sum_of_three_subarrays(solution_class: type, nums: list[int], k: int):
    implementation = solution_class()
    return implementation.max_sum_of_three_subarrays(nums, k)


def assert_max_sum_of_three_subarrays(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
