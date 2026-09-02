def run_constrained_subset_sum(solution_class: type, nums: list[int], k: int):
    implementation = solution_class()
    return implementation.constrained_subset_sum(nums, k)


def assert_constrained_subset_sum(result: int, expected: int) -> bool:
    assert result == expected
    return True
