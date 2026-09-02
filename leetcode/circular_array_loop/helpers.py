def run_circular_array_loop(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.circular_array_loop(nums)


def assert_circular_array_loop(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
