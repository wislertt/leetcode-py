def run_third_max(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.third_max(nums)


def assert_third_max(result: int, expected: int) -> bool:
    assert result == expected
    return True
