def run_two_sum(solution_class: type, nums: list[int], target: int):
    implementation = solution_class()
    return implementation.two_sum(nums, target)


def assert_two_sum(result: list[int], expected: list[int]) -> bool:
    # Sort both result and expected for comparison since order doesn't matter
    result_sorted = [sorted(subset) for subset in sorted(result)]
    expected_sorted = [sorted(subset) for subset in sorted(expected)]
    assert result_sorted == expected_sorted
    return True
