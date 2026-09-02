def run_count_fair_pairs(solution_class: type, nums: list[int], lower: int, upper: int):
    implementation = solution_class()
    return implementation.count_fair_pairs(nums, lower, upper)


def assert_count_fair_pairs(result: int, expected: int) -> bool:
    assert result == expected
    return True
