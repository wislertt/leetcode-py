def run_max_width_ramp(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.max_width_ramp(nums)


def assert_max_width_ramp(result: int, expected: int) -> bool:
    assert result == expected
    return True
