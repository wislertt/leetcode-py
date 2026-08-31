def run_delete_and_earn(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.delete_and_earn(nums)


def assert_delete_and_earn(result: int, expected: int) -> bool:
    assert result == expected
    return True
