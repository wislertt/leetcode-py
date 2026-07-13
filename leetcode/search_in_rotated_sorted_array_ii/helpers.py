def run_search(solution_class: type, nums: list[int], target: int):
    implementation = solution_class()
    return implementation.search(nums, target)


def assert_search(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
