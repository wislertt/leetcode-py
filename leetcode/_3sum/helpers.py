from typing import List


def run_three_sum(solution_class: type, nums: List[int]):
    implementation = solution_class()
    return implementation.three_sum(nums)


def assert_three_sum(result: List[List[int]], expected: List[List[int]]) -> bool:
    assert result == expected
    return True
