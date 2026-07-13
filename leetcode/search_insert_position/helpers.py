def run_search_insert(solution_class: type, nums: list[int], target: int):
    implementation = solution_class()
    return implementation.search_insert(nums, target)


def assert_search_insert(result: int, expected: int) -> bool:
    assert result == expected
    return True
