def run_lexicographically_smallest_array(solution_class: type, nums: list[int], limit: int):
    implementation = solution_class()
    return implementation.lexicographically_smallest_array(nums, limit)


def assert_lexicographically_smallest_array(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
