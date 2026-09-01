def run_min_operations(solution_class: type, nums: list[int], x: int):
    implementation = solution_class()
    return implementation.min_operations(nums, x)


def assert_min_operations(result: int, expected: int) -> bool:
    assert result == expected
    return True
