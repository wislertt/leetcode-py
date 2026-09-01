def run_special_array(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.special_array(nums)


def assert_special_array(result: int, expected: int) -> bool:
    assert result == expected
    return True
