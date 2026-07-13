def run_largest_number(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.largest_number(nums)


def assert_largest_number(result: str, expected: str) -> bool:
    assert result == expected
    return True
