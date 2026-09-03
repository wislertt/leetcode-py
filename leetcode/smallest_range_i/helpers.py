def run_smallest_range_i(solution_class: type, nums: list[int], k: int):
    implementation = solution_class()
    return implementation.smallest_range_i(nums, k)


def assert_smallest_range_i(result: int, expected: int) -> bool:
    assert result == expected
    return True
