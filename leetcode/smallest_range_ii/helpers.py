def run_smallest_range_ii(solution_class: type, nums: list[int], k: int):
    implementation = solution_class()
    return implementation.smallest_range_ii(nums, k)


def assert_smallest_range_ii(result: int, expected: int) -> bool:
    assert result == expected
    return True
