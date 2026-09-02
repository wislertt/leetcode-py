def run_count_smaller(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.count_smaller(nums)


def assert_count_smaller(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
