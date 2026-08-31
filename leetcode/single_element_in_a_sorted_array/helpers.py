def run_single_non_duplicate(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.single_non_duplicate(nums)


def assert_single_non_duplicate(result: int, expected: int) -> bool:
    assert result == expected
    return True
