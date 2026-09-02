def run_max_ascending_sum(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.max_ascending_sum(nums)


def assert_max_ascending_sum(result: int, expected: int) -> bool:
    assert result == expected
    return True
