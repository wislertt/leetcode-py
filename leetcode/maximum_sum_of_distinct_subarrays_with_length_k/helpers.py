def run_maximum_subarray_sum(solution_class: type, nums: list[int], k: int):
    implementation = solution_class()
    return implementation.maximum_subarray_sum(nums, k)


def assert_maximum_subarray_sum(result: int, expected: int) -> bool:
    assert result == expected
    return True
