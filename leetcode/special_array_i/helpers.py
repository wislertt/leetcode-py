def run_is_array_special(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.is_array_special(nums)


def assert_is_array_special(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
