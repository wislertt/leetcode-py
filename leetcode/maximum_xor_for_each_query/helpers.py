def run_get_maximum_xor(solution_class: type, nums: list[int], maximum_bit: int):
    implementation = solution_class()
    return implementation.get_maximum_xor(nums, maximum_bit)


def assert_get_maximum_xor(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
