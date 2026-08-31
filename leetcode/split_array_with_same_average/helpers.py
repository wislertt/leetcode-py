def run_split_array_same_average(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.split_array_same_average(nums)


def assert_split_array_same_average(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
