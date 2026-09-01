def run_largest_unique_number(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.largest_unique_number(nums)


def assert_largest_unique_number(result: int, expected: int) -> bool:
    assert result == expected
    return True
