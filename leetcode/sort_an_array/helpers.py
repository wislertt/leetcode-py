def run_sort_array(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.sort_array(nums)


def assert_sort_array(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
