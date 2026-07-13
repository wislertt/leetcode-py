def run_get_concatenation(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.get_concatenation(nums)


def assert_get_concatenation(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
