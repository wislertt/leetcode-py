from typing import List


def run_three_sum_closest(solution_class: type, nums: List[int], target: int):
    implementation = solution_class()
    return implementation.three_sum_closest(nums, target)


def assert_three_sum_closest(result: int, expected: int) -> bool:
    assert result == expected
    return True
