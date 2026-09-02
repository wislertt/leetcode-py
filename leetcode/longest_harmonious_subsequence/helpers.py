def run_find_lhs(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.find_lhs(nums)


def assert_find_lhs(result: int, expected: int) -> bool:
    assert result == expected
    return True
