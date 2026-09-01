def run_rearrange_array(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.rearrange_array(nums)


def assert_rearrange_array(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
