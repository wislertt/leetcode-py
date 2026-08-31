def run_find_error_nums(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.find_error_nums(nums)


def assert_find_error_nums(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
