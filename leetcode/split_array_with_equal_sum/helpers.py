def run_split_array(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.split_array(nums)


def assert_split_array(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
