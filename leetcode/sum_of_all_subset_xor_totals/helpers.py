def run_subset_xor_sum(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.subset_xor_sum(nums)


def assert_subset_xor_sum(result: int, expected: int) -> bool:
    assert result == expected
    return True
