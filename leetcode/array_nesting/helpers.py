def run_array_nesting(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.array_nesting(nums)


def assert_array_nesting(result: int, expected: int) -> bool:
    assert result == expected
    return True
