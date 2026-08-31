def run_find_peak_element(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.find_peak_element(nums)


def assert_find_peak_element(result: int, expected: int) -> bool:
    assert result == expected
    return True
