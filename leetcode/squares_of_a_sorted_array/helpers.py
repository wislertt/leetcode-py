def run_sorted_squares(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.sorted_squares(nums)


def assert_sorted_squares(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
