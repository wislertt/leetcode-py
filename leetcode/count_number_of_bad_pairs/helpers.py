def run_count_bad_pairs(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.count_bad_pairs(nums)


def assert_count_bad_pairs(result: int, expected: int) -> bool:
    assert result == expected
    return True
