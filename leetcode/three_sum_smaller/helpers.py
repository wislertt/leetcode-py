def run_three_sum_smaller(solution_class: type, nums: list[int], target: int):
    implementation = solution_class()
    return implementation.three_sum_smaller(nums, target)


def assert_three_sum_smaller(result: int, expected: int) -> bool:
    assert result == expected
    return True
