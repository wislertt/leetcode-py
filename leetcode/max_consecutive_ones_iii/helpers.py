def run_longest_ones(solution_class: type, nums: list[int], k: int):
    implementation = solution_class()
    return implementation.longest_ones(nums, k)


def assert_longest_ones(result: int, expected: int) -> bool:
    assert result == expected
    return True
