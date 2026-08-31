def run_num_subarrays_with_sum(solution_class: type, nums: list[int], goal: int):
    implementation = solution_class()
    return implementation.num_subarrays_with_sum(nums, goal)


def assert_num_subarrays_with_sum(result: int, expected: int) -> bool:
    assert result == expected
    return True
