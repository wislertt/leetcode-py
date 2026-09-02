def run_find_subsequences(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.find_subsequences(nums)


def assert_find_subsequences(result: list[list[int]], expected: list[list[int]]) -> bool:
    # Compare as multisets; element order inside each subsequence is meaningful
    result_sorted = sorted([list(sub) for sub in result])
    expected_sorted = sorted([list(sub) for sub in expected])
    assert result_sorted == expected_sorted
    return True
