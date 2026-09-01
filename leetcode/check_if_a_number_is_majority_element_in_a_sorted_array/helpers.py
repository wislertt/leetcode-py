def run_is_majority_element(solution_class: type, nums: list[int], target: int):
    implementation = solution_class()
    return implementation.is_majority_element(nums, target)


def assert_is_majority_element(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
