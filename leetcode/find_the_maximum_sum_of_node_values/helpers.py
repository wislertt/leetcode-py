def run_maximum_value_sum(solution_class: type, nums: list[int], k: int, edges: list[list[int]]):
    implementation = solution_class()
    return implementation.maximum_value_sum(nums, k, edges)


def assert_maximum_value_sum(result: int, expected: int) -> bool:
    assert result == expected
    return True
