def run_check_possibility(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.check_possibility(nums)


def assert_check_possibility(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
