def run_pivot_index(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.pivot_index(nums)


def assert_pivot_index(result: int, expected: int) -> bool:
    assert result == expected
    return True
