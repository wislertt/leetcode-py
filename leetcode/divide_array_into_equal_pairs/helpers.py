def run_divide_array_into_equal_pairs(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.divide_array_into_equal_pairs(nums)


def assert_divide_array_into_equal_pairs(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
