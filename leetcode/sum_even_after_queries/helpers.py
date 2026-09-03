def run_sum_even_after_queries(solution_class: type, nums: list[int], queries: list[list[int]]):
    implementation = solution_class()
    return implementation.sum_even_after_queries(nums, queries)


def assert_sum_even_after_queries(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
