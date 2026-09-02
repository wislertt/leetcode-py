def run_single_number(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.single_number(nums)


def assert_single_number(result: int, expected: int) -> bool:
    assert result == expected
    return True
