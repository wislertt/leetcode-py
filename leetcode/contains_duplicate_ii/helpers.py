def run_contains_nearby_duplicate(solution_class: type, nums: list[int], k: int):
    implementation = solution_class()
    return implementation.contains_nearby_duplicate(nums, k)


def assert_contains_nearby_duplicate(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
