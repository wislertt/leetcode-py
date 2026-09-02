def run_can_divide_into_subsequences(solution_class: type, nums: list[int], k: int):
    implementation = solution_class()
    return implementation.can_divide_into_subsequences(nums, k)


def assert_can_divide_into_subsequences(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
