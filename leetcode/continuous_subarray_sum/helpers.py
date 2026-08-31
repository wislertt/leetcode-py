def run_check_subarray_sum(solution_class: type, nums: list[int], k: int):
    implementation = solution_class()
    return implementation.check_subarray_sum(nums, k)


def assert_check_subarray_sum(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
