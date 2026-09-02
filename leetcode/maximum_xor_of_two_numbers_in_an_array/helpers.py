def run_find_maximum_xor(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.find_maximum_xor(nums)


def assert_find_maximum_xor(result: int, expected: int) -> bool:
    assert result == expected
    return True
