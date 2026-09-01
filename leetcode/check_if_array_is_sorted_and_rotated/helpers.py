def run_check(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.check(nums)


def assert_check(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
