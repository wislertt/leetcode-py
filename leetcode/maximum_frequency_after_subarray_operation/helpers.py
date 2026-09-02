def run_max_frequency(solution_class: type, nums: list[int], k: int):
    implementation = solution_class()
    return implementation.max_frequency(nums, k)


def assert_max_frequency(result: int, expected: int) -> bool:
    assert result == expected
    return True
