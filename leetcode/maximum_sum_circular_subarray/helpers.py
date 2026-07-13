def run_max_subarray_sum_circular(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.max_subarray_sum_circular(nums)


def assert_max_subarray_sum_circular(result: int, expected: int) -> bool:
    assert result == expected
    return True
