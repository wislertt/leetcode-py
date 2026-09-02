def run_number_of_arithmetic_slices(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.number_of_arithmetic_slices(nums)


def assert_number_of_arithmetic_slices(result: int, expected: int) -> bool:
    assert result == expected
    return True
