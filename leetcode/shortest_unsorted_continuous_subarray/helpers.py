def run_find_unsorted_subarray(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.find_unsorted_subarray(nums)


def assert_find_unsorted_subarray(result: int, expected: int) -> bool:
    assert result == expected
    return True
