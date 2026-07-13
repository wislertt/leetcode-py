def run_combination_sum4(solution_class: type, nums: list[int], target: int):
    implementation = solution_class()
    return implementation.combination_sum4(nums, target)


def assert_combination_sum4(result: int, expected: int) -> bool:
    assert result == expected
    return True
