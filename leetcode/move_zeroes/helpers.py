def run_move_zeroes(solution_class: type, nums: list[int]):
    nums_copy = nums.copy()
    implementation = solution_class()
    implementation.move_zeroes(nums_copy)
    return nums_copy


def assert_move_zeroes(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
