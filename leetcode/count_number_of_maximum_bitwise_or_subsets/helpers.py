def run_count_max_or_subsets(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.count_max_or_subsets(nums)


def assert_count_max_or_subsets(result: int, expected: int) -> bool:
    assert result == expected
    return True
