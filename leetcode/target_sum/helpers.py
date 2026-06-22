def run_find_target_sum_ways(solution_class: type, nums: list[int], target: int):
    implementation = solution_class()
    return implementation.find_target_sum_ways(nums, target)


def assert_find_target_sum_ways(result: int, expected: int) -> bool:
    assert result == expected
    return True
