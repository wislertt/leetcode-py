def run_next_greater_elements(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.next_greater_elements(nums)


def assert_next_greater_elements(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
