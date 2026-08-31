def run_find_max_consecutive_ones(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.find_max_consecutive_ones(nums)


def assert_find_max_consecutive_ones(result: int, expected: int) -> bool:
    assert result == expected
    return True
