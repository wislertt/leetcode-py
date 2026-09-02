def run_range_sum(solution_class: type, nums: list[int], n: int, left: int, right: int):
    implementation = solution_class()
    return implementation.range_sum(nums, n, left, right)


def assert_range_sum(result: int, expected: int) -> bool:
    assert result == expected
    return True
