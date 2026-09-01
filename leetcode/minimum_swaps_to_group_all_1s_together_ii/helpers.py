def run_min_swaps(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.min_swaps(nums)


def assert_min_swaps(result: int, expected: int) -> bool:
    assert result == expected
    return True
