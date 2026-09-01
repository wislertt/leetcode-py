def run_minimum_deviation(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.minimum_deviation(nums)


def assert_minimum_deviation(result: int, expected: int) -> bool:
    assert result == expected
    return True
