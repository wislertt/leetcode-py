def run_find_132pattern(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.find_132pattern(nums)


def assert_find_132pattern(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
