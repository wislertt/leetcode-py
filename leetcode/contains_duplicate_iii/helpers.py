def run_contains_nearby_almost_duplicate(
    solution_class: type, nums: list[int], index_diff: int, value_diff: int
):
    implementation = solution_class()
    return implementation.contains_nearby_almost_duplicate(nums, index_diff, value_diff)


def assert_contains_nearby_almost_duplicate(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
