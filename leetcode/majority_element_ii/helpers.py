def run_majority_element(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.majority_element(nums)


def assert_majority_element(result: list[int], expected: list[int]) -> bool:
    assert set(result) == set(expected)
    return True
