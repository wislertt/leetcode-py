def run_longest_monotonic_subarray(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.longest_monotonic_subarray(nums)


def assert_longest_monotonic_subarray(result: int, expected: int) -> bool:
    assert result == expected
    return True
