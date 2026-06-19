def run_subsets_with_dup(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.subsets_with_dup(nums)


def assert_subsets_with_dup(result: list[list[int]], expected: list[list[int]]) -> bool:
    # Sort each subset and the outer list for order-independent comparison
    result_sorted = sorted([sorted(subset) for subset in result])
    expected_sorted = sorted([sorted(subset) for subset in expected])
    assert result_sorted == expected_sorted
    return True
