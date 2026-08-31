def run_find_max_ones(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.find_max_ones(nums)


def assert_find_max_ones(result: int, expected: int) -> bool:
    assert result == expected
    return True
