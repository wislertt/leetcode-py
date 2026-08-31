def run_find_disappeared_numbers(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.find_disappeared_numbers(nums)


def assert_find_disappeared_numbers(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
