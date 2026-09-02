def run_min_moves2(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.min_moves2(nums)


def assert_min_moves2(result: int, expected: int) -> bool:
    assert result == expected
    return True
