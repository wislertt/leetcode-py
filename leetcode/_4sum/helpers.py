from typing import List


def run_four_sum(solution_class: type, nums: List[int], target: int):
    implementation = solution_class()
    return implementation.four_sum(nums, target)


def assert_four_sum(result: List[List[int]], expected: List[List[int]]) -> bool:
    assert result == expected
    return True
