def run_can_sort_array(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.can_sort_array(nums)


def assert_can_sort_array(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
