def run_zero_filled_subarray(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.zero_filled_subarray(nums)


def assert_zero_filled_subarray(result: int, expected: int) -> bool:
    assert result == expected
    return True
