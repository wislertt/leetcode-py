def run_is_monotonic(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.is_monotonic(nums)


def assert_is_monotonic(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
