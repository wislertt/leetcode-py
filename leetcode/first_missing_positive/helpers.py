def run_first_missing_positive(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.first_missing_positive(nums)


def assert_first_missing_positive(result: int, expected: int) -> bool:
    assert result == expected
    return True
