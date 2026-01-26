def run_search_range(solution_class: type, nums: list[int], target: int):
    implementation = solution_class()
    return implementation.search_range(nums, target)


def assert_search_range(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
