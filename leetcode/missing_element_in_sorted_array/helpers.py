def run_missing_element(solution_class: type, nums: list[int], k: int):
    implementation = solution_class()
    return implementation.missing_element(nums, k)


def assert_missing_element(result: int, expected: int) -> bool:
    assert result == expected
    return True
