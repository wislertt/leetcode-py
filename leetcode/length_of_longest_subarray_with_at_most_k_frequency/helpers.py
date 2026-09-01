def run_max_subarray_length(solution_class: type, nums: list[int], k: int):
    implementation = solution_class()
    return implementation.max_subarray_length(nums, k)


def assert_max_subarray_length(result: int, expected: int) -> bool:
    assert result == expected
    return True
