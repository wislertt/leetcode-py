def run_min_subarray(solution_class: type, nums: list[int], p: int):
    implementation = solution_class()
    return implementation.min_subarray(nums, p)


def assert_min_subarray(result: int, expected: int) -> bool:
    assert result == expected
    return True
