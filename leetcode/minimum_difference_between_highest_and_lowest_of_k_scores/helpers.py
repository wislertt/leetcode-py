def run_minimum_difference(solution_class: type, nums: list[int], k: int):
    implementation = solution_class()
    return implementation.minimum_difference(nums, k)


def assert_minimum_difference(result: int, expected: int) -> bool:
    assert result == expected
    return True
