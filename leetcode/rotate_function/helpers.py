def run_max_rotate_function(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.max_rotate_function(nums)


def assert_max_rotate_function(result: int, expected: int) -> bool:
    assert result == expected
    return True
