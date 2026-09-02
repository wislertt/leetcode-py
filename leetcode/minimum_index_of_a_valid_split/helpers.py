def run_minimum_index(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.minimum_index(nums)


def assert_minimum_index(result: int, expected: int) -> bool:
    assert result == expected
    return True
