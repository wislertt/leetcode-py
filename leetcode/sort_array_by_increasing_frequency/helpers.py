def run_frequency_sort(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.frequency_sort(nums)


def assert_frequency_sort(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
