def run_num_subarray_bounded_max(solution_class: type, nums: list[int], left: int, right: int):
    implementation = solution_class()
    return implementation.num_subarray_bounded_max(nums, left, right)


def assert_num_subarray_bounded_max(result: int, expected: int) -> bool:
    assert result == expected
    return True
