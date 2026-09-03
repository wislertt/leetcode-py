def run_is_possible(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.is_possible(nums)


def assert_is_possible(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
