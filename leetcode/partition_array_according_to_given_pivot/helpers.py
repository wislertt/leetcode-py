def run_pivot_array(solution_class: type, nums: list[int], pivot: int):
    implementation = solution_class()
    return implementation.pivot_array(nums, pivot)


def assert_pivot_array(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
