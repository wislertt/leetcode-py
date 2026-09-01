def run_minimum_size(solution_class: type, nums: list[int], max_operations: int):
    implementation = solution_class()
    return implementation.minimum_size(nums, max_operations)


def assert_minimum_size(result: int, expected: int) -> bool:
    assert result == expected
    return True
