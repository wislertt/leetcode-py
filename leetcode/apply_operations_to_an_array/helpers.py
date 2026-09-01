def run_apply_operations(solution_class: type, nums: list[int]):
    nums_copy = nums.copy()
    implementation = solution_class()
    return implementation.apply_operations(nums_copy)


def assert_apply_operations(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
