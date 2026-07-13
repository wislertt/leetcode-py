def run_four_sum(solution_class: type, nums: list[int], target: int):
    implementation = solution_class()
    return implementation.four_sum(nums, target)


def assert_four_sum(result: list[list[int]], expected: list[list[int]]) -> bool:
    assert sorted(result) == sorted(expected)
    return True
