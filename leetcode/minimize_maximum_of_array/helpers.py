def run_minimize_array_value(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.minimize_array_value(nums)


def assert_minimize_array_value(result: int, expected: int) -> bool:
    assert result == expected
    return True
