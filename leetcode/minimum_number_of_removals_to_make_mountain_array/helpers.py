def run_minimum_mountain_removals(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.minimum_mountain_removals(nums)


def assert_minimum_mountain_removals(result: int, expected: int) -> bool:
    assert result == expected
    return True
