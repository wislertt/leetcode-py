def run_longest_subarray(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.longest_subarray(nums)


def assert_longest_subarray(result: int, expected: int) -> bool:
    assert result == expected
    return True
