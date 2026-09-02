def run_min_difference(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.min_difference(nums)


def assert_min_difference(result: int, expected: int) -> bool:
    assert result == expected
    return True
