def run_min_increment_for_unique(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.min_increment_for_unique(nums)


def assert_min_increment_for_unique(result: int, expected: int) -> bool:
    assert result == expected
    return True
